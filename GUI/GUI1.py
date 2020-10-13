import sys
sys.path.append('D:\Github Projects\ProgrammingHomework')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from algorithms.Image_Contrast import Image_contrast

class Ui_Dialog(QtWidgets.QWidget):
    img1,img2='',''
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(642, 332)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(280, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 191, 161))
        self.label_2.setObjectName("graphicsView")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(400, 40, 191, 161))
        self.label_3.setObjectName("graphicsView_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 260, 241, 16))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 210, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 210, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2.clicked.connect(self.openimage1)
        self.pushButton_3.clicked.connect(self.openimage2)
        self.pushButton.clicked.connect(lambda:self.face(self.img1,self.img2))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        
    def openimage1(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.label_2.width(), self.label_2.height())
        self.label_2.setPixmap(jpg)
        self.img1 = imgName
        
        
    def openimage2(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.label_3.width(), self.label_3.height())
        self.label_3.setPixmap(jpg)
        self.img2 = imgName
    
    def face(self,img1,img2):
        self.label.setText(Image_contrast(img1,img2))


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "进行对比"))
        self.label.setText(_translate("Dialog", "请选择图片"))
        self.pushButton_2.setText(_translate("Dialog", "选取照片"))
        self.pushButton_3.setText(_translate("Dialog", "选取照片"))