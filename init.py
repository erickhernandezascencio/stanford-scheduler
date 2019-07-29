import sys
import requests
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QFont
from lxml import html
import json

#Global Constants

#1) gap between the label and its respective widget in pixels
WIDGET_LABEL_GAP = 35


#large to-do: organize so that the color scheme fits with stanford
class Scheduler(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(500, 500, 1200, 1200)
        self.setWindowTitle('Cardinal Scheduler')
        self.setWindowIcon(QIcon('cal_icon.png'))
        self.setUpCalendar()
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.red) #to-do: figure out how to change this color
        self.setPalette(p)
        #todo: add build calendar function


        self.queryParams()
        self.show()
    '''
    This function currently sets up the widgets that will collect the query parameters.
    As of now these parameters include:
    - Quarter - Class Name
    To-Do:
    Add Filtering for
    - Departments - WAYS Classes - Fitting Schedule
    - Unit Count Floor - more....
    '''
    def queryParams(self):
        global WIDGET_LABEL_GAP
        params = []
        #gathers quarter parameter
        qtr = QComboBox(self)
        qtrLabel = QLabel("Select your quarter:",self)
        qtrLabel.move(25,70)
        qtrLabel.show()
        qtr.addItems(["Fall 2019", "Winter 2020", "Spring 2020"])
        qtr.move(25,70 + WIDGET_LABEL_GAP)
        params.append(qtr)
        qtr.show()

        #gathers course name/number
        courseLabel = QLabel("Enter your course name, number:",self)
        courseLabel.move(25,150)
        course = QLineEdit(self)
        course.clearButtonEnabled = True
        course.move(25,150 + WIDGET_LABEL_GAP)
        courseLabel.show()
        params.append(course)
        course.show()
        print(qtr.currentText()) #example at how to access code

        #creates searchButton
        searchButton = QPushButton("Search!",self)
        searchButton.move(25,240)
        searchButton.show()
        searchButton.clicked.connect(lambda: self.onClick(qtr,course))
        #self.searchExploreCourses()

    def searchExploreCourses(self, query):
        # print("making request")
        # page = requests.get('http')
        # print(page.text)
        # tree = html.fromstring(page.text)
        # print (tree)
        searchResultsLabel = QLabel("Search Results:",self)
        searchResultsLabel.move(50,300)
        searchResultsLabel.show()
        #wait for API to come into play

    def setUpCalendar(self):
        calLabel = QLabel("Weekly Schedule",self)
        calLabel.move(620,30)
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(600, 100)
        cal.clicked[QDate].connect(self.showDate)

        # self.lbl = QLabel(self)
        # date = cal.selectedDate()
        # self.lbl.setText(date.toString())
        # self.lbl.move(350, 400)

    def showDate(self, date):
        self.lbl.setText(date.toString())

    @pyqtSlot()
    def onClick(self,qtr,course):
        query = [qtr.currentText(),course.text()]
        self.searchExploreCourses(query)




if __name__ == '__main__':

    app = QApplication(["Scheduler"])
    app.setApplicationName("Scheduler")
    app.setStyle('Fusion')
    app.setFont(QFont("Fira Mono", 20))
    ex = Scheduler()
    sys.exit(app.exec_()) #closes the window without throwing terminal error
