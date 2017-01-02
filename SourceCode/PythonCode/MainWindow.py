# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teste2.ui'
#
# Created: Mon Jan  2 16:09:35 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        #fileMenu = self.menubar.addMenu('&File')
        #fileMenu.addAction("Hue")
        

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.toolBox = QtGui.QToolBox(self.dockWidgetContents)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.First = QtGui.QWidget()
        self.First.setGeometry(QtCore.QRect(0, 0, 124, 415))
        self.First.setObjectName(_fromUtf8("First"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.First)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pushButton_2 = QtGui.QPushButton(self.First)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.toolBox_2 = QtGui.QToolBox(self.First)
        self.toolBox_2.setObjectName(_fromUtf8("toolBox_2"))
        self.page_5 = QtGui.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 104, 234))
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.toolBox_2.addItem(self.page_5, _fromUtf8(""))
        self.page_10 = QtGui.QWidget()
        self.page_10.setGeometry(QtCore.QRect(0, 0, 104, 234))
        self.page_10.setObjectName(_fromUtf8("page_10"))
        self.toolBox_2.addItem(self.page_10, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.toolBox_2)
        self.pushButton_3 = QtGui.QPushButton(self.First)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.pushButton = QtGui.QPushButton(self.First)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.toolBox.addItem(self.First, _fromUtf8(""))
        self.page_7 = QtGui.QWidget()
        self.page_7.setObjectName(_fromUtf8("page_7"))
        self.gridLayout = QtGui.QGridLayout(self.page_7)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.toolBox.addItem(self.page_7, _fromUtf8(""))
        self.page_6 = QtGui.QWidget()
        self.page_6.setGeometry(QtCore.QRect(0, 0, 124, 415))
        self.page_6.setObjectName(_fromUtf8("page_6"))
        self.gridLayout_2 = QtGui.QGridLayout(self.page_6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.toolBox.addItem(self.page_6, _fromUtf8(""))
        self.verticalLayout.addWidget(self.toolBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.toolBox_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_5), _translate("MainWindow", "Page 1", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_10), _translate("MainWindow", "Page 2", None))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.First), _translate("MainWindow", "Page 1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_7), _translate("MainWindow", "Page", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), _translate("MainWindow", "Page 2", None))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())