from tkinter import*
import tkinter.ttk as t
from PIL import ImageTk,Image
from turtle import*
from pyglet import*
win=Tk()
w=win.winfo_screenwidth()
h=win.winfo_screenheight()
win.geometry("%dx%d+0+0"%(w-100,h-100))
win.title("VIRTUAL LAB")
nb=t.Notebook(win)
s1=t.Frame(nb)
s2=t.Frame(nb)
win.iconbitmap('recicon.ico')
img=ImageTk.PhotoImage(Image.open("rec.png"))
imglab1=Label(s1,image=img)
imglab2=Label(s2,image=img)
imglab1.grid(row=1,column=0)
imglab2.grid(row=1,column=0)
label1=Label(s1,text="VIGNESH KUMAR.S\n\nSANTHOSH RAAJAA.S\n\nMANIKANDAN.S\n\nDHIVYADHARSHINI.S\n\nSARAN KUMAR",font=("ARIAL",15))
label1.grid(row=1,column=2)
label2=Label(s2,text="VIGNESH KUMAR.S\n\nSANTHOSH RAAJAA.S\n\nMANIKANDAN.S\n\nDHIVYADHARSHINI.S\n\nSARAN KUMAR",font=("ARIAL",15))
label2.grid(row=1,column=2)
nb.add(s2,text="Port Timing Diagram for 2s Engine")
nb.add(s1,text="Valve Timing Diagram for 4s Engine")
nb.grid(row=0,column=0)

#=======================4s====================
a=IntVar()
b=IntVar()
c=IntVar()
d=IntVar()
a1=IntVar()
b1=IntVar()
c1=IntVar()
d1=IntVar()
cirm=IntVar()
deg1=0
deg2=0
deg3=0
deg4=0
def anime4s():
    animation=image.load_animation('4s.gif')
    animSprite=sprite.Sprite(animation)
    w=animSprite.width
    h=animSprite.height
    global window
    window=window.Window(width=w,height=h,caption="FOUR STROKE Engine ")
    r,g,b,alpha=255,255,255,0
    gl.glClearColor(r,g,b,alpha)
    @window.event
    def on_draw():
        window.clear()
        animSprite.draw()
    app.run()
def degrees(w,x,y,z,cir):

    global deg1
    global deg2
    global deg3
    global deg4
    cir=cirmf.get()
    deg1= (float(w)*360)/float(cir)
    a1.set(str(round(deg1,3))+" "+"Before TDC")
    deg2= (float(x)*360)/float(cir)
    b1.set(str(round(deg2,3))+" "+"After TDC")
    deg3= (float(y)*360)/float(cir)
    c1.set(str(round(deg3,3))+" "+"Before BDC")
    deg4= (float(z)*360)/float(cir)
    d1.set(str(round(deg4,3))+" "+"After BDC")
    return deg1,deg2,deg3,deg4

def involute(deg1,deg2,deg3,deg4):
    resetscreen()
    a=Screen()
    a.title('Valve Timing Diagram')
    a.setup(800,700)
    t=Turtle();t.color('blue')
    t.left(90)

    #axis(x,y)
    xaxis=Turtle();xaxis.speed('fastest')
    yaxis=Turtle();yaxis.speed('fastest')

    xaxis.color('black')
    xaxis.backward(350)
    xaxis.fd(700)
    yaxis.color('black')
    yaxis.left(90)
    yaxis.backward(300)
    yaxis.write('BDC',font=(10))
    yaxis.fd(650)
    yaxis.up()
    yaxis.fd(-20);yaxis.right(90);yaxis.fd(20)
    yaxis.down()
    yaxis.write('TDC',font=(10))
    yaxis.up();yaxis.fd(-20);yaxis.left(90);yaxis.fd(20)

    t.up()
    t.fd(160)
    t.pendown()
    t.right(90)
    for i in range(0,40,5):
        t.fd(1)
        d=-4*(40+i)
        t.circle(d,90)
        t.speed('fastest')


        
    t.up()#ivo
    t.goto(0,0)
    t.down()
    t.setheading(0)
    t.left(90+deg1)
    t.color("orange")
    t.fd(160)
    t.right(90)
    t.color('blue')
    t.circle(-160,deg1)
    #arrow
    t.setheading(180)
    t.circle(160,deg1)
    t.right(45)
    t.fd(-15)
    t.fd(15)
    t.left(90)
    t.fd(-15)
    t.up();t.setheading(0);t.fd(-30);t.down()
    t.write("IVO",font=(7))


    t.up()#ivc
    t.goto(0,0)
    t.down()
    t.setheading(0)
    t.right(90+deg2)
    t.color("brown")
    t.fd(200)
