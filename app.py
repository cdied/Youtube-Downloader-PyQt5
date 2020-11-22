# ---------------  YouTube Downloader  -------------- #
# author: Sayed Mohammad Rezaie -- 22.Nov.2020
# github: @cdied

# description:
# 1. simple Youtube Downloader with PyQt5 UI
# 2. using PyQt5, pytube, Subprocess, sys


# --------------------  imports  -------------------- #
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pytube
import subprocess

# ---------  GUI(Graphical user interface)  --------- #
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(513, 261)
        MainWindow.setMinimumSize(QtCore.QSize(512, 261))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../PHP/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setStyleSheet("font: 25 10pt \"Bahnschrift Light\";\n"
        "color: white;")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 20, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 101, 16))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 80, 261, 31))
        self.lineEdit.setAutoFillBackground(True)
        self.lineEdit.setStyleSheet("font: 8pt \"Bahnschrift Light\";\n"
        "border: 5px;\n"
        "color:black;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 130, 141, 31))
        self.pushButton.setStyleSheet("color: #000000;")
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 200, 451, 23))
        self.progressBar.setStyleSheet("QProgressBar\n"
        "{\n"
        "color:#2F4F4F;\n"
        "}\n"
        "QProgressBar::chunk\n"
        "{\n"
        "background-color:#2F4F4F;\n"
        "}")
        self.progressBar.setProperty("value",0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 130, 111, 31))
        self.pushButton_2.setStyleSheet("color: #000000;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame.setGeometry(QtCore.QRect(0, 0, 16777215, 16777215))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy)
        self.verticalFrame.setSizeIncrement(QtCore.QSize(0, -1))
        self.verticalFrame.setStyleSheet("background-color: #008080;")
        self.verticalFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.verticalFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.verticalFrame.setLineWidth(0)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalFrame.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.progressBar.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube downloader"))
        self.label.setText(_translate("MainWindow", "Welcome to Youtube Downloader with PYQT5"))
        self.label_2.setText(_translate("MainWindow", "Enter your URL"))
        self.pushButton.setText(_translate("MainWindow", "Open file location"))
        self.pushButton_2.setText(_translate("MainWindow", "Download"))
        self.pushButton.clicked.connect(self.openlocation)
        self.pushButton_2.clicked.connect(self.download)

    # -------------------  Functions  ------------------- #

    # progressBar function
    def timerEvent(self, stream,chunk,bytes_remaining):
        progress = (100*(self.file_size-bytes_remaining))/self.file_size
        self.progressBar.setValue(int(progress))

    # Download function
    def download(self):
        link = self.lineEdit.text()
        yt = pytube.YouTube(link, on_progress_callback=self.timerEvent)
        stream = yt.streams.get_highest_resolution()
        global file_size
        file_size = 0
        self.file_size = stream.filesize
        stream.download(".\\Downloads")
    
    # open file location function
    def openlocation(self):
        subprocess.call("explorer .\\Downloads", shell=True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
