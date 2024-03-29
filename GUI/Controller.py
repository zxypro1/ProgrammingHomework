import sys
sys.path.append('D:\Github Projects\ProgrammingHomework')
import GUI.Ui_main as ui
import GUI.Ui_About as ui1
import GUI.Ui_FaceComparsion as ui2
import GUI.Ui_FaceContrast as ui3
import GUI.Ui_FaceDetection as ui4
import GUI.Ui_FaceSignUp as ui5
import GUI.Ui_Massage as ui6
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtGui import *
#Controller为所有页面的跳转函数集合
class Controller:
    def  __init__(self):
        pass
    
    def show_main(self):#显示main页面
        self.main=ui.Ui_MainWindow()
        self.mainWindow=QMainWindow()
        self.main.setupUi(self.mainWindow)
        self.main.pushButton.clicked.connect(self.show_FaceContrast)
        self.main.pushButton_2.clicked.connect(self.show_FaceDetection)
        self.main.pushButton_3.clicked.connect(self.show_FaceComparsion)
        self.main.pushButton_4.clicked.connect(self.show_FaceSignUp)
        self.main.action_3.triggered.connect(self.show_About)
        self.mainWindow.show()
        
        
    
    def show_About(self):#显示About页面
        self.about=ui1.Ui_Dialog()
        self.dialog=QDialog()
        self.about.setupUi(self.dialog)
        self.dialog.show()
        
        
    def show_FaceComparsion(self):#显示人脸检索功能页
        self.faceC=ui2.Ui_Dialog()
        self.dialog2=QDialog()
        self.faceC.setupUi(self.dialog2)
        self.dialog2.show()
    
    
    def show_FaceContrast(self):#显示人脸对比功能页
        self.faceCon=ui3.Ui_Dialog()
        self.dialog3=QDialog()
        self.faceCon.setupUi(self.dialog3)
        self.dialog3.show()
        
    
    def show_FaceDetection(self):#显示人脸分析功能页面
        self.faceD=ui4.Ui_Dialog()
        self.dialog4=QDialog()
        self.faceD.setupUi(self.dialog4)
        self.dialog4.show()
        
        
    def show_FaceSignUp(self):#显示人脸上传功能页
        self.faceS=ui5.Ui_Dialog()
        self.dialog5=QDialog()
        self.faceS.setupUi(self.dialog5)
        self.dialog5.show()
        
        
    def show_Massage(self):#显示人脸上传功能的消息栏
        self.mass=ui6.Ui_Dialog()
        self.dialog6=QDialog()
        self.mass.setupUi(self.dialog6)
        self.dialog6.show()