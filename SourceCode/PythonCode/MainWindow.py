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
import generateCrossVals
import os
import cluster
import MainKSC
import plot_members
import SelectingAClusteringFolderPlot

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
		

		## Tenta
		self.gridLayoutCentral = QtGui.QGridLayout(self.centralwidget)
		self.gridLayoutCentral.setObjectName(_fromUtf8("gridLayoutCentral"))
		self.verticalLayoutTop = QtGui.QVBoxLayout()
		self.verticalLayoutTop.setObjectName(_fromUtf8("verticalLayoutTop"))
		self.dockWidgetTop = QtGui.QDockWidget(self.centralwidget)
		self.dockWidgetTop.setObjectName(_fromUtf8("dockWidgetTop"))
		self.dockWidgetContentsTop = QtGui.QWidget()
		self.dockWidgetContentsTop.setObjectName(_fromUtf8("dockWidgetContentsTop"))
		self.gridLayoutTop = QtGui.QGridLayout(self.dockWidgetContentsTop)
		self.gridLayoutTop.setObjectName(_fromUtf8("gridLayoutTop"))
		self.verticalLayoutTopInside = QtGui.QVBoxLayout()
		self.verticalLayoutTopInside.setObjectName(_fromUtf8("verticalLayoutTopInside"))
		self.gridLayoutTop.addLayout(self.verticalLayoutTopInside, 0, 0, 1, 1)
		self.dockWidgetTop.setWidget(self.dockWidgetContentsTop)
		self.verticalLayoutTop.addWidget(self.dockWidgetTop)
		self.gridLayoutCentral.addLayout(self.verticalLayoutTop, 0, 0, 1, 1)
		self.verticalLayoutDown = QtGui.QVBoxLayout()
		self.verticalLayoutDown.setObjectName(_fromUtf8("verticalLayoutDown"))
		self.dockWidgetDown = QtGui.QDockWidget(self.centralwidget)
		self.dockWidgetDown.setObjectName(_fromUtf8("dockWidgetDown"))
		self.dockWidgetContentsDown = QtGui.QWidget()
		self.dockWidgetContentsDown.setObjectName(_fromUtf8("dockWidgetContentsDown"))
		self.gridLayoutDown = QtGui.QGridLayout(self.dockWidgetContentsDown)
		self.gridLayoutDown.setObjectName(_fromUtf8("gridLayoutDown"))
		self.verticalLayoutDownInside = QtGui.QVBoxLayout()
		self.verticalLayoutDownInside.setObjectName(_fromUtf8("verticalLayoutDownInside"))
		self.plainTextEditLog = QtGui.QPlainTextEdit(self.dockWidgetContentsDown)
		self.plainTextEditLog.setObjectName(_fromUtf8("plainTextEditLog"))
		self.plainTextEditLog.setReadOnly(True)
		self.verticalLayoutDownInside.addWidget(self.plainTextEditLog)
		self.gridLayoutDown.addLayout(self.verticalLayoutDownInside, 0, 0, 1, 1)
		self.dockWidgetDown.setWidget(self.dockWidgetContentsDown)
		self.verticalLayoutDown.addWidget(self.dockWidgetDown)
		self.gridLayoutCentral.addLayout(self.verticalLayoutDown, 1, 0, 1, 1)
		self.plainTextEditLog.appendPlainText("TrendLearnerApp started...\n")

		## Temporário
		self.plainTextEditLog2 = QtGui.QPlainTextEdit(self.dockWidgetContentsTop)
		self.plainTextEditLog2.setObjectName(_fromUtf8("plainTextEditLog2"))
		self.plainTextEditLog2.setReadOnly(True)
		self.verticalLayoutTopInside.addWidget(self.plainTextEditLog2)
		## FimTemporário
		## FimTenta

		# MenuBar
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
		self.menubar.setObjectName(_fromUtf8("menubar"))
	   
		self.projectMenu = self.menubar.addMenu('&Project')
		self.projectMenuNewAction = self.projectMenu.addAction("New...")
		self.projectMenuSaveAction = self.projectMenu.addAction("Save")
		self.projectMenu.addSeparator()
		self.projectMenuExitAction = self.projectMenu.addAction("Exit")
		#fileMenu.addAction("Hue")

		self.editMenu = self.menubar.addMenu('&Edit')
		#editMenu.addAction("Hue")

		self.toolsMenu = self.menubar.addMenu('&Tools')
		self.toolsInputMenu = self.toolsMenu.addMenu("Input")
		self.toolsInputMenuReadFileAction = self.toolsInputMenu.addAction("ReadFile", self.openMainInput)
		self.toolsClusteringMenu = self.toolsMenu.addMenu("Clustering")
		self.toolsClusteringClusteringMenu = self.toolsClusteringMenu.addMenu("Clustering")
		self.toolsClusteringClusteringMenuKSCAction = self.toolsClusteringClusteringMenu.addAction("K-SC", self.openMainKSC)
		self.toolsClusteringQualityMenu = self.toolsClusteringMenu.addMenu("Quality")
		self.toolsClusteringQualityMenuBetaCVAction = self.toolsClusteringQualityMenu.addAction("BetaCV")
		self.toolsClusteringQualityMenuSilhouetteAction = self.toolsClusteringQualityMenu.addAction(_fromUtf8("Silhouette Index"))
		self.toolsClusteringPlotMenu = self.toolsClusteringMenu.addMenu("Plot")
		self.toolsClusteringPlotMenuPlotAction = self.toolsClusteringPlotMenu.addAction("Plot Examples", self.openMainPlotExamples)
		self.toolsClassifierMenu = self.toolsMenu.addMenu("Classifier")
		self.toolsClassifierMenuProbAction = self.toolsClassifierMenu.addAction("Probability Only")
		self.toolsClassifierMenuERTreeAction = self.toolsClassifierMenu.addAction("ERTree Only")
		self.toolsClassifierMenuERTreeProbAction = self.toolsClassifierMenu.addAction("ERTree + Prob")
		self.toolsClassifierMenuTrendLearnerAction = self.toolsClassifierMenu.addAction("TrendLearner")


		self.viewMenu = self.menubar.addMenu('&View')
	   
		self.helpMenu = self.menubar.addMenu('&Help')
		self.helpMenuHelpAction = self.helpMenu.addAction("Help Contents")
		self.helpMenuAboutAction = self.helpMenu.addAction("About TrendLearnerApp")
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


		# Desabilitando butões
		self.kscButton.setDisabled(True)
		self.bcvButton.setDisabled(True)
		self.silhouetteButton.setDisabled(True)
		self.plotExamplesButton.setDisabled(True)
		self.probabilityOnlyButton.setDisabled(True)
		self.ertreePButton.setDisabled(True)
		self.ertreeOnlyButton.setDisabled(True)
		self.trendLearnerButton.setDisabled(True)
		#Desabilitando Menus
		self.toolsClusteringClusteringMenuKSCAction.setDisabled(True)
		self.toolsClusteringQualityMenuBetaCVAction.setDisabled(True)
		self.toolsClusteringQualityMenuSilhouetteAction.setDisabled(True)
		self.toolsClusteringPlotMenuPlotAction.setDisabled(True)
		self.toolsClassifierMenuERTreeAction.setDisabled(True)
		self.toolsClassifierMenuProbAction.setDisabled(True)
		self.toolsClassifierMenuTrendLearnerAction.setDisabled(True)
		self.toolsClassifierMenuERTreeProbAction.setDisabled(True)


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
		self.silhouetteButton.setText(_translate("TrendLearnerApp", "Silhouette Index", None))
		self.toolBox.setItemText(self.toolBox.indexOf(self.IOWidget), _translate("TrendLearnerApp", "Input", None))
		self.toolBox.setItemText(self.toolBox.indexOf(self.ClusteringWidget), _translate("TrendLearnerApp", "Clustering", None))
		self.toolBox.setItemText(self.toolBox.indexOf(self.ClassifierWidget), _translate("TrendLearnerApp", "Classifier", None))
		self.uploadFileButton.clicked.connect(self.openMainInput)
		self.kscButton.clicked.connect(self.openMainKSC)
		self.plotExamplesButton.clicked.connect(self.openMainPlotExamples)

	def openMainInput(self):
		self.mainInputWin = MainInput.Ui_Dialog(self)
		#self.mainInputWin.exec_()
		self.mainInputWin.show()
		self.mainInputWin.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.checkOkButton)

	def openMainKSC(self):
		self.mainKSCWin = MainKSC.Ui_Dialog(self)
		self.mainKSCWin.show()
		self.plainTextEditLog.appendPlainText("Clustering...")
		self.mainKSCWin.buttonBox.button(QtGui.QDialogButtonBox.Cancel).clicked.connect(self.CancelButtonPressed)
		self.mainKSCWin.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.kscOkButtonPressed)

	def openMainPlotExamples(self):
		self.plainTextEditLog.appendPlainText("Ploting examples...")
		self.selectingclusterfoldWin = SelectingAClusteringFolderPlot.Ui_Dialog()
		self.selectingclusterfoldWin.show()
		self.fillComboBox()
		self.selectingclusterfoldWin.buttonBox.button(QtGui.QDialogButtonBox.Cancel).clicked.connect(self.CancelButtonPressed)
		self.selectingclusterfoldWin.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.openMainPlotExamplesOk)

	def openMainPlotExamplesOk(self):
		if str(self.selectingclusterfoldWin.comboBox.currentText()) != "":
			plotfolder = os.path.join(os.path.join(self.projectDirectory,str(self.selectingclusterfoldWin.comboBox.currentText())), "Examples")
			os.makedirs(plotfolder)
			plot_members.plotExamples(self.projectDirectory + "/Data/Input.txt", self.projectDirectory + "/" +str(self.selectingclusterfoldWin.comboBox.currentText()) + "/assign.dat", self.projectDirectory + "/" + str(self.selectingclusterfoldWin.comboBox.currentText()) + "/cents.dat", plotfolder)
			self.plainTextEditLog.appendPlainText("Done!\n")
		else:
			self.createErrorBox("All possible examples have already been generated")

	def fillComboBox(self):
		self.root, self.dirs, self.files = os.walk(self.projectDirectory).next()
		self.auxVetor = []
		for self.dirname in self.dirs:
			if( self.dirname[:11] == "Clustering_") and (not os.path.isdir(os.path.join(os.path.join(self.projectDirectory,self.dirname),"Examples")) ):
				self.auxVetor.append(self.dirname)
		self.auxVetor.sort()
		self.selectingclusterfoldWin.comboBox.addItems(self.auxVetor)

	def CancelButtonPressed(self):
		self.plainTextEditLog.appendPlainText("Canceled!\n")

	def kscOkButtonPressed(self):
		cluster.clusterKSC(self.projectDirectory + "/Data/Input.txt", self.projectDirectory + "/Data/", self.mainKSCWin.spinBox.value())
		self.setKscButtonDisabled()
		self.plainTextEditLog.appendPlainText("Done!\n")

	def checkOkButton(self):
		if not self.mainInputWin.lineEdit.text().isEmpty():
			if generateCrossVals.tryload_series(unicode(self.mainInputWin.lineEdit.text().toUtf8(), encoding="UTF-8")):
				if self.mainInputWin.radioButton.isChecked():
					self.plainTextEditLog.appendPlainText("Reading Input File...")
					generateCrossVals.generateCrossValsRandom(unicode(self.mainInputWin.lineEdit.text().toUtf8(), encoding="UTF-8"),self.projectDirectory)
					self.setUploadFileButtonDisabled()
					self.plainTextEditLog.appendPlainText("Done!\n")
				elif self.mainInputWin.radioButton_2.isChecked():
					self.plainTextEditLog.appendPlainText("Reading Input File...")
					generateCrossVals.generateCrossValsSequential(unicode(self.mainInputWin.lineEdit.text().toUtf8(), encoding="UTF-8"),self.projectDirectory, self.mainInputWin.spinBox.value()/100.00)
					self.setUploadFileButtonDisabled()
					self.plainTextEditLog.appendPlainText("Done!\n")
				else:
					sys.exit()
			else:
				self.createErrorBox('The operation can not be completed because the file is in incompatible format.\n\nCheck Help contents to see the correct format.')
		else:
			self.createErrorBox('The operation can not be completed because the file directory is empty')

	def setKscButtonDisabled(self):
		self.kscButton.setDisabled(True)
		self.toolsClusteringClusteringMenuKSCAction.setDisabled(True)
		#Butões
		self.plotExamplesButton.setDisabled(False)
		self.probabilityOnlyButton.setDisabled(False)
		self.ertreePButton.setDisabled(False)
		self.ertreeOnlyButton.setDisabled(False)
		self.trendLearnerButton.setDisabled(False)
		#Desabilitando Menus
		self.toolsClusteringPlotMenuPlotAction.setDisabled(False)
		self.toolsClassifierMenuERTreeAction.setDisabled(False)
		self.toolsClassifierMenuProbAction.setDisabled(False)
		self.toolsClassifierMenuTrendLearnerAction.setDisabled(False)
		self.toolsClassifierMenuERTreeProbAction.setDisabled(False)

	def setUploadFileButtonDisabled(self):
		self.uploadFileButton.setDisabled(True)
		self.toolsInputMenuReadFileAction.setDisabled(True)
		#Butões
		self.kscButton.setDisabled(False)
		self.bcvButton.setDisabled(False)
		self.silhouetteButton.setDisabled(False)
		#Menus
		self.toolsClusteringClusteringMenuKSCAction.setDisabled(False)
		self.toolsClusteringQualityMenuBetaCVAction.setDisabled(False)
		self.toolsClusteringQualityMenuSilhouetteAction.setDisabled(False)
		

	def createErrorBox(self,notification):
		msg = QtGui.QMessageBox()
		msg.setIcon(QtGui.QMessageBox.Critical)

		msg.setText(notification)
		msg.setWindowTitle("Erro")
		msg.setStandardButtons(QtGui.QMessageBox.Ok)	
		retval = msg.exec_()
		

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	ex = Ui_MainWindow()
	ex.show()
	sys.exit(app.exec_())