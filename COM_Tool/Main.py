from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QColor
import sys
import Main_form

class Main_form_UI(QtWidgets.QMainWindow, QtWidgets.QWidget, Main_form.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main_form_UI, self).__init__(parent)
        self.setupUi(self)

def mywindow():
    mywindow = Main_form_UI()
    mywindow.show()
    return mywindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myobj = mywindow()
    sys.exit(app.exec_())
