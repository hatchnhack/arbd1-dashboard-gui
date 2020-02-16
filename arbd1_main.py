import glob
import serial
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from UI import Ui_MainWindow,ArLib
import serial.tools.list_ports
class Main(object):
    def serial_descp(self):
        ports = list(serial.tools.list_ports.comports())
        portList = []
        for p in ports:
            portList.append(str(p))
        return portList
    def serial_ports(self):
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        self.result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                self.result.append(port)
            except (OSError, serial.SerialException):
                pass
        return self.result

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(539, 206)


        # self.quit = QtWidgets.QAction(MainWindow)
        # self.quit.triggered.connect(self.closeEvent)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 155, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.startButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 155, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 5, 73, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("COM")
        self.comboBox.activated.connect(self.handleActivated)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 5, 81, 26))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.on_click_refresh)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 10, 66, 16))
        self.label.setObjectName("label")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 576, 226))
        self.graphicsView.setStyleSheet("")
        self.graphicsView.setObjectName("graphicsView")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(25, 35, 466, 76))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("graphics/ARBD1.png"))
        self.label_2.setObjectName("label_2")
        self.notificationLabel = QtWidgets.QLabel(self.centralwidget)
        self.notificationLabel.setGeometry(QtCore.QRect(170,120,236,16))
        self.notificationLabel.setObjectName("notificationLabel")
        self.graphicsView.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.comboBox.raise_()
        self.pushButton_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.notificationLabel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ARBD1 V1.0"))
        MainWindow.setWindowIcon(QtGui.QIcon('graphics/icon.png'))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
        self.pushButton_2.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.pushButton_3.setText(_translate("MainWindow", "Refresh"))
        self.label.setText(_translate("MainWindow", "COM PORT"))

    def handleActivated(self,portIndex):
        self.selectedCom=portIndex
        if self.comboBox.itemText(portIndex)=='COM':
            pass
        else:
            #print(self.comboBox.itemText(portIndex))
            _translate = QtCore.QCoreApplication.translate
            k=self.serial_descp()
            #print(self.portIndex)
            self.notificationLabel.setText(_translate("MainWindow", k[self.portIndex]))

    # Refresh Button Method to refresh COM Port
    def on_click_refresh(self):
        # self.p = self.serial_ports()
        # self.comboBox.clear()
        # self.comboBox.addItem("COM")
        # #self.port=self.ports()
        # for i in self.p:
        #     self.comboBox.addItem(i)

        self.portIndex=None
        self.p=self.serial_descp()
        self.comboBox.clear()
        self.comboBox.addItem("COM")
        for i in self.p:
            self.comboBox.addItem(i[0:4])
            self.portIndex=self.p.index(i)








    def startButton(self):

        _translate = QtCore.QCoreApplication.translate
       # self.notificationLabel.setText(_translate("MainWindow", "Loading........................."))
        try:
            ArLib.board.intiate(self.comboBox.itemText(self.selectedCom))
            self.openwindow()

        except:
            try:
                self.window.show()
            except:
                #print("COM PORT NOT SELECTED")
                _translate = QtCore.QCoreApplication.translate
                self.notificationLabel.setText(_translate("MainWindow", "COM PORT NOT SELECTED"))

    def openwindow(self):
        self.window=QtWidgets.QMainWindow()
        self.mainUI=Ui_MainWindow()
        self.mainUI.setupUi(self.window)
        self.window.show()
class MyWin(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self)
        self.ui = Main()
        self.ui.setupUi(self)
        self.ui.on_click_refresh()

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    myapp=MyWin()
    myapp.show()
    sys.exit(app.exec_())