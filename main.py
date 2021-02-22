import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5 import QtGui
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowIcon(QtGui.QIcon('img/browser.jpg'))
        self.setWindowTitle('My-Browser')
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #Navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        #Adding back button
        back_btn = QAction(QtGui.QIcon('img/backward.png'),'Back',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        #Adding forward button
        forward_btn = QAction(QtGui.QIcon('img/forward.png'),'Forward',self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
        #Reload Button
        reload_btn = QAction(QtGui.QIcon('img/reload.png'),'Reload',self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)
        #Home Button
        home_btn = QAction(QtGui.QIcon('img/homeicon.jpg'),'Home',self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        #adding url bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        #capturing url
        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('MyBrowser')
window = MainWindow()
app.exec_()