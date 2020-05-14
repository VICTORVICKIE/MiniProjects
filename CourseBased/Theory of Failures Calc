from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os, sys, subprocess
from math import sqrt
#FILEPATH = os.path.abspath(__file__)
#EXIT_CODE_REBOOT = -123

class Ui_MainWindow(object):
    
    EXIT_CODE_REBOOT = -123
    def Restart(self):
            QtWidgets.qApp.exit( Ui_MainWindow.EXIT_CODE_REBOOT )
            '''self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            #sys.exit()
            #self.window.hide()'''
    def nature(self,_1,_2,_3,n1,n2,n3,syp,r,method,c1,combo1,combo2):
        if n1 == "Tensile":
            _1 = _1
        elif n1 == "Compressive":
            _1 = -(_1)
        if n2 == "Tensile":
            _2 = _2
        elif n2 == "Compressive":
            _2 = -(_2)
        if n3 == "Tensile":
            _3 = _3
        elif n3 == "Compressive":
            _3 = -(_3)
        self.switch(_1,_2,_3,syp,r,method,c1,combo1,combo2)
    def switch(self,_1,_2,_3,syp,r,method,c1,combo1,combo2):    
        #print(_1,_2,_3,syp,r,method)
        if method == "Rankine or Max Principal Stress ":
            self.Rankine(_1,_2,_3,syp,r,c1,combo1,combo2)

        if method == "Guest & Tresca & columb or Max Shear Stress ":
            self.Guest(_1,_2,_3,syp,r,c1,combo1,combo2)

        if method == "St.Venant or Max Principal Strain ":
            self.Stvenants(_1,_2,_3,syp,r,c1,combo1,combo2)

        if method == "Beltrami,Haigh's or Max Total Energy ":
            self.Beltrami(_1,_2,_3,syp,r,c1,combo1,combo2)

        if method == "Von Miscs Hencky or Max Shear Strain Energy":
            self.Vonmiscs(_1,_2,_3,syp,r,c1,combo1,combo2)



    def Rankine(self,_1,_2,_3,syp,r,c1,combo1,combo2):
        if c1 == combo1:
            stress_list = [_1,_2,_3]
            sigma_w = max(stress_list)
            if abs(sigma_w) >= syp:
                #print(f" Rankine's Theory:\n     Material Fails as Maximum Principal Stress ({abs(sigma_w)}) is greater than or equal to Yield Point Stress ({syp})")
                _translate = QtCore.QCoreApplication.translate
                self.result2.setText(_translate("MainWindow",f" Rankine's Theory:\n     Material Fails as Maximum Principal Stress ({abs(sigma_w)})\n is greater than or equal to Yield Point Stress ({syp})"))
                
            else:
                self.fos1 = syp/sigma_w
                #print("FOS:",fos1)
                
                _translate = QtCore.QCoreApplication.translate
                self.result.setText(_translate("MainWindow", f"  σyp > σw (i.e) ({syp}>{sigma_w})\n FOS:{round(self.fos1,2)}"))
        if c1 == combo2:
            first = (_1 + _2)/2
            second = ((_1 - _2)/2)**2
            third = (_3)**2
            s1 = (first) + sqrt(second + third)
            s2 = (first) - sqrt(second + third)
            stress_list = [s1, s2]
            #print(stress_list)
            sigma_w = max(stress_list)
            if abs(sigma_w) >= syp:
                _translate = QtCore.QCoreApplication.translate
                self.result2.setText(_translate("MainWindow",f" Rankine's Theory:\n     Material Fails as Maximum Principal Stress ({abs(sigma_w)})\n is greater than or equal to Yield Point Stress ({syp})"))
                #print(f" Rankine's Theory:\n     Material Fails as Maximum Principal Stress ({abs(sigma_w)}) is greater than or equal to Yield Point Stress ({syp})")
            else:
                self.fos1 = syp/sigma_w
                #print("FOS:",fos1)
                _translate = QtCore.QCoreApplication.translate
                self.result.setText(_translate("MainWindow", f"  σyp > σw (i.e) ({syp}>{sigma_w})\n FOS:{round(self.fos1,2)}"))
            
    def Guest(self,_1,_2,_3,syp,r,c1,combo1,combo2):
        if c1 == combo1:
            s1 = abs(_1-_2)
            s2 = abs(_2 -_3)
            s3 = abs(_3-_1)
            #print(_3,s1,s2,s3)
            stress_list = [s1,s2,s3]
            sigma_w = max(stress_list)
            if abs(sigma_w) >= syp:
                #print(f" Guest & Tresca's Theory:\n     Material Fails as Maximum Shear Stress ({abs(sigma_w)}) is greater than or equal to Yield Point Shear Stress ({syp})")
                _translate = QtCore.QCoreApplication.translate
                self.result2.setText(_translate("MainWindow",f" Guest & Tresca's Theory:\n     Material Fails as Maximum Shear Stress ({abs(sigma_w)})\n is greater than or equal to Yield Point Shear Stress ({syp})"))

            else:
                self.fos2 = syp/sigma_w
                #print("FOS:",fos2)
                _translate = QtCore.QCoreApplication.translate
                self.result.setText(_translate("MainWindow", f"  σyp > σw (i.e) ({syp}>{sigma_w})\n FOS:{round(self.fos2,2)}"))
        if c1 == combo2:
            first = (_1 + _2)/2
            second = ((_1 - _2)/2)**2
            third = (_3)**2
            s1 = (first) + sqrt(second + third)
            s2 = (first) - sqrt(second + third)
            stress_list = [abs(s1-s2)]
            #print(stress_list)
            sigma_w = max(stress_list)
            if abs(sigma_w) >= syp:
                #print(f" Guest & Tresca's Theory:\n     Material Fails as Maximum Shear Stress ({abs(sigma_w)}) is greater than or equal to Yield Point Stress ({syp})")
                _translate = QtCore.QCoreApplication.translate
                self.result2.setText(_translate("MainWindow",f" Guest & Tresca's Theory:\n     Material Fails as Maximum Shear Stress ({abs(sigma_w)})\n is greater than or equal to Yield Point Shear Stress ({syp})"))

            else:
                self.fos2 = syp/sigma_w
                #print("FOS:",fos2)
                _translate = QtCore.QCoreApplication.translate
                self.result.setText(_translate("MainWindow", f"  σyp > σw (i.e) ({syp}>{sigma_w})\n FOS:{round(self.fos2,2)}"))
    def Stvenants(self,_1,_2,_3,syp,r,c1,combo1,combo2):
        if c1 == combo1:
            s1 = abs(_1 - (r*(_2+_3)))
            s2 = abs(_2 - (r*(_1+_3)))
            s3 = abs(_3 - (r*(_2+_1)))
            #print(_3,s1,s2,s3)
            stress_list = [s1,s2,s3]
            sigma_w = max(stress_list)
            if abs(sigma_w) >= syp:
                #print(f" St.Venant's Theory:\n     Material Fails as Maximum Principal Strain ({abs(sigma_w)}) is greater than or equal to Yield Point Strain ({syp})")
                _translate = QtCore.QCoreApplication.translate
                self.result2.setText(_translate("MainWindow",f" St.Venant's Theory:\n     Material Fails as Maximum Principal Strain ({abs(sigma_w)})\n is greater than or equal to Yield Point Strain ({syp})"))

            else:
                self.fos3 = syp/sigma_w
                #print("FOS:",fos3)
                _translate = QtCore.QCoreApplication.translate
                self.result.setText(_translate("MainWindow", f"  σyp > σw (i.e) ({syp}>{sigma_w})\n FOS:{round(self.fos3,2)}"))
        
        if c1 == combo2:
            first = (_1 + _2)/2
            second = ((_1 - _2)/2)**2
            third = (_3)**2
            s1 = (first) + sqrt(second + third)
            s2 = (first) - sqrt(second + third)
            stress_list = [abs(s1-(r*s2)),abs(s2-(r*s1))]
            #print(stress_list)
            sigma_w = max(stress_list)
            if abs(sigma_w) >= syp:
                #print(f" St.Venant's Theory:\n     Material Fails as Maximum Principal Strain ({abs(sigma_w)}) is greater than or equal to Yield Point strain ({syp})")
                _translate = QtCore.QCoreApplication.translate
                self.result2.setText(_translate("MainWindow",f" St.Venant's Theory:\n     Material Fails as Maximum Principal Strain ({abs(sigma_w)})\n is greater than or equal to Yield Point Strain ({syp})"))


            else:
                self.fos3 = syp/sigma_w
                #print("FOS:",fos3)
                _translate = QtCore.QCoreApplication.translate
                self.result.setText(_translate("MainWindow", f"  σyp > σw (i.e) ({syp}>{sigma_w})\n FOS:{round(self.fos3,2)}"))
        
    def Beltrami(self,_1,_2,_3,syp,r,c1,combo1,combo2):
        if c1 == combo1:
            sigma_w = _1**2 + _2**2 + _3**2 - (2*r)*(_1*_2 + _2*_3 + _3*_1)
            #print(sigma_w)
            if abs(sigma_w) >= syp**2:
                #print(f" Beltrami's Theory:\n     Material Fails as Energy limit Volume({abs(sigma_w)}) is greater than or equal to Energy absorbed ({syp**2})")
                _translate = QtCore.QCoreApplication.translate
                self.result2.setText(_translate("MainWindow",f" Beltrami's Theory:\n     Material Fails as Energy limit Volume({abs(sigma_w)})\n is greater than or equal to Energy absorbed ({syp**2})"))

            else:
                self.fos4 = sqrt((syp**2)/sigma_w)
                #print("FOS:",fos4)
                _translate = QtCore.QCoreApplication.translate
                self.result.setText(_translate("MainWindow", f"  σyp² > σw (i.e) ({syp**2}>{sigma_w})\n FOS:{round(self.fos4,2)}"))
        if c1 == combo2:
            first = (_1 + _2)/2
            second = ((_1 - _2)/2)**2
            third = (_3)**2
            s1 = (first) + sqrt(second + third)
            s2 = (first) - sqrt(second + third)
            sigma_w = s1**2 + s2**2  - (2*r)*(s1*s2)
            if abs(sigma_w) >= syp**2:
                #print(f" Beltrami's Theory:\n     Material Fails as Maximum Principal Strain ({abs(sigma_w)}) is greater than or equal to Energy absored({syp**2})")
                _translate = QtCore.QCoreApplication.translate
                self.result2.setText(_translate("MainWindow",f" Beltrami's Theory:\n     Material Fails as Energy limit Volume({abs(sigma_w)})\n is greater than or equal to Energy absorbed ({syp**2})"))
            else:
                self.fos4 = sqrt(syp**2/sigma_w)
                #print("FOS:",fos4)
                _translate = QtCore.QCoreApplication.translate
                self.result.setText(_translate("MainWindow", f"  σyp² > σw (i.e) ({syp**2}>{sigma_w})\n FOS:{round(self.fos4,2)}"))
        
    def Vonmiscs(self,_1,_2,_3,syp,r,c1,combo1,combo2):
        if c1 == combo1:
            sigma_w = (_1 - _2)**2 + (_2 - _3)**2 + (_3 - _1)**2
            #print(sigma_w)
            if abs(sigma_w) >= 2*(syp**2):
                #print(f" Von Miscs's Theory:\n     Material Fails as Energy limit Volume({abs(sigma_w)}) is greater than or equal to Energy absorbed ({syp**2})")
                _translate = QtCore.QCoreApplication.translate
                self.result2.setText(_translate("MainWindow",f" Von Miscs's Theory:\n     Material Fails as Energy limit Volume({abs(sigma_w)})\n is greater than or equal to Energy absorbed ({syp**2})"))
            else:
                self.fos5 = sqrt((2*(syp**2))/sigma_w)
                #print("FOS:",fos5)
                _translate = QtCore.QCoreApplication.translate
                self.result.setText(_translate("MainWindow", f"  2*σyp² > σw (i.e) ({2*syp**2}>{sigma_w})\n FOS:{round(self.fos5,2)}"))
        if c1 == combo2:
            first = (_1 + _2)/2
            second = ((_1 - _2)/2)**2
            third = (_3)**2
            s1 = (first) + sqrt(second + third)
            s2 = (first) - sqrt(second + third)
            sigma_w = (_1 - _2)**2
            if abs(sigma_w) >= 2*(syp**2):
                #print(f" Beltrami's Theory:\n     Material Fails as Maximum Principal Strain ({abs(sigma_w)}) is greater than or equal to Energy absored({syp**2})")
                _translate = QtCore.QCoreApplication.translate
                self.result2.setText(_translate("MainWindow",f" Von Miscs's Theory:\n     Material Fails as Energy limit Volume({abs(sigma_w)})\n is greater than or equal to Energy absorbed ({syp**2})"))
            else:
                self.fos5 = sqrt(2*(syp**2)/sigma_w)
                #print("FOS:",fos5)
                _translate = QtCore.QCoreApplication.translate
                self.result.setText(_translate("MainWindow", f"    2*σyp² > σw (i.e) ({2*syp**2}>{sigma_w})\n FOS:{round(self.fos5,2)}"))
    
    def inputvals(self):
        _1 = self.lineEdit.text()
        _2 = self.lineEdit_2.text()
        _3 = self.lineEdit_3.text()
        syp = self.lineEdit_4.text()
        r = self.lineEdit_5.text()
        try:
            _1 = float(_1)
            _2 = float(_2)
            _3 = float(_3)
            syp = float(syp)
            r = float(r)
            n1 = self.comboBox_6.currentText()
            n2 = self.comboBox_4.currentText()
            n3 = self.comboBox_5.currentText()
            method = self.comboBox_7.currentText()
            t1 = str(self.comboBox.currentText())
            t2 = str(self.comboBox_2.currentText())
            t3 = str(self.comboBox_3.currentText())
            combo1 = ["Principal Stress 1:","Principal Stress 2:","Principal Stress 3:"]
            combo2 = ["Stress in X:","Stress in Y:","Shear Stress"]
            
            c1 = [t1,t2,t3]
            if ((c1 == combo1) or (c1 == combo2)):
                self.nature(_1,_2,_3,n1,n2,n3,syp,r,method,c1,combo1,combo2)
            else:
                msg = QMessageBox()
                msg.setWindowTitle("StressError")
                msg.setText("!!Your selection is incorrect!!")
                msg.setIcon(QMessageBox.Critical)
                msg.buttonClicked.connect(self.Restart)
                x = msg.exec_()
            #print(n1)
            #print(_1,_2,_3,syp,r)
            
                
        except ValueError:
            msg = QMessageBox()
            msg.setWindowTitle("ValueError")
            msg.setText("!!Your input is incorrect!!")
            msg.setIcon(QMessageBox.Critical)
            msg.buttonClicked.connect(self.Restart)
            x = msg.exec_()
            
        
            
        

    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 680)
        MainWindow.setMaximumSize(QtCore.QSize(480, 680))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(80, 550, 400, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.result.setFont(font)
        self.result.setObjectName("result")

        self.link = QtWidgets.QLabel(self.centralwidget)
        self.link.setGeometry(QtCore.QRect(290,50,175,25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.link.setFont(font)
        self.link.setObjectName("link")
        

        self.result2 = QtWidgets.QLabel(self.centralwidget)
        self.result2.setGeometry(QtCore.QRect(80, 550, 400, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.result2.setFont(font)
        self.result2.setObjectName("result2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 160, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 120, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBox_7 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_7.setGeometry(QtCore.QRect(150, 410, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_7.setFont(font)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 120, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 410, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(370, 350, 61, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(350, 280, 111, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 220, 131, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 350, 61, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 220, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 480, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.inputvals)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 20, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 160, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 280, 131, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 280, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 530, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(350, 220, 111, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 350, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(26, 70, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(260, 350, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_6.setGeometry(QtCore.QRect(350, 160, 111, 22))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Theory of Failure"))
        self.label_3.setText(_translate("MainWindow", "Stress Type"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Principal Stress 1:"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Stress in X:"))
        self.label_5.setText(_translate("MainWindow", "Nature"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "Rankine or Max Principal Stress "))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "Guest & Tresca & columb or Max Shear Stress "))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "St.Venant or Max Principal Strain "))
        self.comboBox_7.setItemText(3, _translate("MainWindow", "Beltrami,Haigh's or Max Total Energy "))
        self.comboBox_7.setItemText(4, _translate("MainWindow", "Von Miscs Hencky or Max Shear Strain Energy"))
        self.label_4.setText(_translate("MainWindow", "Values"))
        self.label_6.setText(_translate("MainWindow", "Method (or) Theory:"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Tensile"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Compressive"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Principal Stress 2:"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Stress in Y:"))
        self.pushButton.setText(_translate("MainWindow", "TEST"))
        self.label.setText(_translate("MainWindow", "Theory of Failure"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Principal Stress 3:"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Shear Stress"))
        self.label_10.setText(_translate("MainWindow", "Output:"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Tensile"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Compressive"))
        self.label_8.setText(_translate("MainWindow", "Yield Point Stress:"))
        self.label_2.setText(_translate("MainWindow", "Input:"))
        self.label_9.setText(_translate("MainWindow", "Poison\'s Ratio:"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Tensile"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Compressive"))
        self.link.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://github.com/VICTORVICKIE/Virtual-lab\"><span style=\" text-decoration: underline; color:#0000ff;\">-VIGNESH KUMAR S</span></a></p></body></html>"))
        self.link.setOpenExternalLinks(True)



#app = QtWidgets.QApplication(sys.argv)
#MainWindow = QtWidgets.QMainWindow()
#ui = Ui_MainWindow()
#ui.setupUi(MainWindow)
#MainWindow.show()
#a = Ui_MainWindow()
#a.Restart()
#sys.exit(app.exec_())










if __name__ =="__main__":
    currentExitCode = Ui_MainWindow.EXIT_CODE_REBOOT
    while currentExitCode == Ui_MainWindow.EXIT_CODE_REBOOT:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        currentExitCode = app.exec_()
        app = None  # delete the QApplication object
