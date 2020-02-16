import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QThread
import webbrowser
from arbd import arbd1
from ArLib import ArLib

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(797, 610)
        MainWindow.setStyleSheet("back{\n"
"rgb(255, 255, 255)\n"
"}")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #POTENTIOMETER
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(40, 0, 141, 121))
        self.dial.setObjectName("dial")
        #self.dial.setValue(self.board.potentiometer())
        self.startThread()


        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(70, 120, 71, 31))
        self.lcdNumber.setObjectName("lcdNumber")
        self.rSlider = QtWidgets.QSlider(self.centralwidget)
        self.rSlider.setGeometry(QtCore.QRect(50, 260, 22, 160))
        self.rSlider.setOrientation(QtCore.Qt.Vertical)
        self.rSlider.setObjectName("rSlider")
        self.rSlider.valueChanged.connect(self.valueChangeR)
        self.gSlider = QtWidgets.QSlider(self.centralwidget)
        self.gSlider.setGeometry(QtCore.QRect(100, 260, 22, 160))
        self.gSlider.setOrientation(QtCore.Qt.Vertical)
        self.gSlider.setObjectName("gSlider")
        self.gSlider.valueChanged.connect(self.valueChangeG)
        self.bSlider = QtWidgets.QSlider(self.centralwidget)
        self.bSlider.setGeometry(QtCore.QRect(150, 260, 22, 160))
        self.bSlider.setOrientation(QtCore.Qt.Vertical)
        self.bSlider.setObjectName("bSlider")
        self.bSlider.valueChanged.connect(self.valueChangeB)
        self.pushButtonBuzzer = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBuzzer.setEnabled(True)
        self.pushButtonBuzzer.setGeometry(QtCore.QRect(550, 210, 71, 61))
        self.pushButtonBuzzer.setCheckable(True)
        self.pushButtonBuzzer.clicked.connect(self.btnstate)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(136, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(136, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(136, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(136, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(136, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(136, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(136, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(136, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(136, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.pushButtonBuzzer.setPalette(palette)
        self.pushButtonBuzzer.setAutoFillBackground(False)
        self.pushButtonBuzzer.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        radius: 3.0, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButtonBuzzer.setObjectName("pushButtonBuzzer")
        self.tempLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.tempLCD.setGeometry(QtCore.QRect(480, 110, 111, 61))
        self.tempLCD.setObjectName("tempLCD")
        self.humdLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.humdLCD.setGeometry(QtCore.QRect(590, 110, 101, 61))
        self.humdLCD.setObjectName("humdLCD")
        self.pushButtonNavUp = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButtonNavUp.setDown(0)
        self.pushButtonNavUp.setGeometry(QtCore.QRect(570, 360, 41, 41))
        self.pushButtonNavUp.setObjectName("pushButtonNavUp")
        self.pushButtonNavDown = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNavDown.setGeometry(QtCore.QRect(570, 480, 41, 41))
        self.pushButtonNavDown.setObjectName("pushButtonNavDown")
        self.pushButtonNavCenter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNavCenter.setGeometry(QtCore.QRect(570, 420, 41, 41))
        self.pushButtonNavCenter.setObjectName("pushButtonNavCenter")
        self.pushButtonNavRight = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNavRight.setGeometry(QtCore.QRect(640, 420, 41, 41))
        self.pushButtonNavRight.setObjectName("pushButtonNavRight")
        self.pushButtonNavLeft = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNavLeft.setGeometry(QtCore.QRect(500, 420, 41, 41))
        self.pushButtonNavLeft.setObjectName("pushButtonNavLeft")
        self.charLed12 = QtWidgets.QRadioButton(self.centralwidget)
        self.charLed12.setGeometry(QtCore.QRect(360, 240, 16, 20))
        self.charLed12.setText("")
        self.charLed12.setObjectName("charLed12")
        self.charLed12.toggled.connect(self.radio)
        self.charLed2 = QtWidgets.QRadioButton(self.centralwidget)
        self.charLed2.setGeometry(QtCore.QRect(420, 280, 16, 20))
        self.charLed2.setText("")
        self.charLed2.setObjectName("charLed2")
        self.charLed2.toggled.connect(self.radio)
        self.charLed3 = QtWidgets.QRadioButton(self.centralwidget)
        self.charLed3.setGeometry(QtCore.QRect(440, 320, 16, 20))
        self.charLed3.setText("")
        self.charLed3.setObjectName("charLed3")
        self.charLed3.toggled.connect(self.radio)
        self.charLed4 = QtWidgets.QRadioButton(self.centralwidget)
        self.charLed4.setGeometry(QtCore.QRect(420, 360, 16, 20))
        self.charLed4.setText("")
        self.charLed4.setObjectName("charLed4")
        self.charLed4.toggled.connect(self.radio)
        self.charLed1 = QtWidgets.QRadioButton(self.centralwidget)
        self.charLed1.setGeometry(QtCore.QRect(400, 260, 16, 20))
        self.charLed1.setText("")
        self.charLed1.setObjectName("charLed1")
        self.charLed1.toggled.connect(self.radio)
        self.charLed5 = QtWidgets.QRadioButton(self.centralwidget)
        self.charLed5.setGeometry(QtCore.QRect(400, 380, 16, 20))
        self.charLed5.setText("")
        self.charLed5.setObjectName("charLed5")
        self.charLed5.toggled.connect(self.radio)
        self.charLed6 = QtWidgets.QRadioButton(self.centralwidget)
        self.charLed6.setGeometry(QtCore.QRect(360, 400, 16, 20))
        self.charLed6.setText("")
        self.charLed6.setObjectName("charLed6")
        self.charLed6.toggled.connect(self.radio)
        self.charLed7 = QtWidgets.QRadioButton(self.centralwidget)
        self.charLed7.setGeometry(QtCore.QRect(320, 380, 16, 20))
        self.charLed7.setText("")
        self.charLed7.setObjectName("charLed7")
        self.charLed7.toggled.connect(self.radio)
        self.charLed8 = QtWidgets.QRadioButton(self.centralwidget)
        self.charLed8.setGeometry(QtCore.QRect(300, 360, 16, 21))
        self.charLed8.setText("")
        self.charLed8.setObjectName("charLed8")
        self.charLed8.toggled.connect(self.radio)
        self.charLed9 = QtWidgets.QRadioButton(self.centralwidget)
        self.charLed9.setGeometry(QtCore.QRect(280, 320, 16, 20))
        self.charLed9.setText("")
        self.charLed9.setObjectName("charLed9")
        self.charLed9.toggled.connect(self.radio)
        self.charLed10 = QtWidgets.QRadioButton(self.centralwidget)
        self.charLed10.setGeometry(QtCore.QRect(300, 280, 16, 20))
        self.charLed10.setText("")
        self.charLed10.setObjectName("charLed10")
        self.charLed10.toggled.connect(self.radio)
        self.charLed11 = QtWidgets.QRadioButton(self.centralwidget)
        self.charLed11.setGeometry(QtCore.QRect(320, 260, 16, 20))
        self.charLed11.setText("")
        self.charLed11.setObjectName("charLed11")
        self.charLed11.toggled.connect(self.radio)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(660, 230, 118, 23))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"border: 1px solid black;\n"
"text-align: top;\n"
"padding: 1px;\n"
"border-top-left-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #fff,\n"
"stop: 0.4999 #eee,\n"
"stop: 0.5 #ddd,\n"
"stop: 1 #eee );\n"
"width: 15px;\n"
"}\n"
"QProgressBar::chunk {\n"
"background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,\n"
"stop: 0 #0000ff,\n"
"stop: 1 #ddd000 );\n"
"border-top-left-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"border: 1px solid black;\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.potLabel = QtWidgets.QLabel(self.centralwidget)
        self.potLabel.setGeometry(QtCore.QRect(60, 160, 101, 16))
        self.potLabel.setObjectName("potLabel")
        self.charlieLabel = QtWidgets.QLabel(self.centralwidget)
        self.charlieLabel.setGeometry(QtCore.QRect(330, 320, 81, 20))
        self.charlieLabel.setObjectName("charlieLabel")
        self.rLabel = QtWidgets.QLabel(self.centralwidget)
        self.rLabel.setGeometry(QtCore.QRect(60, 420, 16, 16))
        self.rLabel.setObjectName("rLabel")
        self.gLabel = QtWidgets.QLabel(self.centralwidget)
        self.gLabel.setGeometry(QtCore.QRect(110, 420, 16, 16))
        self.gLabel.setObjectName("gLabel")
        self.bLabel = QtWidgets.QLabel(self.centralwidget)
        self.bLabel.setGeometry(QtCore.QRect(160, 420, 16, 16))
        self.bLabel.setObjectName("bLabel")
        self.navLabel = QtWidgets.QLabel(self.centralwidget)
        self.navLabel.setGeometry(QtCore.QRect(550, 530, 81, 16))
        self.navLabel.setObjectName("navLabel")
        self.tempLabel = QtWidgets.QLabel(self.centralwidget)
        self.tempLabel.setGeometry(QtCore.QRect(490, 170, 101, 20))
        self.tempLabel.setObjectName("tempLabel")
        self.humdLabel = QtWidgets.QLabel(self.centralwidget)
        self.humdLabel.setGeometry(QtCore.QRect(610, 170, 71, 20))
        self.humdLabel.setObjectName("humdLabel")
        self.ldrLAbel = QtWidgets.QLabel(self.centralwidget)
        self.ldrLAbel.setGeometry(QtCore.QRect(710, 260, 21, 20))
        self.ldrLAbel.setObjectName("ldrLAbel")
        self.HnHlabel = QtWidgets.QLabel(self.centralwidget)
        self.HnHlabel.setGeometry(QtCore.QRect(280, 540, 211, 20))
        self.HnHlabel.setObjectName("HnHlabel")
        self.headingLabel = QtWidgets.QLabel(self.centralwidget)
        self.headingLabel.setGeometry(QtCore.QRect(100, 440, 21, 16))
        self.headingLabel.setObjectName("headingLabel")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(250, 0, 291, 101))
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        # self.menuEdit = QtWidgets.QMenu(self.menubar)
        # self.menuEdit.setObjectName("menuEdit")
        # self.menuSetting = QtWidgets.QMenu(self.menubar)
        # self.menuSetting.setObjectName("menuSetting")
        # self.menuCOM_PORT = QtWidgets.QMenu(self.menuSetting)
        # self.menuCOM_PORT.setObjectName("menuCOM_PORT")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
       # self.actionReset = QtWidgets.QAction(MainWindow)
        #self.actionReset.setObjectName("actionReset")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.triggered.connect(QtCore.QCoreApplication.instance().quit)
        #self.actionCOM_1 = QtWidgets.QAction(MainWindow)
        #self.actionCOM_1.setObjectName("actionCOM_1")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionDocumentation.triggered.connect(self.urlDoc)
        self.menuFile.addAction(self.actionQuit)
        # self.menuCOM_PORT.addAction(self.actionCOM_1)
        # self.menuSetting.addAction(self.menuCOM_PORT.menuAction())
        self.menuHelp.addAction(self.actionDocumentation)
        self.menubar.addAction(self.menuFile.menuAction())
        #self.menubar.addAction(self.menuEdit.menuAction())
        # self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ARBD1 DASHBOARD V1.0"))
        MainWindow.setWindowIcon(QtGui.QIcon('graphics/icon.png'))
        self.pushButtonBuzzer.setText(_translate("MainWindow", "BUZZER"))
        self.pushButtonNavUp.setText(_translate("MainWindow", "^"))
        self.pushButtonNavDown.setText(_translate("MainWindow", "^"))
        self.pushButtonNavCenter.setText(_translate("MainWindow", "X"))
        self.pushButtonNavRight.setText(_translate("MainWindow", ">"))
        self.pushButtonNavLeft.setText(_translate("MainWindow", "<"))
        self.potLabel.setText(_translate("MainWindow", "POTENTIOMETER"))
        self.charlieLabel.setText(_translate("MainWindow", "CHARLIEPLEX"))
        self.rLabel.setText(_translate("MainWindow", "R"))
        self.gLabel.setText(_translate("MainWindow", "G"))
        self.bLabel.setText(_translate("MainWindow", "B"))
        self.navLabel.setText(_translate("MainWindow", "Navi Switches"))
        self.tempLabel.setText(_translate("MainWindow", "Temperature °C"))
        self.humdLabel.setText(_translate("MainWindow", "Humidity %"))
        self.ldrLAbel.setText(_translate("MainWindow", "LDR"))
        self.HnHlabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">&nbsp;&nbsp;&nbsp;HatchNhack Solutions</span></p></body></html>"))
        self.headingLabel.setText(_translate("MainWindow", "LED"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">ARBD1 DASHBOARD</span></p><p align=\"center\"><span style=\" font-size:10pt;\"></span></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        #self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
    def radio(self):
            if(self.charLed1.isChecked()):
                ArLib.board.charlieplexing('Z', 'Z', 'L', 'H')
            elif (self.charLed2.isChecked()):
                    ArLib.board.charlieplexing('Z', 'L', 'Z', 'H')
            elif (self.charLed3.isChecked()):
                    ArLib.board.charlieplexing('L', 'Z', 'Z', 'H')
            elif (self.charLed4.isChecked()):
                    ArLib.board.charlieplexing('Z', 'L', 'H', 'Z')
            elif (self.charLed5.isChecked()):
                    ArLib.board.charlieplexing('L', 'Z', 'H', 'Z')
            elif (self.charLed6.isChecked()):
                    ArLib.board.charlieplexing('Z', 'Z', 'H', 'L')
            elif (self.charLed7.isChecked()):
                    ArLib.board.charlieplexing('L', 'H', 'Z', 'Z')
            elif (self.charLed8.isChecked()):
                    ArLib.board.charlieplexing('Z', 'H', 'Z', 'L')
            elif (self.charLed9.isChecked()):
                    ArLib.board.charlieplexing('Z', 'H', 'L', 'Z')
            elif (self.charLed10.isChecked()):
                    ArLib.board.charlieplexing('H', 'Z', 'Z', 'L')
            elif (self.charLed11.isChecked()):
                    ArLib.board.charlieplexing('H','Z','L','Z')
            elif (self.charLed12.isChecked()):
                    ArLib.board.charlieplexing('H', 'L', 'Z', 'Z')

# For buzzer
    def btnstate(self):
        if self.pushButtonBuzzer.isChecked():
                ArLib.board.buzzerAnalog(1)
        else:
                ArLib.board.buzzerAnalog(0)

    def valueChangeR(self):
            ArLib.board.rgbAnalogR(self.rSlider.value()/100)
    def valueChangeG(self):
            ArLib.board.rgbAnalogG(self.gSlider.value()/100)
    def valueChangeB(self):
            ArLib.board.rgbAnalogB(self.bSlider.value()/100)
    def ldrBar(self,val):
            self.progressBar.setValue(val)
           # self.tempLCD.display(val)
    def setPot(self,val):
            self.dial.setValue(val)
            self.lcdNumber.display(val)
    def getTemp(self,val):
            self.tempLCD.display(val)
    def getHumidity(self,val):
            self.humdLCD.display(val)


    def getNav(self,val):
            #print('Value is ', val)
            if val==1:
                self.pushButtonNavUp.setDown(1)
            elif val==2:
                self.pushButtonNavDown.setDown(1)
            elif val==3:
                self.pushButtonNavLeft.setDown(1)
            elif val==4:
                self.pushButtonNavRight.setDown(1)
            elif val==5:
                self.pushButtonNavCenter.setDown(1)
            else:
                self.pushButtonNavUp.setDown(0)
                self.pushButtonNavDown.setDown(0)
                self.pushButtonNavLeft.setDown(0)
                self.pushButtonNavRight.setDown(0)
                self.pushButtonNavCenter.setDown(0)
    def urlDoc(self):
            webbrowser.open('https://arbd1.hatchnhack.com/', new=2)
    def startThread(self):
            self.thread=MyThread()
            self.thread.pot_value.connect(self.setPot)
            self.thread.ldr.connect(self.ldrBar)
            self.thread.nav_val.connect(self.getNav)
            self.thread.temp.connect(self.getTemp)
            self.thread.humidity.connect(self.getHumidity)
            self.thread.start()

# class MyWin(QtWidgets.QMainWindow):
#     def __init__(self,parent=None):
#         QtWidgets.QWidget.__init__(self)
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)




class MyThread(QThread):
        pot_value=pyqtSignal(int)
        ldr=pyqtSignal(int)
        nav_val=pyqtSignal(int)
        temp=pyqtSignal(int)
        humidity=pyqtSignal(int)
        def run(self):

                while 1:
                        val_pot=ArLib.board.potentiometer()
                        val_dht=ArLib.board.ldr()
                        nav=ArLib.board.navigationSwitches()
                        dht=ArLib.board.tempAndHumidity()
                        temp_vals=dht[0]
                        humd_val=dht[1]
                        self.nav_val.emit(nav)
                        self.ldr.emit(val_dht)
                        self.pot_value.emit(val_pot)
                        self.temp.emit(temp_vals)
                        self.humidity.emit(humd_val)
                        #print('Done')




#
# if __name__=="__main__":
#     app=QtWidgets.QApplication(sys.argv)
#     myapp=MyWin()
#     myapp.show()
#     sys.exit(app.exec_())