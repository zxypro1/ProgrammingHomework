import sys
sys.path.append('D:\Github Projects\ProgrammingHomework')
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
from GUI.Controller import Controller
#运行
if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller=Controller()
    controller.show_main()#打开Ui_main页面
    sys.exit(app.exec_())