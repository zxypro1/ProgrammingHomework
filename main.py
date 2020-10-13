import sys
sys.path.append('D:\Github Projects\ProgrammingHomework')
from PyQt5 import QtGui
from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt5.QtGui import *
from GUI.GUI1 import Ui_Dialog
from algorithms.Image_Contrast import Image_contrast
from PyQt5 import QtWidgets
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Dialog()    
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())