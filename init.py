import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon



class Scheduler(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setApplicationName("Doug's Application")

    def initUI(self):

        self.setGeometry(500, 500, 1000, 1000)
        self.setWindowTitle('Stanford Schedule')
        self.setWindowIcon(QIcon('cal_icon.png'))
        self.show()
        self.queryParams()

    def queryParams(self):
        qtr = QComboBox(self)
        # qtrEntries = QStringList(["Fall 2019", "Winter 2020", "Spring 2020"])
        qtr.addItems(["Fall 2019", "Winter 2020", "Spring 2020"])
        qtr.show()
        print(qtr.currentText())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = Scheduler()
    sys.exit(app.exec_()) #closes the window without throwing terminal error












# class Application(QMainWindow):
#     def __init__(self):
#         super(Application, self).__init__()
#         self.setWindowIcon(QtGui.QIcon('cal_icon.png'))

# def createGUI():
# 	app = QtWidgets.QApplication(sys.argv)
#     app.setStyle('Macintosh')
#     window = QtWidgets.QMainWindow()
#     button = QtWidgets.QPushButton("Hello, PyQt!")
#     window.setCentralWidget(button)
#     window.show()
#     app.exec_()


# def main():
# 	createGUI()

# if __name__ == '__main__':
#     main()