#arrow
    t.setheading(-45)
    t.right(-45)
    t.fd(15)
    t.fd(-15)
    t.left(-90)
    t.fd(15)
    t.fd(-15)
    t.setheading(-45)
    t.right(45)
    t.fd(-15)
    t.fd(15)
    t.left(90)
    t.fd(-15)
    t.up();t.setheading(0);t.fd(30);t.down()
    t.write("IVC",font=(7))
    
    

    t.up()#evo
    t.goto(0,0)
    t.down()
    t.setheading(0)
    t.right(90-deg3)
    t.color("gray")
    t.fd(250)

    #arrow
    t.setheading(-45)
    t.right(-45)
    t.fd(15)
    t.fd(-15)
    t.left(-90)
    t.fd(15)
    t.fd(-15)
    t.setheading(-45)
    t.right(45)
    t.fd(-15)
    t.fd(15)
    t.left(90)
    t.fd(-15)
    t.up();t.setheading(0);t.fd(30);t.down()
    t.write("EVO",font=(7))

    

    t.up()#evc
    t.goto(0,0)
    t.down()
    t.setheading(0)
    t.left(90-deg4)
    t.color("yellow")
    t.fd(320)
    t.left(90)
    t.color("blue")
    t.circle(320,deg4)

    #arrow
    t.setheading(0)
    t.circle(-320,deg4)
    t.right(45)
    t.fd(-15)
    t.fd(15)
    t.left(90)
    t.fd(-15)
    t.up();t.setheading(0);t.fd(30);t.down()
    t.write("EVC",font=(7))

    t.hideturtle()


    #mark angle
    ma=Turtle();ma.speed('fastest')
    ma.left(90+deg1)
    ma.fd(50)
    ma.right(90)
    ma.circle(-50,deg1)#ivo
    
    ma.fd(-100);ma.write(round(deg1,2),font=(5))

    ma.up()#ivc
    ma.goto(0,0)
    ma.down()
    ma.setheading(0)
    ma.right(90+deg2)
    ma.fd(50)
    ma.left(90)
    ma.circle(50,deg2)
    ma.fd(-100);ma.write(round(deg2,2),font=(5))


    ma.up()#evo
    ma.goto(0,0)
    ma.down()
    ma.setheading(0)
    ma.right(90-deg3)
    ma.fd(70)
    ma.left(90)
    ma.circle(70,-deg3)
    ma.fd(100);ma.write(round(deg3,2),font=(5))


    ma.up()#evc
    ma.goto(0,0)
    ma.down()
    ma.setheading(0)
    ma.left(90-deg4)
    ma.fd(70)
    ma.right(90)
    ma.circle(-70,-deg4)
    ma.fd(100);ma.write(round(deg4,2),font=(5))

    ma.hideturtle()



    #writing text
    tx=Turtle();tx.color('red');tx.speed("fastest")
    tx.up()
    tx.goto(307.0,207.0)
    tx.down()
    tx.write('After TDC',font=(10))

    tx.up()
    tx.goto(-340.0,218.0)
    tx.down()
    tx.write('Before TDC',font=(10))

    tx.up()
    tx.goto(-313.0,-240.0)
    tx.down()
    tx.write('After BDC',font=(10))

    tx.up()
    tx.goto(284.0,-231.0)
    tx.down()
    tx.write('Before BDC',font=(10))

    tx.up();tx.goto(70,22);tx.down()
    tx.write('SUCTION',font=(10))

    tx.up();tx.goto(-190,15);tx.down()
    tx.write('COMPRESSION',font=(10))

    tx.up();tx.goto(150,-100);tx.down()
    tx.write('POWER',font=(10))

    tx.up();tx.goto(-150,245);tx.down()
    tx.write('EXHAUST',font=(10))
    tx.up();tx.goto(190,240);tx.setheading(-45);tx.down();tx.circle(-340,20)



event=Label(s1,text="Event",font=("calibri",20,"underline bold italic"))
event.grid(row=2,column=0,padx=20,pady=20)
Distance=Label(s1,text="Distance from\ntheir respective\n dead centres in cm",font=("calibri",20,"underline bold italic"))
Distance.grid(row=2,column=1,padx=10,pady=10)
Valve=Label(s1,text="Valve opening period in\ndegrees",font=("calibri",20,"underline bold italic"))
Valve.grid(row=2,column=2,padx=10,pady=10)


