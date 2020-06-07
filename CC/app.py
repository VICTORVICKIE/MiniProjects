from flask import Flask,render_template,url_for,session,request,logging,redirect,flash
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
from forms import *
from password import p
from sqlhelpers import *
from functools import wraps

app = Flask(__name__)									#initializing  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = p
app.config['MYSQL_DB'] = 'CAMPUS_COINS'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

def is_logged_in(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash("Unauthorized!! Please Login","danger")
			return redirect(url_for('login'))
	return wrap

@app.route("/")											#Home page
def index():
	return render_template('index.html') 


@app.route("/register",methods=['GET','POST'])			#registration page
def register():
	form = Registerform(request.form)
	users = Table("users","name","email","username","password")

	if request.method == 'POST' and form.validate():
		username = form.username.data
		email = form.email.data
		name = form.name.data

		if isnewuser(username): 						#check new user
			password = sha256_crypt.hash(form.password.data)
			users.insert(name,email,username,password)
			log_in_user(username)
			return redirect(url_for('dashboard'))
		
		else:
			flash('user already exists','danger')
			return redirect(url_for('login'))	
	return render_template('register.html',form=form)

@app.route("/login", methods=['GET','POST'])			#login page
def login():
	if request.method == 'POST':
		username = request.form['username']
		candidate = request.form['password']

		users = Table("users","name","email","username","password")
		user = users.getone("username",username)
		accpass = user.get('password')

		if accpass is None:
			flash("Username not found",'danger')
			return redirect(url_for('login'))

		else:
			if sha256_crypt.verify(candidate,accpass):	
				log_in_user(username)
				flash("You are logged in",'success')
				return redirect(url_for("dashboard"))
			else:
				flash("Invalid Password",'danger')
				return redirect(url_for('login'))

	return render_template('login.html')

@app.route("/logout")									#logout
@is_logged_in
def logout():
	session.clear()
	flash("Logout success","success")
	return redirect(url_for('login'))


@app.route("/dashboard")
@is_logged_in								#user dashboard
def dashboard():
	return render_template('dashboard.html',session=session)


def log_in_user(username):
	users = Table("users","name","email","username","password")
	user = users.getone("username",username)

	session["logged_in"] = True
	session["username"] = username
	session["name"] = user.get('name')
	session["email"] = user.get('email')


if __name__ == '__main__':
	app.secret_key = 'CC123'
	app.run(debug=True)
