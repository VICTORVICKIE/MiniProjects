from flask import Flask,render_template,url_for,session,request,logging,redirect,flash
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
from forms import *
from password import p
from sqlhelpers import *

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = p
app.config['MYSQL_DB'] = 'CAMPUS_COINS'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route("/")
def index():
	return render_template('index.html') 



@app.route("/register",methods=['GET','POST'])
def register():
	form = Registerform(request.form)
	users = Table("users","name","email","username","password")

	if request.method == 'POST' and form.validate():
		username = form.username.data
		email = form.email.data
		name = form.name.data

		if isnewuser(username): #check new user
			password = sha256_crypt.hash(form.password.data)
			users.insert(name,email,username,password)
			log_in_user(username)
			return redirect(url_for('dashboard'))
		else:
			flash('user already exists','danger')	
	return render_template('register.html',form=form)

@app.route("/dashboard")
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