ivo=Label(s1,text="Inlet valve opens",font=("calibri",15," bold italic"))
ivo.grid(row=3,column=0,padx=10,pady=10)
ivc=Label(s1,text="Inlet valve closes",font=("calibri",15," bold italic"))
ivc.grid(row=4,column=0,padx=10,pady=10)
evo=Label(s1,text="Exhaust valve opens",font=("calibri",15," bold italic"))
evo.grid(row=5,column=0,padx=10,pady=10)
evc=Label(s1,text="Exhaust valve closes",font=("calibri",15," bold italic"))
evc.grid(row=6,column=0,padx=10,pady=10)


ivo1=Entry(s1,textvariable=a)
ivo1.grid(row=3,column=1,padx=10,pady=10)
ivc2=Entry(s1,textvariable=b)
ivc2.grid(row=4,column=1,padx=10,pady=10)
evo3=Entry(s1,textvariable=c)
evo3.grid(row=5,column=1,padx=10,pady=10)
evc4=Entry(s1,textvariable=d)
evc4.grid(row=6,column=1,padx=10,pady=10)


ivo_p=Entry(s1,textvariable=a1,state=DISABLED)
ivo_p.grid(row=3,column=2,padx=10,pady=10)
ivc_p=Entry(s1,textvariable=b1,state=DISABLED)
ivc_p.grid(row=4,column=2,padx=10,pady=10)
evo_p=Entry(s1,textvariable=c1,state=DISABLED)

evo_p.grid(row=5,column=2,padx=10,pady=10)
evc_p=Entry(s1,textvariable=d1,state=DISABLED)
evc_p.grid(row=6,column=2,padx=10,pady=10)

ci=Label(s1,text="Circumference",font=("calibri",15," bold italic"))
ci.grid(row=7,column=0,padx=10,pady=10)

cirmf=Entry(s1,textvariable=cirm)
cirmf.grid(row=7,column=1,padx=10,pady=10)

button=Button(s1,text="calculate",command=lambda:degrees(ivo1.get(),ivc2.get(),evo3.get(),evc4.get(),cirmf.get()))
button.grid(row=7,column=2,padx=10,pady=10)
button=Button(s1,text="plot",command=lambda:involute(deg1,deg2,deg3,deg4))
button.grid(row=7,column=3,padx=10,pady=10)
button=Button(s1,text="Animate",command=anime4s)
button.grid(row=8,column=3,padx=10,pady=10)



#===============================2s==================
a2=IntVar()
b2=IntVar()
c2=IntVar()
d2=IntVar()
a3=IntVar()
b3=IntVar()
c3=IntVar()
d3=IntVar()
cirm2=IntVar()
deg5=0
deg6=0
deg7=0
deg8=0
def anime2s():
    animation=image.load_animation('2s.gif')
    animSprite=sprite.Sprite(animation)
    w=animSprite.width
    h=animSprite.height
    global wind
    wind=window.Window(width=w,height=h,caption="TWO STROKE Engine ")
    r,g,b,alpha=255,255,255,0
    gl.glClearColor(r,g,b,alpha)
    @wind.event
    def on_draw():
        wind.clear()
        animSprite.draw()
    app.run()

def degrees1(w1,x1,y1,z1,cir1):

    global deg5
    global deg6
    global deg7
    global deg8
    
    cir1=cirmfs.get()
    deg5= (float(w1)*360)/float(cir1)
    a3.set(str(round(deg5,3))+" "+"Before BDC")
    deg6 = (float(x1)*360)/float(cir1)
    b3.set(str(round(deg6,3))+" "+"After BDC")
    deg7= (float(y1)*360)/float(cir1)
    c3.set(str(round(deg7,3))+" "+"Before BDC")
    deg8= (float(z1)*360)/float(cir1)
    d3.set(str(round(deg8,3))+" "+"After BDC")
    return deg5,deg6,deg7,deg8

