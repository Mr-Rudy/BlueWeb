import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
import qdarkstyle


class Window(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("BlueWeb")
        self.setWindowIcon(QIcon("icons/BlueWeb.png"))
        self.setGeometry(200,200, 900,600)

        app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())

        toolbar = QToolBar()
        self.addToolBar(toolbar)

#Back
        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon('icons/back.png'))
        self.backButton.setIconSize(QSize(36,36))
        self.backButton.clicked.connect(self.backBtn)
        toolbar.addWidget(self.backButton)


 #Foward
        
        self.fowardButton = QPushButton()
        self.fowardButton.setIcon(QIcon('icons/foward.png'))
        self.fowardButton.setIconSize(QSize(36,36))
        toolbar.addWidget(self.fowardButton)
        self.fowardButton.clicked.connect(self.fowardBtn)

 #Refresh
        
        self.refreshButton = QPushButton()
        self.refreshButton.setIcon(QIcon('icons/refresh.png'))
        self.refreshButton.setIconSize(QSize(36,36))
        self.refreshButton.clicked.connect(self.reloadBtn)
        toolbar.addWidget(self.refreshButton)

 #Arcade
        
        self.arcadeButton = QPushButton()
        self.arcadeButton.setIcon(QIcon('icons/arcade.png'))
        self.arcadeButton.setIconSize(QSize(36,36))
        self.arcadeButton.clicked.connect(self.arcadeBtn)
        toolbar.addWidget(self.arcadeButton)

 #Arcade Carter
        
        self.carcadeButton = QPushButton()
        self.carcadeButton.setIcon(QIcon('icons/arcadeCarter.png'))
        self.carcadeButton.setIconSize(QSize(36,36))
        self.carcadeButton.clicked.connect(self.carcadeBtn)
        toolbar.addWidget(self.carcadeButton)


 #Home
        
        self.homeButton = QPushButton()
        self.homeButton.setIcon(QIcon('icons/home.png'))
        self.homeButton.setIconSize(QSize(36,36))
        self.homeButton.clicked.connect(self.homeBtn)
        toolbar.addWidget(self.homeButton)


#Address Line Edit

        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.setFont(QFont("Sansserif", 13))
        self.addressLineEdit.returnPressed.connect(self.searchBtn)
        toolbar.addWidget(self.addressLineEdit)

#Search Button
        self.searchButton = QPushButton()
        self.searchButton.setIcon(QIcon('icons/search.png'))
        self.searchButton.setIconSize(QSize(36,36))
        self.searchButton.clicked.connect(self.searchBtn)
        toolbar.addWidget(self.searchButton)
        
# Web Engine
        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        initialUrl = 'https://www.bing.com/'
        self.addressLineEdit.setText(initialUrl)
        self.webEngineView.load(QUrl(initialUrl))

#Surfing the web

    def searchBtn(self):
        myurl = self.addressLineEdit.text()
        self.webEngineView.load(QUrl(myurl))
    def backBtn(self):
        self.webEngineView.back()
    def fowardBtn(self):
        self.webEngineView.foward()
    def reloadBtn(self):
        self.webEngineView.reload()
    def homeBtn(self):
        self.webEngineView.load(QUrl('https://www.bing.com/'))
        self.addressLineEdit.setText('https://www.bing.com/')
    def arcadeBtn(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error 1")
        msg.setText("The arcade website is not made by me it is made by the creators of poki.com")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ignore)
        msg.setDetailedText("Be safe on poki.com i have no idea if it will ever get hacked or something")
        showArcadeError = msg.exec_()
        self.webEngineView.load(QUrl('https://www.poki.com/'))
        self.addressLineEdit.setText('https://www.poki.com/')
    def carcadeBtn(self):
        self.webEngineView.load(QUrl('https://carters3421.itch.io'))
        self.addressLineEdit.setText('https://carters3421/itch.io')


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
