from PyQt5 import QtCore, QtGui, QtWidgets
from turtle import *
from math import *


class Ui_mainWindow(object):


    def circle(self):
        t = float(self.t_obj.text())
        s1 = float(self.s1_obj.text())
        s2 = float(self.s2_obj.text())
        o = float(self.o_obj.text())
        s1_choice = self.comboBox.currentText()
        s2_choice = self.comboBox_2.currentText()
        o_choice = self.comboBox_3.currentText()
        if s1_choice == "Tensile force":
            s1 = s1
        elif s1_choice == "Compressive force":
            s1 = -s1

        if s2_choice == "Tensile force":
            s2 = s2
        elif s2_choice == "Compressive force":
            s2 = -s2
        s3 = (s1 + s2) / 2
        ang = degrees(atan((t) / (s1 - s3)))
        if o_choice == 'of plane':
            o = o
        elif o_choice == 'From Principal Plane':
            h = (2 * o) - ang
            o = h / 2
        div = 1
        o1 = 2 * o
        s3 = (s1 + s2) / 2

        R = ((((s1 - s2) / 2) ** 2) + t ** 2) ** 0.5  # real values
        val = R
        m = (s1 + s2) / 2
        ang = degrees(atan((t) / (s1 - s3)))
        '''if ang<0:
            o1=-o1'''

        if (t ** 2) ** 0.5 > (s1 ** 2) ** 0.5 and (t ** 2) ** 0.5 > (s2 ** 2) ** 0.5:

            while (t ** 2) ** 0.5 > 10:
                div = div * 10
                t = t / 10
                s1 = s1 / 10
                s2 = s2 / 10
        elif (s1 ** 2) ** 0.5 > (t ** 2) ** 0.5 and (s1 ** 2) ** 0.5 > (s2 ** 2) ** 0.5:
            while (s1 ** 2) ** 0.5 > 10:
                div = div * 10
                t = t / 10
                s1 = s1 / 10
                s2 = s2 / 10
        else:
            while (s2 ** 2) ** 0.5 > 10:
                div = div * 10
                t = t / 10
                s1 = s1 / 10
                s2 = s2 / 10

        # scale values
        t = t * 50
        s1 = s1 * 50
        s2 = s2 * 50

        R1 = (((((s1 - s2) / 2) ** 2) + t ** 2) ** 0.5)
        g = R1
        s3 = (s1 + s2) / 2

        a = Screen();
        a.title("Mohr's Circle")
        a.screensize(2000, 2000)

        r1 = Turtle();
        r1.color('red');
        r1.speed('fastest')
        r2 = Turtle();
        r2.color('red');
        r2.speed('fastest')
        r3 = Turtle();
        r3.color('blue');
        r3.speed('fastest')
        r4 = Turtle();
        r4.color('blue');
        r4.speed('fastest')
        r5 = Turtle();
        r5.color('blue');
        r5.speed('fastest')
        r6 = Turtle();
        r6.color('green');
        r6.speed('fastest')
        r7 = Turtle();
        r7.color('green');
        r7.speed('fastest')
        r8 = Turtle();
        r8.color('black');
        r8.speed('fastest')
        r9 = Turtle();
        r9.color('black');
        r9.speed('fastest')
        r10 = Turtle();
        r10.color('orange');
        r10.speed('fastest')

        r1.left(90)
        r1.fd(-g - 100);
        r1.fd(2 * (g + 100));
        r1.write('SHEAR STRESS', font=('arial', 16, 'bold'))  # axis
        r2.fd(-((s3 ** 2) ** 0.5) - g - 100);
        r2.fd(2 * (((s3 ** 2) ** 0.5) + g + 100))
        r2.write('NORMAL STRESS', font=('arial', 16, 'bold'))

        r3.penup();
        r3.goto(s1, t);
        r3.pendown();
        r3.goto(s2, -t)
        # r3.write('('+str(s1)+','+str(t)+')' ,font=('arial',16,'bold'))

        r4.penup();
        r4.goto(s2, -t);
        r4.pendown();
        r4.goto(s1, t)
        # r4.write('('+str(s2)+','+str(-t)+')' ,font=('arial',16,'bold'))

        r5.penup();
        r5.goto(s3, 0);
        r5.left(90);
        r5.fd(g);
        r5.right(90);
        r5.pendown();
        r5.circle(-g)
        r5.penup();
        r5.goto(s3, 0)
        r5.color('yellow');
        r5.left(90);
        r5.fd(g);
        r5.pendown();
        r5.fd(30)
        r5.write(str(round(val, 2)), font=('arial', 10, 'bold'))

        r6.penup();
        r6.goto(s3 + g, 0);
        r6.pendown()
        r6.write(str(round(m + val, 2)), font=('arial', 10, 'bold'))
        r7.penup();
        r7.goto(s3 - g, 0);
        r7.pendown()
        r7.write(str(round(m - val, 2)), font=('arial', 10, 'bold'))

        r8.penup();
        r8.goto(s3, 0);
        r8.pendown();
        r8.left(ang);
        r8.left(o1);
        r8.fd(g)

        p = list((r8.position()))
        sa = p[0];
        ta = p[1]
        c1 = sa;
        c2 = ta
        sa = (sa / 50) * div;
        ta = (ta / 50) * div
        res = (sa ** 2 + ta ** 2) ** 0.5

        r8.write('(' + str(round(sa, 2)) + ',' + str(round(ta, 2)) + ')', font=('arial', 9, 'bold'))

        '''r8.backward(2*g)

        p1=list((r8.position()))
        sa1=p1[0];ta1=p1[1]
        c3=sa1;c4=ta1
        sa1=(sa1/50)*div;ta1=(ta1/50)*div
        res1=(sa1**2 + ta1**2)**0.5

        r8.write('('+str(round(sa1,2))+','+str(round(ta1,2))+')',font=('arial',9,'bold'))'''

        r8.ht()

        r9.penup();
        r9.goto(s3, 0);
        r9.left(ang);
        r9.left(o1);
        r9.fd(30);
        r9.right(90);
        r9.pendown();
        r9.circle(-30, (o1 ** 2) ** 0.5)
        r9.write(str(round(o1, 3)) + 'degs', font=('arial', 9, 'bold'));
        r9.ht()

        r10.ht();
        r10.goto(c1 / 2, c2 / 2);
        r10.write(str(round(res, 2)), font=('arial', 9, 'bold'))
        r10.goto(c1, c2);
        r10.goto(0, 0)

        '''r10.goto(c3/2,c4/2);r10.write(str(round(res1,2)),font=('arial',9,'bold'))
        r10.goto(c3,c4)'''

        mainloop()


    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        mainWindow.setMinimumSize(QtCore.QSize(800, 600))
        mainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 801, 581))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(230, 10, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.scrollArea = QtWidgets.QScrollArea(self.page)
        self.scrollArea.setGeometry(QtCore.QRect(0, 70, 801, 591))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 799, 589))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(10, 40, 781, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setGeometry(QtCore.QRect(350, 10, 111, 21))
        self.label_17.setObjectName("label_17")
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setGeometry(QtCore.QRect(20, 120, 741, 431))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 20, 75, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.page)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 20, 141, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(240, 20, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.s2_obj = QtWidgets.QLineEdit(self.page_2)
        self.s2_obj.setGeometry(QtCore.QRect(380, 220, 113, 20))
        self.s2_obj.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.s2_obj.setObjectName("s2_obj")
        self.t_obj = QtWidgets.QLineEdit(self.page_2)
        self.t_obj.setGeometry(QtCore.QRect(380, 290, 113, 20))
        self.t_obj.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.t_obj.setObjectName("t_obj")
        self.o_obj = QtWidgets.QLineEdit(self.page_2)
        self.o_obj.setGeometry(QtCore.QRect(610, 370, 113, 20))
        self.o_obj.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.o_obj.setObjectName("o_obj")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(80, 180, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.page_2)
        self.comboBox_2.setGeometry(QtCore.QRect(540, 220, 111, 22))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.page_2)
        self.comboBox_3.setGeometry(QtCore.QRect(450, 370, 111, 22))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.page_2)
        self.pushButton.setGeometry(QtCore.QRect(310, 440, 181, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.circle)
        self.s1_obj = QtWidgets.QLineEdit(self.page_2)
        self.s1_obj.setGeometry(QtCore.QRect(380, 160, 113, 20))
        self.s1_obj.setObjectName("s1_obj")
        self.comboBox = QtWidgets.QComboBox(self.page_2)
        self.comboBox.setGeometry(QtCore.QRect(540, 160, 111, 22))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(160, 280, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(240, 370, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_13 = QtWidgets.QLabel(self.page_2)
        self.label_13.setGeometry(QtCore.QRect(380, 100, 101, 31))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page_2)
        self.label_14.setGeometry(QtCore.QRect(540, 100, 101, 31))
        self.label_14.setObjectName("label_14")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_4.setGeometry(QtCore.QRect(700, 20, 75, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 20, 101, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_18 = QtWidgets.QLabel(self.page_2)
        self.label_18.setGeometry(QtCore.QRect(20, 370, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(340, 140, 31, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_8 = QtWidgets.QLabel(self.page_3)
        self.label_8.setGeometry(QtCore.QRect(110, 110, 251, 51))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_3)
        self.label_9.setGeometry(QtCore.QRect(350, 180, 201, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setGeometry(QtCore.QRect(360, 270, 191, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.page_3)
        self.label_11.setGeometry(QtCore.QRect(130, 230, 221, 31))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page_3)
        self.label_12.setGeometry(QtCore.QRect(340, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_15 = QtWidgets.QLabel(self.page_3)
        self.label_15.setGeometry(QtCore.QRect(360, 400, 211, 61))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.page_3)
        self.label_16.setGeometry(QtCore.QRect(160, 420, 161, 21))
        self.label_16.setObjectName("label_16")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_6.setGeometry(QtCore.QRect(670, 30, 111, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 30, 121, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_6.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.stackedWidget.addWidget(self.page_3)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Mohr\'s Circle"))
        self.label_2.setText(_translate("mainWindow", "How to Draw a Mohr\'s Circle"))
        self.label.setText(_translate("mainWindow", "Mohr\'s Circle is a graphical method to determine the stresses developed inside any material \n"
"when it is subjected to external forces.For this article, assume that the material is subjected to external forces \n"
"in two mutually perpendicular directions,and a shear stress along one of its planes."))
        self.label_17.setText(_translate("mainWindow", "OverView"))
        self.label_19.setText(_translate("mainWindow", "USER INSTRUCTIONS:\n"
"\n"
"1) Read the drop box carefully and enter the required values.\n"
"2) The value of shear stress should be given as positive value.\n"
"3) Tensile stress is considered as positive and\n"
"    Compressive stress is considered as negative.\n"
"4) The plane at which the shear and normal stress has to be found can be determined,\n"
"     by entering the angle of the plane measured from(normal plane/principal plane)                                           \n"
"                                                                      \n"
"*NOTE:select the plane carefully and enter the angle*\n"
"\n"
"5 )COLOR INDICATIONS:\n"
"    green - principal majar & minor stresses\n"
"    yellow - maximum shear stress\n"
"    blue pointers - entered coordinates\n"
"    black -  required normal and shear stress coordinate\n"
"    yellow  -  resultant of required coordinate\n"
""))
        self.pushButton_2.setText(_translate("mainWindow", "About"))
        self.pushButton_3.setText(_translate("mainWindow", "Experiment"))
        self.label_3.setText(_translate("mainWindow", "How to Draw a Mohr\'s Circle"))
        self.label_4.setText(_translate("mainWindow", "Two Perpendicular stresses"))
        self.comboBox_2.setItemText(0, _translate("mainWindow", "Tensile force"))
        self.comboBox_2.setItemText(1, _translate("mainWindow", "Compressive force"))
        self.comboBox_3.setItemText(0, _translate("mainWindow", "of plane"))
        self.comboBox_3.setItemText(1, _translate("mainWindow", "From Princpal Plane"))
        self.pushButton.setText(_translate("mainWindow", "DRAW"))
        self.comboBox.setItemText(0, _translate("mainWindow", "Tensile force"))
        self.comboBox.setItemText(1, _translate("mainWindow", "Compressive force"))
        self.label_6.setText(_translate("mainWindow", "    simple shear  :"))
        self.label_7.setText(_translate("mainWindow", "Angle of inclination"))
        self.label_13.setText(_translate("mainWindow", "Magnitude"))
        self.label_14.setText(_translate("mainWindow", "Direction"))
        self.pushButton_4.setText(_translate("mainWindow", "About"))
        self.pushButton_5.setText(_translate("mainWindow", "OverView"))
        self.label_18.setText(_translate("mainWindow", "TYPE OF PROBLEM ==>"))
        self.label_5.setText(_translate("mainWindow", "{"))
        self.label_8.setText(_translate("mainWindow", "Backend Developed by:"))
        self.label_9.setText(_translate("mainWindow", "Santhosh Raajaa . S .S"))
        self.label_10.setText(_translate("mainWindow", "Vignesh Kumar . S"))
        self.label_11.setText(_translate("mainWindow", "GUI Developed by :"))
        self.label_12.setText(_translate("mainWindow", "Developers"))
        self.label_15.setText(_translate("mainWindow", "<html><head/><body><p><a href=\"https://github.com/VICTORVICKIE/Virtual-lab\"><span style=\" text-decoration: underline; color:#0000ff;\">My GitHub Repository</span></a></p></body></html>"))
        self.label_15.setOpenExternalLinks(True)
        self.label_16.setText(_translate("mainWindow", "Click here ====>"))
        self.pushButton_6.setText(_translate("mainWindow", "OverView"))
        self.pushButton_7.setText(_translate("mainWindow", "Experiment"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