def circle(deg5,deg6,deg7,deg8):
  
    resetscreen()
    b=Screen()
    b.title('Port Timing Diagram')
    b.setup(800,700)
    sk=Turtle() ; sk.color('blue');sk.speed('fastest')
    sk.up();sk.left(90);sk.fd(280);sk.right(90)
    sk.down()

    sk.circle(-280)

    #axis(x,y)
    xaxis=Turtle();xaxis.speed('fastest')
    yaxis=Turtle();yaxis.speed('fastest')

    xaxis.color('black')
    xaxis.backward(350)
    xaxis.fd(700)
    yaxis.color('black')
    yaxis.left(90)
    yaxis.backward(350)
    yaxis.write('BDC',font=(10))
    yaxis.fd(700)
    yaxis.up()
    yaxis.fd(-20);yaxis.right(90);yaxis.fd(20)
    yaxis.down()
    yaxis.write('TDC',font=(10))
    yaxis.up();yaxis.fd(-20);yaxis.left(90);yaxis.fd(20)


    #TPO
    sk.up()
    sk.goto(0,0)
    sk.down()
    sk.setheading(0)
    sk.right(90-deg7)
    sk.color("brown")#angle
    sk.fd(280)
    sk.up();sk.setheading(0);sk.fd(30);sk.down()
    sk.write('TPO',font=(10))
    sk.up()
    sk.goto(0,0)
    sk.down()
    sk.setheading(0)
    sk.right(90-deg7)   
    sk.fd(50);sk.right(90);sk.circle(-50,deg7)
    sk.up();sk.setheading(-45);sk.fd(30);sk.down()
    sk.write(round(deg7,2),font=(5))

    sk.color("black")
    sk.up();sk.home();sk.setheading(-90);sk.fd(250);sk.down()
    sk.setheading(0);sk.circle(250,deg7)
    sk.up();sk.home();sk.setheading(-90);sk.fd(250);sk.down()
    sk.setheading(180);sk.circle(-250,deg8)
    


    #EPO
    sk.up()
    sk.goto(0,0)
    sk.down()
    sk.setheading(0)
    sk.right(90-deg5)
    sk.color("yellow")#angle
    sk.fd(280)
    sk.up();sk.setheading(0);sk.fd(30);sk.down()
    sk.write('EPO',font=(10))
    sk.up()
    sk.goto(0,0)
    sk.down()
    sk.setheading(0)
    sk.right(90-deg5)   
    sk.fd(100);sk.right(90);sk.circle(-100,deg5)#get change the circle angle
    sk.up();sk.setheading(-45);sk.fd(30);sk.down()
    sk.write(round(deg5,2),font=(5))



    #TPC
    sk.up()
    sk.goto(0,0)
    sk.down()
    sk.setheading(0)
    sk.right(90+deg8)
    sk.color("gray")#angle
    sk.fd(280)
    sk.up();sk.setheading(0);sk.fd(-50);sk.down()
    sk.write('TPC',font=(10))
    sk.up()
    sk.goto(0,0)
    sk.down()
    sk.setheading(0)
    sk.right(90+deg8)   
    sk.fd(130);sk.left(90)
    sk.circle(130,deg8)
    sk.up();sk.setheading(-150);sk.fd(50);sk.down()
    sk.write(round(deg8,2),font=(2))




    #EPC
    sk.up()
    sk.goto(0,0)
    sk.down()
    sk.setheading(0)
    sk.right(90+deg6)
    sk.color("orange")#angle
    sk.fd(280)
    sk.up();sk.setheading(0);sk.fd(-50);sk.down()
    sk.write('EPC',font=(10))
    sk.up()
    sk.goto(0,0)
    sk.down()
    sk.setheading(0)
    sk.right(90+deg6)   
    sk.fd(180);sk.left(90)
    sk.circle(180,deg6)
    sk.up();sk.setheading(-150);sk.fd(50);sk.down()
    sk.write(round(deg6,2),font=(2))


    sk.up();sk.home();sk.down()
    sk.setheading(135)
    sk.color("black")
    for i in range(15):
        sk.fd(10)
        sk.up();sk.fd(10);sk.down()
    sk.up();sk.setheading(0);sk.fd(-20);sk.down()
    sk.write('IVO',font=(10))

    sk.up();sk.home();sk.down()
    
    sk.setheading(45)
    sk.color("black")
    for i in range(15):
        sk.fd(10)
        sk.up();sk.fd(10);sk.down()
    sk.up();sk.setheading(0);sk.fd(20);sk.down()
    sk.write('IVC',font=(10))

    sk.up();sk.home();sk.down()
    
    sk.setheading(110)
    sk.color("black")
    for i in range(15):
        sk.fd(10)
        sk.up();sk.fd(10);sk.down()
    sk.up();sk.setheading(0);sk.fd(-20);sk.down()
    sk.write('IGN',font=(10))
    sk.hideturtle()
    

    #writing text
    tx=Turtle();tx.color('red');tx.speed("fastest")
    tx.up()
    tx.goto(307.0,207.0)
    tx.down()
    tx.write('After TDC',font=(10))

    tx.up()
    tx.goto(-340.0,218.0)
    tx.down()
    tx.write('Before TDC',font=(10))

    tx.up()
    tx.goto(-313.0,-240.0)
    tx.down()
    tx.write('After BDC',font=(10))

    tx.up()
    tx.goto(284.0,-231.0)
    tx.down()
    tx.write('Before BDC',font=(10))

    tx.up();tx.goto(-380.0,148.0);tx.down()
    tx.write('COMPRESSION',font=(10))

    tx.up();tx.goto(257.0,150.0);tx.down()
    tx.write('EXPANSION',font=(10))

    tx.up();tx.goto(10.0,-305.0);tx.down()
    tx.write('EXHAUST',font=(10))

    tx.up();tx.goto(-29.0,-265.0);tx.down()
    tx.write('scavenging',font=(10))
    tx.up();tx.goto(-340.0,-125.0);tx.setheading(120);tx.down();tx.circle(-340,30)

