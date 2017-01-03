# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teste2.ui'
#
# Created: Mon Jan  2 16:09:35 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import NewProjectWindow
import MainInput

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

        # CentralWidget
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        


        # MenuBar
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
       
        self.projectMenu = self.menubar.addMenu('&Project')
        self.projectMenu.addAction("New...")
        self.projectMenu.addAction("Save")
        self.projectMenu.addSeparator()
        self.projectMenu.addAction("Exit")
        #fileMenu.addAction("Hue")

        self.editMenu = self.menubar.addMenu('&Edit')
        #editMenu.addAction("Hue")

        self.toolsMenu = self.menubar.addMenu('&Tools')
        self.toolsInputMenu = self.toolsMenu.addMenu("Input")
        self.toolsInputMenu.addAction("ReadFile", self.openMainInput)
        self.toolsClusteringMenu = self.toolsMenu.addMenu("Clustering")
        self.toolsClusteringClusteringMenu = self.toolsClusteringMenu.addMenu("Clustering")
        self.toolsClusteringClusteringMenu.addAction("K-SC")
        self.toolsClusteringQualityMenu = self.toolsClusteringMenu.addMenu("Quality")
        self.toolsClusteringQualityMenu.addAction("BetaCV")
        self.toolsClusteringQualityMenu.addAction(_fromUtf8("Silhouette Index"))
        self.toolsClusteringPlotMenu = self.toolsClusteringMenu.addMenu("Plot")
        self.toolsClusteringPlotMenu.addAction("Plot Examples")
        self.toolsClassifierMenu = self.toolsMenu.addMenu("Classifier")
        self.toolsClassifierMenu.addAction("Probability Only")
        self.toolsClassifierMenu.addAction("ERTree Only")
        self.toolsClassifierMenu.addAction("ERTree + Prob")
        self.toolsClassifierMenu.addAction("TrendLearner")


        self.viewMenu = self.menubar.addMenu('&View')
        #viewMenu.addAction("Hue")
       
        self.helpMenu = self.menubar.addMenu('&Help')
        self.helpMenu.addAction("Help Contents")
        self.helpMenu.addAction("About TrendLearnerApp")
        #helpMenu.addAction("Hue")
        MainWindow.setMenuBar(self.menubar)



        # StatusBar
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)



        # DockWidget
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
        
        self.IOWidget = QtGui.QWidget()
        self.IOWidget.setGeometry(QtCore.QRect(0, 0, 124, 415))
        self.IOWidget.setObjectName(_fromUtf8("IOWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.IOWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.uploadFileButton = QtGui.QPushButton(self.IOWidget)
        self.uploadFileButton.setObjectName(_fromUtf8("uploadFileButton"))
        self.verticalLayout_3.addWidget(self.uploadFileButton)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.toolBox.addItem(self.IOWidget, _fromUtf8(""))
        
        
        self.ClusteringWidget = QtGui.QWidget()
        self.ClusteringWidget.setObjectName(_fromUtf8("ClusteringWidget"))
        self.gridLayout = QtGui.QGridLayout(self.ClusteringWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.toolBox.addItem(self.ClusteringWidget, _fromUtf8(""))


        self.toolBoxClustering = QtGui.QToolBox(self.ClusteringWidget)
        self.toolBoxClustering.setObjectName(_fromUtf8("toolBoxClustering"))
        self.ClusteringClusteringWidget = QtGui.QWidget()
        self.ClusteringClusteringWidget.setGeometry(QtCore.QRect(0, 0, 104, 234))
        self.ClusteringClusteringWidget.setObjectName(_fromUtf8("ClusteringClusteringWidget"))
        self.toolBoxClustering.addItem(self.ClusteringClusteringWidget, _fromUtf8(""))
        
        self.horizontalLayoutClusteringClusteringWidget = QtGui.QHBoxLayout(self.ClusteringClusteringWidget)
        self.horizontalLayoutClusteringClusteringWidget.setObjectName(_fromUtf8("horizontalLayoutClusteringClusteringWidget"))
        self.verticalLayoutClusteringClusteringWidget = QtGui.QVBoxLayout()
        self.verticalLayoutClusteringClusteringWidget.setObjectName(_fromUtf8("verticalLayoutClusteringClusteringWidget"))
        self.kscButton = QtGui.QPushButton(self.ClusteringClusteringWidget)
        self.kscButton.setObjectName(_fromUtf8("kscButton"))
        self.verticalLayoutClusteringClusteringWidget.addWidget(self.kscButton)
        #self.kmeansButton = QtGui.QPushButton(self.ClusteringClusteringWidget)
        #self.kmeansButton.setObjectName(_fromUtf8("kmeansButton"))
        #self.verticalLayoutClusteringClusteringWidget.addWidget(self.kmeansButton)
        self.horizontalLayoutClusteringClusteringWidget.addLayout(self.verticalLayoutClusteringClusteringWidget)


        self.ClusteringQualityWidget = QtGui.QWidget()
        self.ClusteringQualityWidget.setGeometry(QtCore.QRect(0, 0, 104, 234))
        self.ClusteringQualityWidget.setObjectName(_fromUtf8("ClusteringQualityWidget"))
        self.toolBoxClustering.addItem(self.ClusteringQualityWidget, _fromUtf8(""))
        self.horizontalLayoutClusteringQualityWidget = QtGui.QHBoxLayout(self.ClusteringQualityWidget)
        self.horizontalLayoutClusteringQualityWidget.setObjectName(_fromUtf8("horizontalLayoutClusteringQualityWidget"))
        self.verticalLayoutClusteringQualityWidget = QtGui.QVBoxLayout()
        self.verticalLayoutClusteringQualityWidget.setObjectName(_fromUtf8("verticalLayoutClusteringQualityWidget"))
        self.bcvButton = QtGui.QPushButton(self.ClusteringQualityWidget)
        self.bcvButton.setObjectName(_fromUtf8("bcvButton"))
        self.verticalLayoutClusteringQualityWidget.addWidget(self.bcvButton)
        self.silhouetteButton = QtGui.QPushButton(self.ClusteringQualityWidget)
        self.silhouetteButton.setObjectName(_fromUtf8("silhouetteButton"))
        self.verticalLayoutClusteringQualityWidget.addWidget(self.silhouetteButton)
        self.horizontalLayoutClusteringQualityWidget.addLayout(self.verticalLayoutClusteringQualityWidget)



        self.ClusteringPlotWidget = QtGui.QWidget()
        self.ClusteringPlotWidget.setGeometry(QtCore.QRect(0, 0, 104, 234))
        self.ClusteringPlotWidget.setObjectName(_fromUtf8("ClusteringPlotWidget"))
        self.toolBoxClustering.addItem(self.ClusteringPlotWidget, _fromUtf8(""))
        self.horizontalLayoutClusteringPlotWidget = QtGui.QHBoxLayout(self.ClusteringPlotWidget)
        self.horizontalLayoutClusteringPlotWidget.setObjectName(_fromUtf8("horizontalLayoutClusteringPlotWidget"))
        self.verticalLayoutClusteringPlotWidget = QtGui.QVBoxLayout()
        self.verticalLayoutClusteringPlotWidget.setObjectName(_fromUtf8("verticalLayoutClusteringPlotWidget"))
        self.plotExamplesButton = QtGui.QPushButton(self.ClusteringPlotWidget)
        self.plotExamplesButton.setObjectName(_fromUtf8("plotExamplesButton"))
        self.verticalLayoutClusteringPlotWidget.addWidget(self.plotExamplesButton)
        self.horizontalLayoutClusteringPlotWidget.addLayout(self.verticalLayoutClusteringPlotWidget)
        self.verticalLayout_4.addWidget(self.toolBoxClustering)


        self.ClassifierWidget = QtGui.QWidget()
        self.ClassifierWidget.setGeometry(QtCore.QRect(0, 0, 124, 415))
        self.ClassifierWidget.setObjectName(_fromUtf8("ClassifierWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.ClassifierWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayoutClassifierWidget = QtGui.QVBoxLayout()
        self.verticalLayoutClassifierWidget.setObjectName(_fromUtf8("verticalLayoutClassifierWidget"))
        self.gridLayout_2.addLayout(self.verticalLayoutClassifierWidget, 0, 0, 1, 1)
        self.toolBox.addItem(self.ClassifierWidget, _fromUtf8(""))


        self.probabilityOnlyButton = QtGui.QPushButton(self.ClassifierWidget)
        self.probabilityOnlyButton.setObjectName(_fromUtf8("probabilityOnlyButton"))        
        self.verticalLayoutClassifierWidget.addWidget(self.probabilityOnlyButton)
        self.ertreeOnlyButton = QtGui.QPushButton(self.ClassifierWidget)
        self.ertreeOnlyButton.setObjectName(_fromUtf8("ertreeOnlyButton"))        
        self.verticalLayoutClassifierWidget.addWidget(self.ertreeOnlyButton)
        self.ertreePButton = QtGui.QPushButton(self.ClassifierWidget)
        self.ertreePButton.setObjectName(_fromUtf8("ertreePButton"))        
        self.verticalLayoutClassifierWidget.addWidget(self.ertreePButton)
        self.trendLearnerButton = QtGui.QPushButton(self.ClassifierWidget)
        self.trendLearnerButton.setObjectName(_fromUtf8("trendLearnerButton"))        
        self.verticalLayoutClassifierWidget.addWidget(self.trendLearnerButton)



        self.verticalLayout.addWidget(self.toolBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.toolBoxClustering.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("TrendLearnerApp", "TrendLearnerApp", None))
        self.uploadFileButton.setText(_translate("TrendLearnerApp", "ReadFile", None))
        self.toolBoxClustering.setItemText(self.toolBoxClustering.indexOf(self.ClusteringClusteringWidget), _translate("TrendLearnerApp", "Clustering", None))
        self.toolBoxClustering.setItemText(self.toolBoxClustering.indexOf(self.ClusteringQualityWidget), _translate("TrendLearnerApp", "Quality", None))
        self.toolBoxClustering.setItemText(self.toolBoxClustering.indexOf(self.ClusteringPlotWidget), _translate("TrendLearnerApp", "Plot", None))
        self.kscButton.setText(_translate("TrendLearnerApp", "K-SC", None))
        #self.kmeansButton.setText(_translate("TrendLearnerApp", "K-means", None))
        self.probabilityOnlyButton.setText(_translate("TrendLearnerApp", "Probability Only", None))
        self.ertreeOnlyButton.setText(_translate("TrendLearnerApp", "ERTree Only", None))
        self.ertreePButton.setText(_translate("TrendLearnerApp", "ERTree + Prob", None))
        self.trendLearnerButton.setText(_translate("TrendLearnerApp", "TrendLearner", None))
        self.plotExamplesButton.setText(_translate("TrendLearnerApp", "Plot Examples", None))
        self.bcvButton.setText(_translate("TrendLearnerApp", "BetaCV", None))
        self.silhouetteButton.setText(_translate("TrendLearnerApp", "Silhouette index", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.IOWidget), _translate("TrendLearnerApp", "Input", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.ClusteringWidget), _translate("TrendLearnerApp", "Clustering", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.ClassifierWidget), _translate("TrendLearnerApp", "Classifier", None))
        self.uploadFileButton.clicked.connect(self.openMainInput)
        

    def openMainInput(self):
        self.mainInputWin = MainInput.Ui_Dialog()
        self.mainInputWin.show()

    

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())