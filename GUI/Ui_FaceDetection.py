# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Github Projects\ProgrammingHomework\GUI\FaceDetection.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
#此文件为人脸分析功能的UI

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys
sys.path.append('D:\Github Projects\ProgrammingHomework')
from algorithms.FaceDetection import FaceDetection

class Ui_Dialog(QtWidgets.QWidget):
    img=''
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(562, 332)
        Dialog.setMinimumSize(QtCore.QSize(562, 332))
        Dialog.setMaximumSize(QtCore.QSize(562, 332))
        Dialog.setStyleSheet("font: 9pt \"黑体\";")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 10, 151, 41))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 60, 501, 211))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 280, 141, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 280, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        #点击时的操作
        self.pushButton_2.clicked.connect(self.openimage)#选择文件
        self.pushButton.clicked.connect(lambda:self.face(self.img))#运行face
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def openimage(self):#开启一个选择文件的窗口
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.label_3.width(), self.label_3.height())
        self.label_3.setPixmap(jpg)#显示已选文件
        self.img = imgName
        
    def face(self,img):#获取从后端返回的信息并显示
        self.label_2.setText(FaceDetection(img))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">人脸分析</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">请选择照片并分析<br/></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "分析图片"))
        self.pushButton_2.setText(_translate("Dialog", "选择照片"))