'''



'''




event1=Label(s2,text="Event",font=("calibri",20,"underline bold italic"))
event1.grid(row=2,column=0,padx=20,pady=20)
Distance1=Label(s2,text="Distance from\ntheir respective\n dead centres in cm",font=("calibri",20,"underline bold italic"))
Distance1.grid(row=2,column=1,padx=10,pady=10)
Valve1=Label(s2,text="Port opening period in\ndegrees",font=("calibri",20,"underline bold italic"))
Valve1.grid(row=2,column=2,padx=10,pady=10)


ivo2s=Label(s2,text="Exhaust port opens",font=("calibri",15," bold italic"))
ivo2s.grid(row=3,column=0,padx=10,pady=10)
ivc2s=Label(s2,text="Exhaust port closes",font=("calibri",15," bold italic"))
ivc2s.grid(row=4,column=0,padx=10,pady=10)
evo2s=Label(s2,text="Transfer port opens",font=("calibri",15," bold italic"))
evo2s.grid(row=5,column=0,padx=10,pady=10)
evc2s=Label(s2,text="Transfer Port closes",font=("calibri",15," bold italic"))
evc2s.grid(row=6,column=0,padx=10,pady=10)


ivo1s=Entry(s2,textvariable=a2)
ivo1s.grid(row=3,column=1,padx=10,pady=10)
ivc2s=Entry(s2,textvariable=b2)
ivc2s.grid(row=4,column=1,padx=10,pady=10)
evo3s=Entry(s2,textvariable=c2)
evo3s.grid(row=5,column=1,padx=10,pady=10)
evc4s=Entry(s2,textvariable=d2)
evc4s.grid(row=6,column=1,padx=10,pady=10)


ivo_ps=Entry(s2,textvariable=a3,state=DISABLED)
ivo_ps.grid(row=3,column=2,padx=10,pady=10)
ivc_ps=Entry(s2,textvariable=b3,state=DISABLED)
ivc_ps.grid(row=4,column=2,padx=10,pady=10)
evo_ps=Entry(s2,textvariable=c3,state=DISABLED)

evo_ps.grid(row=5,column=2,padx=10,pady=10)
evc_ps=Entry(s2,textvariable=d3,state=DISABLED)
evc_ps.grid(row=6,column=2,padx=10,pady=10)

cis=Label(s2,text="Circumference",font=("calibri",15," bold italic"))
cis.grid(row=7,column=0,padx=10,pady=10)

cirmfs=Entry(s2,textvariable=cirm2)
cirmfs.grid(row=7,column=1,padx=10,pady=10)

buttons=Button(s2,text="calculate",command=lambda:degrees1(ivo1s.get(),ivc2s.get(),evo3s.get(),evc4s.get(),cirmfs.get()))
buttons.grid(row=7,column=2,padx=10,pady=10)
buttons2=Button(s2,text="Plot",command=lambda:circle(deg5,deg6,deg7,deg8))
buttons2.grid(row=7,column=3,padx=10,pady=10)
buttons2=Button(s2,text="Animate",command=anime2s)
buttons2.grid(row=8,column=3,padx=10,pady=10)


    
     

win.mainloop()
