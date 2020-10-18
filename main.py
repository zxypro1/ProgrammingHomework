import sys
sys.path.append('D:\Github Projects\ProgrammingHomework')
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
from GUI.Controller import Controller
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller=Controller()
    controller.show_main()
    sys.exit(app.exec_())