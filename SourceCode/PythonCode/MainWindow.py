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
import classify_pts
import DefiningF1AndGamma
import DefiningF1AndGammaAndFeatures
import classify_pts_test
import create_test_assign
import classify_theta_train
import classify_theta
import multimodel_class
import testingFeaturesFile
import plot_quality
import MainBCV
import shutil
import textWidget
import ViewInputFile
import webbrowser
import SelectingPDFFileToOpen
import SelectingPDFFileAndDatFileToOpen
import selectingPlotFolderAndFile

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
		self.dockWidgetContentsTop = QtGui.QStackedWidget()
		self.dockWidgetContentsTop.setObjectName(_fromUtf8("dockWidgetContentsTop"))
		# Isso é da area em branco no topo... Acredito que vá sair#
		#self.gridLayoutTop = QtGui.QGridLayout(self.dockWidgetContentsTop)
		#self.gridLayoutTop.setObjectName(_fromUtf8("gridLayoutTop"))
		#self.verticalLayoutTopInside = QtGui.QVBoxLayout()
		#self.verticalLayoutTopInside.setObjectName(_fromUtf8("verticalLayoutTopInside"))
		#self.gridLayoutTop.addLayout(self.verticalLayoutTopInside, 0, 0, 1, 1)
		# (FIM) Isso é da area em branco no topo... Acredito que vá sair#
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

		## Preenche Widgets
		self.dockWidgetContentsTop.addWidget(QtGui.QWidget()) # 0
		self.dockWidgetContentsTop.addWidget(ViewInputFile.Ui_Form()) # 1
		self.dockWidgetContentsTop.addWidget(textWidget.Ui_Form()) # 2
		self.dockWidgetContentsTop.addWidget(SelectingPDFFileToOpen.Ui_Form()) # 3
		self.dockWidgetContentsTop.addWidget(SelectingPDFFileAndDatFileToOpen.Ui_Form()) # 4
		self.dockWidgetContentsTop.addWidget(selectingPlotFolderAndFile.Ui_Form()) # 5
		## Fim Preenche Widgets

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
		self.toolsClusteringQualityMenuBetaCVAction = self.toolsClusteringQualityMenu.addAction("BetaCV", self.openMainQualityBCV)
		self.toolsClusteringQualityMenuSilhouetteAction = self.toolsClusteringQualityMenu.addAction(_fromUtf8("Silhouette Index"))
		self.toolsClusteringPlotMenu = self.toolsClusteringMenu.addMenu("Plot")
		self.toolsClusteringPlotMenuPlotAction = self.toolsClusteringPlotMenu.addAction("Plot Examples", self.openMainPlotExamples)
		self.toolsClassifierMenu = self.toolsMenu.addMenu("Classifier")
		self.toolsClassifierMenuProbAction = self.toolsClassifierMenu.addAction("Probability Only", self.openMainClassifierProbOnly)
		self.toolsClassifierMenuERTreeAction = self.toolsClassifierMenu.addAction("ERTree Only", self.openMainClassifierERTreeOnly)
		self.toolsClassifierMenuERTreeProbAction = self.toolsClassifierMenu.addAction("ERTree + Prob", self.openMainClassifierERTreeP)
		self.toolsClassifierMenuTrendLearnerAction = self.toolsClassifierMenu.addAction("TrendLearner", self.openMainClassifierTrendLearner)


		self.viewMenu = self.menubar.addMenu('&View')
		self.viewInputMenu = self.viewMenu.addAction('Input Results', self.setOneWidget)
		self.viewClusteringMenu = self.viewMenu.addMenu('Clustering')
		self.viewClusteringClusteringMenu = self.viewClusteringMenu.addMenu('Clustering')
		self.viewClusteringClusteringKSCAction = self.viewClusteringClusteringMenu.addAction('K-SC Results')
		self.viewClusteringQualityMenu = self.viewClusteringMenu.addMenu('Quality')
		self.viewClusteringPlotMenu = self.viewClusteringMenu.addMenu('Plot')
		self.viewClusteringPlotPlotAction = self.viewClusteringPlotMenu.addAction('Plot Examples Results')
		self.viewClassifierMenu = self.viewMenu.addMenu('Classifier')
		self.viewClassifierProbAction = self.viewClassifierMenu.addAction('Probability Only Results')
		self.viewClassifierERTreeAction = self.viewClassifierMenu.addAction('ERTree Only Results')
		self.viewClassifierERTreeProbAction = self.viewClassifierMenu.addAction('ERTree + Prob  Results')
		self.viewClassifierTrendLearnerAction = self.viewClassifierMenu.addAction('TrendLearner Results')
	   
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
		self.viewInputMenu.setDisabled(True)
		self.viewClusteringClusteringKSCAction.setDisabled(True)
		self.viewClusteringPlotPlotAction.setDisabled(True)
		self.viewClassifierERTreeAction.setDisabled(True)
		self.viewClassifierProbAction.setDisabled(True)
		self.viewClassifierERTreeProbAction.setDisabled(True)
		self.viewClassifierTrendLearnerAction.setDisabled(True)


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
		self.probabilityOnlyButton.clicked.connect(self.openMainClassifierProbOnly)
		self.ertreeOnlyButton.clicked.connect(self.openMainClassifierERTreeOnly)
		self.ertreePButton.clicked.connect(self.openMainClassifierERTreeP)
		self.trendLearnerButton.clicked.connect(self.openMainClassifierTrendLearner)
		self.bcvButton.clicked.connect(self.openMainQualityBCV)


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

	def openMainQualityBCV(self):
		self.plainTextEditLog.appendPlainText("Generating quality...")
		self.mainBCVWin = MainBCV.Ui_Dialog(self)
		self.mainBCVWin.show()
		self.mainBCVWin.buttonBox.button(QtGui.QDialogButtonBox.Cancel).clicked.connect(self.CancelButtonPressed)
		self.mainBCVWin.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.bcvOkButtonPressed)

	def bcvOkButtonPressed(self):
		plotfolder = os.path.join(self.projectDirectory, "BCV")
		os.makedirs(plotfolder)
		plot_quality.main(os.path.join(self.projectDirectory, "Data", "Input.txt"), plotfolder, self.mainBCVWin.spinBox.value())
		self.bcvButton.setDisabled(True)
		self.toolsClusteringQualityMenuBetaCVAction.setDisabled(True)

		#Show
		self.setThreeWidget()
		self.viewClusteringQualityBetaCVAction = self.viewClusteringQualityMenu.addAction('BetaCV Results',self.setThreeWidget)
		#FimShow
		self.plainTextEditLog.appendPlainText("Done!\n")

	def openMainClassifierProbOnly(self):
		self.plainTextEditLog.appendPlainText("Classifying...")
		self.DefiningF1andGammaWinProbOnly = DefiningF1AndGamma.Ui_Dialog()
		self.DefiningF1andGammaWinProbOnly.show()
		self.fillComboBoxClassProbOnly()
		self.DefiningF1andGammaWinProbOnly.buttonBox.button(QtGui.QDialogButtonBox.Cancel).clicked.connect(self.CancelButtonPressed)
		self.DefiningF1andGammaWinProbOnly.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.openMainClassifierProbOnlyOk)

	def openMainClassifierProbOnlyOk(self):
		if str(self.DefiningF1andGammaWinProbOnly.comboBox.currentText()) != "":
			plotfolder = os.path.join(os.path.join(self.projectDirectory,str(self.DefiningF1andGammaWinProbOnly.comboBox.currentText())), "Classifiers")
			try:
				os.makedirs(plotfolder)
			except:
				pass
			plotfolder = os.path.join(plotfolder,"ProbOnly")
			os.makedirs(plotfolder)

			#Chamar Métodos Aqui
			os.makedirs( os.path.join(plotfolder, "probs") )
			classify_pts.classifyPtsMethod(self.projectDirectory + "/Data/Input.txt", self.projectDirectory + "/Data/train.dat", os.path.join(plotfolder,"../../cents.dat"), os.path.join(plotfolder,"../../assign.dat"), os.path.join(plotfolder,"probs"), self.DefiningF1andGammaWinProbOnly.spinBox.value())
			
			os.makedirs( os.path.join(plotfolder, "probs-test") )
			classify_pts_test.classifyPtsMethod(self.projectDirectory + "/Data/Input.txt", os.path.join(plotfolder,"../../cents.dat"), self.projectDirectory + "/Data/test.dat", os.path.join(plotfolder,"../../assign.dat"), os.path.join(plotfolder,"probs-test"), self.DefiningF1andGammaWinProbOnly.spinBox.value())

			create_test_assign.create_test_assignMethod(self.projectDirectory + "/Data/Input.txt", self.projectDirectory + "/Data/test.dat", os.path.join(plotfolder,"../../cents.dat"), os.path.join(plotfolder,"../../test_assign.dat"))
			
			os.makedirs( os.path.join(plotfolder, "cls-res-fitted-" + str(self.DefiningF1andGammaWinProbOnly.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaWinProbOnly.spinBox.value()) + "-train") )
			classify_theta_train.classify_theta_trainMethod(self.projectDirectory + "/Data/Input.txt", plotfolder , self.DefiningF1andGammaWinProbOnly.doubleSpinBox.value(), "cls-res-fitted-" + str(self.DefiningF1andGammaWinProbOnly.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaWinProbOnly.spinBox.value()) + "-train", self.DefiningF1andGammaWinProbOnly.spinBox.value(), self.mainKSCWin.spinBox.value())
			
			os.makedirs( os.path.join(plotfolder, "cls-res-fitted-" + str(self.DefiningF1andGammaWinProbOnly.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaWinProbOnly.spinBox.value())) )
			classify_theta.main(self.projectDirectory + "/Data/Input.txt", plotfolder , self.DefiningF1andGammaWinProbOnly.doubleSpinBox.value(), "cls-res-fitted-" + str(self.DefiningF1andGammaWinProbOnly.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaWinProbOnly.spinBox.value()), self.DefiningF1andGammaWinProbOnly.spinBox.value(), self.mainKSCWin.spinBox.value())
			
			multimodel_class.calcProbOnly(plotfolder, "cls-res-fitted-" + str(self.DefiningF1andGammaWinProbOnly.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaWinProbOnly.spinBox.value()), self.DefiningF1andGammaWinProbOnly.spinBox.value())
			#Fim dos Métodos

			self.plainTextEditLog.appendPlainText("Done!\n")
		else:
			self.createErrorBox("All possible classifications have already been generated")

	def openMainClassifierERTreeOnly(self):
		self.plainTextEditLog.appendPlainText("Classifying...")
		self.DefiningF1andGammaAndFeaturesWinERTreeOnly = DefiningF1AndGammaAndFeatures.Ui_Dialog()
		self.DefiningF1andGammaAndFeaturesWinERTreeOnly.show()
		self.fillComboBoxClassERTreeOnly()
		self.DefiningF1andGammaAndFeaturesWinERTreeOnly.buttonBox.button(QtGui.QDialogButtonBox.Cancel).clicked.connect(self.CancelButtonPressed)
		self.DefiningF1andGammaAndFeaturesWinERTreeOnly.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.openMainClassifierERTreeOnlyOk)

	def openMainClassifierERTreeOnlyOk(self):
		if str(self.DefiningF1andGammaAndFeaturesWinERTreeOnly.comboBox.currentText()) != "":
			if not self.DefiningF1andGammaAndFeaturesWinERTreeOnly.lineEdit.text().isEmpty():
				plotfolder = os.path.join(os.path.join(self.projectDirectory,str(self.DefiningF1andGammaAndFeaturesWinERTreeOnly.comboBox.currentText())), "Classifiers")
				try:
					os.makedirs(plotfolder)
				except:
					pass
				plotfolder = os.path.join(plotfolder,"ERTreeOnly")
				os.makedirs(plotfolder)

				#Chamar Métodos Aqui
				os.makedirs( os.path.join(plotfolder, "probs") )
				classify_pts.classifyPtsMethod(self.projectDirectory + "/Data/Input.txt", self.projectDirectory + "/Data/train.dat", os.path.join(plotfolder,"../../cents.dat"), os.path.join(plotfolder,"../../assign.dat"), os.path.join(plotfolder,"probs"), self.DefiningF1andGammaAndFeaturesWinERTreeOnly.spinBox.value())
				
				os.makedirs( os.path.join(plotfolder, "probs-test") )
				classify_pts_test.classifyPtsMethod(self.projectDirectory + "/Data/Input.txt", os.path.join(plotfolder,"../../cents.dat"), self.projectDirectory + "/Data/test.dat", os.path.join(plotfolder,"../../assign.dat"), os.path.join(plotfolder,"probs-test"), self.DefiningF1andGammaAndFeaturesWinERTreeOnly.spinBox.value())

				create_test_assign.create_test_assignMethod(self.projectDirectory + "/Data/Input.txt", self.projectDirectory + "/Data/test.dat", os.path.join(plotfolder,"../../cents.dat"), os.path.join(plotfolder,"../../test_assign.dat"))
				
				os.makedirs( os.path.join(plotfolder, "cls-res-fitted-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeOnly.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeOnly.spinBox.value()) + "-train") )
				classify_theta_train.classify_theta_trainMethod(self.projectDirectory + "/Data/Input.txt", plotfolder , self.DefiningF1andGammaAndFeaturesWinERTreeOnly.doubleSpinBox.value(), "cls-res-fitted-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeOnly.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeOnly.spinBox.value()) + "-train", self.DefiningF1andGammaAndFeaturesWinERTreeOnly.spinBox.value(), self.mainKSCWin.spinBox.value())
				
				os.makedirs( os.path.join(plotfolder, "cls-res-fitted-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeOnly.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeOnly.spinBox.value())) )
				classify_theta.main(self.projectDirectory + "/Data/Input.txt", plotfolder , self.DefiningF1andGammaAndFeaturesWinERTreeOnly.doubleSpinBox.value(), "cls-res-fitted-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeOnly.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeOnly.spinBox.value()), self.DefiningF1andGammaAndFeaturesWinERTreeOnly.spinBox.value(), self.mainKSCWin.spinBox.value())
				
				if testingFeaturesFile.testOne(unicode(self.DefiningF1andGammaAndFeaturesWinERTreeOnly.lineEdit.text().toUtf8(), encoding="UTF-8"), plotfolder, "cls-res-fitted-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeOnly.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeOnly.spinBox.value()), self.DefiningF1andGammaAndFeaturesWinERTreeOnly.spinBox.value()):
					multimodel_class.calcERTreeOnly(unicode(self.DefiningF1andGammaAndFeaturesWinERTreeOnly.lineEdit.text().toUtf8(), encoding="UTF-8"), plotfolder, "cls-res-fitted-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeOnly.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeOnly.spinBox.value()), self.DefiningF1andGammaAndFeaturesWinERTreeOnly.spinBox.value())
					self.plainTextEditLog.appendPlainText("Done!\n")
				else:
					self.createErrorBox('The operation can not be completed because the files in features directory are in incompatible format.\n\nCheck Help contents to see the correct format.')
					shutil.rmtree(plotfolder)
					self.plainTextEditLog.appendPlainText("Interrupted!\n")
				#Fim dos Métodos
			else:
				self.createErrorBox("You need provide a features directory folder")
				self.plainTextEditLog.appendPlainText("Interrupted!\n")
		else:
			self.createErrorBox("All possible classifications have already been generated")
			self.plainTextEditLog.appendPlainText("Interrupted!\n")

	def openMainClassifierERTreeP(self):
		self.plainTextEditLog.appendPlainText("Classifying...")
		self.DefiningF1andGammaAndFeaturesWinERTreeP = DefiningF1AndGammaAndFeatures.Ui_Dialog()
		self.DefiningF1andGammaAndFeaturesWinERTreeP.show()
		self.fillComboBoxClassERTreeP()
		self.DefiningF1andGammaAndFeaturesWinERTreeP.buttonBox.button(QtGui.QDialogButtonBox.Cancel).clicked.connect(self.CancelButtonPressed)
		self.DefiningF1andGammaAndFeaturesWinERTreeP.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.openMainClassifierERTreePOk)

	def openMainClassifierERTreePOk(self):
		if str(self.DefiningF1andGammaAndFeaturesWinERTreeP.comboBox.currentText()) != "":
			if not self.DefiningF1andGammaAndFeaturesWinERTreeP.lineEdit.text().isEmpty():
				plotfolder = os.path.join(os.path.join(self.projectDirectory,str(self.DefiningF1andGammaAndFeaturesWinERTreeP.comboBox.currentText())), "Classifiers")
				try:
					os.makedirs(plotfolder)
				except:
					pass
				plotfolder = os.path.join(plotfolder,"ERTreeP")
				os.makedirs(plotfolder)

				#Chamar Métodos Aqui
				os.makedirs( os.path.join(plotfolder, "probs") )
				classify_pts.classifyPtsMethod(self.projectDirectory + "/Data/Input.txt", self.projectDirectory + "/Data/train.dat", os.path.join(plotfolder,"../../cents.dat"), os.path.join(plotfolder,"../../assign.dat"), os.path.join(plotfolder,"probs"), self.DefiningF1andGammaAndFeaturesWinERTreeP.spinBox.value())
				
				os.makedirs( os.path.join(plotfolder, "probs-test") )
				classify_pts_test.classifyPtsMethod(self.projectDirectory + "/Data/Input.txt", os.path.join(plotfolder,"../../cents.dat"), self.projectDirectory + "/Data/test.dat", os.path.join(plotfolder,"../../assign.dat"), os.path.join(plotfolder,"probs-test"), self.DefiningF1andGammaAndFeaturesWinERTreeP.spinBox.value())

				create_test_assign.create_test_assignMethod(self.projectDirectory + "/Data/Input.txt", self.projectDirectory + "/Data/test.dat", os.path.join(plotfolder,"../../cents.dat"), os.path.join(plotfolder,"../../test_assign.dat"))
				
				os.makedirs( os.path.join(plotfolder, "cls-res-fitted-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeP.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeP.spinBox.value()) + "-train") )
				classify_theta_train.classify_theta_trainMethod(self.projectDirectory + "/Data/Input.txt", plotfolder , self.DefiningF1andGammaAndFeaturesWinERTreeP.doubleSpinBox.value(), "cls-res-fitted-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeP.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeP.spinBox.value()) + "-train", self.DefiningF1andGammaAndFeaturesWinERTreeP.spinBox.value(), self.mainKSCWin.spinBox.value())
				
				os.makedirs( os.path.join(plotfolder, "cls-res-fitted-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeP.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeP.spinBox.value())) )
				classify_theta.main(self.projectDirectory + "/Data/Input.txt", plotfolder , self.DefiningF1andGammaAndFeaturesWinERTreeP.doubleSpinBox.value(), "cls-res-fitted-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeP.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeP.spinBox.value()), self.DefiningF1andGammaAndFeaturesWinERTreeP.spinBox.value(), self.mainKSCWin.spinBox.value())
				
				if testingFeaturesFile.testOne(unicode(self.DefiningF1andGammaAndFeaturesWinERTreeP.lineEdit.text().toUtf8(), encoding="UTF-8"), plotfolder, "cls-res-fitted-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeP.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeP.spinBox.value()), self.DefiningF1andGammaAndFeaturesWinERTreeP.spinBox.value()):
					multimodel_class.calcERTreeP(unicode(self.DefiningF1andGammaAndFeaturesWinERTreeP.lineEdit.text().toUtf8(), encoding="UTF-8"), plotfolder, "cls-res-fitted-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeP.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaAndFeaturesWinERTreeP.spinBox.value()), self.DefiningF1andGammaAndFeaturesWinERTreeP.spinBox.value())
					self.plainTextEditLog.appendPlainText("Done!\n")
				else:
					self.createErrorBox('The operation can not be completed because the files in features directory are in incompatible format.\n\nCheck Help contents to see the correct format.')
					shutil.rmtree(plotfolder)
					self.plainTextEditLog.appendPlainText("Interrupted!\n")
				#Fim dos Métodos
			else:
				self.createErrorBox("You need provide a features directory folder")
				self.plainTextEditLog.appendPlainText("Interrupted!\n")
		else:
			self.createErrorBox("All possible classifications have already been generated")
			self.plainTextEditLog.appendPlainText("Interrupted!\n")

	def openMainClassifierTrendLearner(self):
		self.plainTextEditLog.appendPlainText("Classifying...")
		self.DefiningF1andGammaAndFeaturesWinTrendLearner = DefiningF1AndGammaAndFeatures.Ui_Dialog()
		self.DefiningF1andGammaAndFeaturesWinTrendLearner.show()
		self.fillComboBoxClassTrendLearner()
		self.DefiningF1andGammaAndFeaturesWinTrendLearner.buttonBox.button(QtGui.QDialogButtonBox.Cancel).clicked.connect(self.CancelButtonPressed)
		self.DefiningF1andGammaAndFeaturesWinTrendLearner.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.openMainClassifierTrendLearnerOk)

	def openMainClassifierTrendLearnerOk(self):
		if str(self.DefiningF1andGammaAndFeaturesWinTrendLearner.comboBox.currentText()) != "":
			if not self.DefiningF1andGammaAndFeaturesWinTrendLearner.lineEdit.text().isEmpty():
				plotfolder = os.path.join(os.path.join(self.projectDirectory,str(self.DefiningF1andGammaAndFeaturesWinTrendLearner.comboBox.currentText())), "Classifiers")
				try:
					os.makedirs(plotfolder)
				except:
					pass
				plotfolder = os.path.join(plotfolder,"TrendLearner")
				os.makedirs(plotfolder)

				#Chamar Métodos Aqui
				os.makedirs( os.path.join(plotfolder, "probs") )
				classify_pts.classifyPtsMethod(self.projectDirectory + "/Data/Input.txt", self.projectDirectory + "/Data/train.dat", os.path.join(plotfolder,"../../cents.dat"), os.path.join(plotfolder,"../../assign.dat"), os.path.join(plotfolder,"probs"), self.DefiningF1andGammaAndFeaturesWinTrendLearner.spinBox.value())
				
				os.makedirs( os.path.join(plotfolder, "probs-test") )
				classify_pts_test.classifyPtsMethod(self.projectDirectory + "/Data/Input.txt", os.path.join(plotfolder,"../../cents.dat"), self.projectDirectory + "/Data/test.dat", os.path.join(plotfolder,"../../assign.dat"), os.path.join(plotfolder,"probs-test"), self.DefiningF1andGammaAndFeaturesWinTrendLearner.spinBox.value())

				create_test_assign.create_test_assignMethod(self.projectDirectory + "/Data/Input.txt", self.projectDirectory + "/Data/test.dat", os.path.join(plotfolder,"../../cents.dat"), os.path.join(plotfolder,"../../test_assign.dat"))
				
				os.makedirs( os.path.join(plotfolder, "cls-res-fitted-" + str(self.DefiningF1andGammaAndFeaturesWinTrendLearner.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaAndFeaturesWinTrendLearner.spinBox.value()) + "-train") )
				classify_theta_train.classify_theta_trainMethod(self.projectDirectory + "/Data/Input.txt", plotfolder , self.DefiningF1andGammaAndFeaturesWinTrendLearner.doubleSpinBox.value(), "cls-res-fitted-" + str(self.DefiningF1andGammaAndFeaturesWinTrendLearner.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaAndFeaturesWinTrendLearner.spinBox.value()) + "-train", self.DefiningF1andGammaAndFeaturesWinTrendLearner.spinBox.value(), self.mainKSCWin.spinBox.value())
				
				os.makedirs( os.path.join(plotfolder, "cls-res-fitted-" + str(self.DefiningF1andGammaAndFeaturesWinTrendLearner.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaAndFeaturesWinTrendLearner.spinBox.value())) )
				classify_theta.main(self.projectDirectory + "/Data/Input.txt", plotfolder , self.DefiningF1andGammaAndFeaturesWinTrendLearner.doubleSpinBox.value(), "cls-res-fitted-" + str(self.DefiningF1andGammaAndFeaturesWinTrendLearner.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaAndFeaturesWinTrendLearner.spinBox.value()), self.DefiningF1andGammaAndFeaturesWinTrendLearner.spinBox.value(), self.mainKSCWin.spinBox.value())
				
				if testingFeaturesFile.testOne(unicode(self.DefiningF1andGammaAndFeaturesWinTrendLearner.lineEdit.text().toUtf8(), encoding="UTF-8"), plotfolder, "cls-res-fitted-" + str(self.DefiningF1andGammaAndFeaturesWinTrendLearner.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaAndFeaturesWinTrendLearner.spinBox.value()), self.DefiningF1andGammaAndFeaturesWinTrendLearner.spinBox.value()):
					multimodel_class.calcTrendLearner(unicode(self.DefiningF1andGammaAndFeaturesWinTrendLearner.lineEdit.text().toUtf8(), encoding="UTF-8"), plotfolder, "cls-res-fitted-" + str(self.DefiningF1andGammaAndFeaturesWinTrendLearner.doubleSpinBox.value()) + "-" + str(self.DefiningF1andGammaAndFeaturesWinTrendLearner.spinBox.value()), self.DefiningF1andGammaAndFeaturesWinTrendLearner.spinBox.value())
					self.plainTextEditLog.appendPlainText("Done!\n")
				else:
					self.createErrorBox('The operation can not be completed because the files in features directory are in incompatible format.\n\nCheck Help contents to see the correct format.')
					shutil.rmtree(plotfolder)
					self.plainTextEditLog.appendPlainText("Interrupted!\n")
				#Fim dos Métodos
			else:
				self.createErrorBox("You need provide a features directory folder")
				self.plainTextEditLog.appendPlainText("Interrupted!\n")
		else:
			self.createErrorBox("All possible classifications have already been generated")
			self.plainTextEditLog.appendPlainText("Interrupted!\n")

	def openMainPlotExamples(self):
		self.plainTextEditLog.appendPlainText("Ploting examples...")
		self.selectingclusterfoldWinPlot = SelectingAClusteringFolderPlot.Ui_Dialog()
		self.selectingclusterfoldWinPlot.show()
		self.fillComboBoxPlot()
		self.selectingclusterfoldWinPlot.buttonBox.button(QtGui.QDialogButtonBox.Cancel).clicked.connect(self.CancelButtonPressed)
		self.selectingclusterfoldWinPlot.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.openMainPlotExamplesOk)

	def openMainPlotExamplesOk(self):
		if str(self.selectingclusterfoldWinPlot.comboBox.currentText()) != "":
			plotfolder = os.path.join(os.path.join(self.projectDirectory,str(self.selectingclusterfoldWinPlot.comboBox.currentText())), "Examples")
			os.makedirs(plotfolder)
			plot_members.plotExamples(self.projectDirectory + "/Data/Input.txt", self.projectDirectory + "/" +str(self.selectingclusterfoldWinPlot.comboBox.currentText()) + "/assign.dat", self.projectDirectory + "/" + str(self.selectingclusterfoldWinPlot.comboBox.currentText()) + "/cents.dat", plotfolder)
			
			#Show
			self.dockWidgetContentsTop.setCurrentIndex(5)
			self.dockWidgetContentsTop.currentWidget().pushButton.clicked.connect(self.setCleanWidget)

			self.root, self.dirs, self.files = os.walk(plotfolder).next()
			self.auxVetorDIR = []
			for mdir in self.dirs:
				self.auxVetorDIR.append(mdir)
			self.auxVetorDIR.sort()
			self.dockWidgetContentsTop.currentWidget().comboBox.clear()
			self.dockWidgetContentsTop.currentWidget().comboBox.addItems(self.auxVetorDIR)
			self.root2, self.dirs2, self.files2 = os.walk( os.path.join(plotfolder, str(self.dockWidgetContentsTop.currentWidget().comboBox.currentText()) ) ).next()
			self.auxVetorFiles = []
			for mfiles in self.files2:
				self.auxVetorFiles.append(mfiles)
			self.auxVetorFiles.sort()
			self.dockWidgetContentsTop.currentWidget().comboBox_2.clear()
			self.dockWidgetContentsTop.currentWidget().comboBox_2.addItems(self.auxVetorFiles)
			self.dockWidgetContentsTop.currentWidget().comboBox.activated.connect(lambda: self.on_combo_activatedPlotExamples(plotfolder))
			self.dockWidgetContentsTop.currentWidget().pushButton_2.clicked.connect(lambda: self.openPlotExamplesImage(plotfolder) )
			#FimShow

			self.plainTextEditLog.appendPlainText("Done!\n")
		else:
			self.createErrorBox("All possible examples have already been generated")

	def openPlotExamplesImage(self,directoryArg):
		filename = os.path.join(directoryArg,unicode(self.dockWidgetContentsTop.currentWidget().comboBox.currentText().toUtf8(), encoding="UTF-8"), unicode(self.dockWidgetContentsTop.currentWidget().comboBox_2.currentText().toUtf8(), encoding="UTF-8"))
		webbrowser.open(filename)

	def on_combo_activatedPlotExamples(self, directoryArg):
		self.root2, self.dirs2, self.files2 = os.walk( os.path.join(directoryArg, str(self.dockWidgetContentsTop.currentWidget().comboBox.currentText()) ) ).next()
		self.auxVetorFiles = []
		for mfiles in self.files2:
			self.auxVetorFiles.append(mfiles)
		self.auxVetorFiles.sort()
		self.dockWidgetContentsTop.currentWidget().comboBox_2.clear()
		self.dockWidgetContentsTop.currentWidget().comboBox_2.addItems(self.auxVetorFiles)

	def fillComboBoxPlot(self):
		self.root, self.dirs, self.files = os.walk(self.projectDirectory).next()
		self.auxVetor = []
		for self.dirname in self.dirs:
			if( self.dirname[:11] == "Clustering_") and (not os.path.isdir(os.path.join(os.path.join(self.projectDirectory,self.dirname),"Examples")) ):
				self.auxVetor.append(self.dirname)
		self.auxVetor.sort()
		self.selectingclusterfoldWinPlot.comboBox.clear()
		self.selectingclusterfoldWinPlot.comboBox.addItems(self.auxVetor)

	def fillComboBoxClassProbOnly(self):
		self.root, self.dirs, self.files = os.walk(self.projectDirectory).next()
		self.auxVetor = []
		for self.dirname in self.dirs:
			if( self.dirname[:11] == "Clustering_") and (not os.path.isdir( os.path.join(os.path.join(os.path.join(self.projectDirectory,self.dirname),"Classifiers"), "ProbOnly")) ):
				self.auxVetor.append(self.dirname)
		self.auxVetor.sort()
		self.DefiningF1andGammaWinProbOnly.comboBox.clear()
		self.DefiningF1andGammaWinProbOnly.comboBox.addItems(self.auxVetor)

	def fillComboBoxClassERTreeP(self):
		self.root, self.dirs, self.files = os.walk(self.projectDirectory).next()
		self.auxVetor = []
		for self.dirname in self.dirs:
			if( self.dirname[:11] == "Clustering_") and (not os.path.isdir( os.path.join(os.path.join(os.path.join(self.projectDirectory,self.dirname),"Classifiers"), "ERTreeP")) ):
				self.auxVetor.append(self.dirname)
		self.auxVetor.sort()
		self.DefiningF1andGammaAndFeaturesWinERTreeP.comboBox.clear()
		self.DefiningF1andGammaAndFeaturesWinERTreeP.comboBox.addItems(self.auxVetor)

	def fillComboBoxClassTrendLearner(self):
		self.root, self.dirs, self.files = os.walk(self.projectDirectory).next()
		self.auxVetor = []
		for self.dirname in self.dirs:
			if( self.dirname[:11] == "Clustering_") and (not os.path.isdir( os.path.join(os.path.join(os.path.join(self.projectDirectory,self.dirname),"Classifiers"), "TrendLearner")) ):
				self.auxVetor.append(self.dirname)
		self.auxVetor.sort()
		self.DefiningF1andGammaAndFeaturesWinTrendLearner.comboBox.clear()
		self.DefiningF1andGammaAndFeaturesWinTrendLearner.comboBox.addItems(self.auxVetor)

	def fillComboBoxClassERTreeOnly(self):
		self.root, self.dirs, self.files = os.walk(self.projectDirectory).next()
		self.auxVetor = []
		for self.dirname in self.dirs:
			if( self.dirname[:11] == "Clustering_") and (not os.path.isdir( os.path.join(os.path.join(os.path.join(self.projectDirectory,self.dirname),"Classifiers"), "ERTreeOnly")) ):
				self.auxVetor.append(self.dirname)
		self.auxVetor.sort()
		self.DefiningF1andGammaAndFeaturesWinERTreeOnly.comboBox.clear()
		self.DefiningF1andGammaAndFeaturesWinERTreeOnly.comboBox.addItems(self.auxVetor)

	def CancelButtonPressed(self):
		self.plainTextEditLog.appendPlainText("Canceled!\n")

	def kscOkButtonPressed(self):
		cluster.clusterKSC(self.projectDirectory + "/Data/Input.txt", self.projectDirectory + "/Data/", self.mainKSCWin.spinBox.value())
		self.setKscButtonDisabled()

		#Show
		self.dockWidgetContentsTop.setCurrentIndex(4)
		self.root, self.dirs, self.files = os.walk( os.path.join(self.projectDirectory, "Clustering_KSC") ) .next()
		self.auxVetorPDF = []
		self.auxVetorDAT = []
		for mfiles in self.files:
			if mfiles[-4:] == ".pdf":
				self.auxVetorPDF.append(mfiles)
			elif mfiles[-4:] == ".dat":
				self.auxVetorDAT.append(mfiles)
		self.auxVetorPDF.sort()
		self.auxVetorDAT.sort()
		self.dockWidgetContentsTop.currentWidget().comboBox.clear()
		self.dockWidgetContentsTop.currentWidget().comboBox.addItems(self.auxVetorPDF)
		self.dockWidgetContentsTop.currentWidget().comboBox_2.clear()
		self.dockWidgetContentsTop.currentWidget().comboBox_2.addItems(self.auxVetorDAT)
		self.dockWidgetContentsTop.currentWidget().pushButton.clicked.connect(self.setCleanWidget)
		self.dockWidgetContentsTop.currentWidget().pushButton_2.clicked.connect(self.openKSCPDF)
		self.dockWidgetContentsTop.currentWidget().pushButton_4.clicked.connect(self.openKSCDAT)
		self.dockWidgetContentsTop.currentWidget().pushButton_3.clicked.connect(self.setKSCView)
		#FimShow

		self.plainTextEditLog.appendPlainText("Done!\n")

	def checkOkButton(self):
		if not self.mainInputWin.lineEdit.text().isEmpty():
			if generateCrossVals.tryload_series(unicode(self.mainInputWin.lineEdit.text().toUtf8(), encoding="UTF-8")):
				if self.mainInputWin.radioButton.isChecked():
					self.plainTextEditLog.appendPlainText("Reading Input File...")
					generateCrossVals.generateCrossValsRandom(unicode(self.mainInputWin.lineEdit.text().toUtf8(), encoding="UTF-8"),self.projectDirectory)
					self.setUploadFileButtonDisabled()

					# Show #
					self.setOneWidget()
					# Show #

					self.plainTextEditLog.appendPlainText("Done!\n")
				elif self.mainInputWin.radioButton_2.isChecked():
					self.plainTextEditLog.appendPlainText("Reading Input File...")
					generateCrossVals.generateCrossValsSequential(unicode(self.mainInputWin.lineEdit.text().toUtf8(), encoding="UTF-8"),self.projectDirectory, self.mainInputWin.spinBox.value()/100.00)
					self.setUploadFileButtonDisabled()

					# Show #
					self.setOneWidget()
					# Show #

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
		#self.silhouetteButton.setDisabled(False)
		#Menus
		self.toolsClusteringClusteringMenuKSCAction.setDisabled(False)
		self.toolsClusteringQualityMenuBetaCVAction.setDisabled(False)
		#self.toolsClusteringQualityMenuSilhouetteAction.setDisabled(False)
		self.viewInputMenu.setDisabled(False)
		
	def createErrorBox(self,notification):
		msg = QtGui.QMessageBox()
		msg.setIcon(QtGui.QMessageBox.Critical)

		msg.setText(notification)
		msg.setWindowTitle("Erro")
		msg.setStandardButtons(QtGui.QMessageBox.Ok)	
		retval = msg.exec_()
	
	def setCleanWidget(self):
		self.dockWidgetContentsTop.setCurrentIndex(0)

	def setOneWidget(self):
		self.dockWidgetContentsTop.setCurrentIndex(1)
		self.dockWidgetContentsTop.currentWidget().pushButton.clicked.connect(self.setInputText)
		self.dockWidgetContentsTop.currentWidget().pushButton_2.clicked.connect(self.setTestText)
		self.dockWidgetContentsTop.currentWidget().pushButton_3.clicked.connect(self.setTrainText)
		self.dockWidgetContentsTop.currentWidget().pushButton_4.clicked.connect(self.setCleanWidget)
		self.dockWidgetContentsTop.currentWidget().pushButton_5.clicked.connect(self.openInputText)
		self.dockWidgetContentsTop.currentWidget().pushButton_6.clicked.connect(self.openTestText)
		self.dockWidgetContentsTop.currentWidget().pushButton_7.clicked.connect(self.openTrainText)

	def setThreeWidget(self):
		self.dockWidgetContentsTop.setCurrentIndex(3)
		self.root, self.dirs, self.files = os.walk( os.path.join(self.projectDirectory, "BCV") ) .next()
		self.auxVetor = []
		for mfiles in self.files:
			if mfiles[-4:] == ".pdf":
				self.auxVetor.append(mfiles)
		self.auxVetor.sort()
		self.dockWidgetContentsTop.currentWidget().comboBox.clear()
		self.dockWidgetContentsTop.currentWidget().comboBox.addItems(self.auxVetor)

		self.dockWidgetContentsTop.currentWidget().pushButton_2.clicked.connect(self.openBCVPDF)
		self.dockWidgetContentsTop.currentWidget().pushButton.clicked.connect(self.setCleanWidget)

	def setFourWidget(self):
		self.dockWidgetContentsTop.setCurrentIndex(4)

	def openBCVPDF(self):
		filename = os.path.join(self.projectDirectory, "BCV", unicode(self.dockWidgetContentsTop.currentWidget().comboBox.currentText().toUtf8(), encoding="UTF-8"))
		webbrowser.open(filename)

	def openKSCPDF(self):
		filename = os.path.join(self.projectDirectory, "Clustering_KSC", unicode(self.dockWidgetContentsTop.currentWidget().comboBox.currentText().toUtf8(), encoding="UTF-8"))
		webbrowser.open(filename)

	def openKSCDAT(self):
		filename = os.path.join(self.projectDirectory, "Clustering_KSC", unicode(self.dockWidgetContentsTop.currentWidget().comboBox_2.currentText().toUtf8(), encoding="UTF-8"))
		webbrowser.open(filename)

	def openInputText(self):
		filename = os.path.join(self.projectDirectory, "Data", "Input.txt") 
		editor = os.getenv('EDITOR')
		if editor:
			ps.system(editor + ' ' + filename)
		else:
			webbrowser.open(filename)

	def openTestText(self):
		filename = os.path.join(self.projectDirectory, "Data", "test.dat") 
		editor = os.getenv('EDITOR')
		if editor:
			ps.system(editor + ' ' + filename)
		else:
			webbrowser.open(filename)

	def openTrainText(self):
		filename = os.path.join(self.projectDirectory, "Data", "train.dat") 
		editor = os.getenv('EDITOR')
		if editor:
			ps.system(editor + ' ' + filename)
		else:
			webbrowser.open(filename)

	def setKSCView(self):
		self.auxWord = self.dockWidgetContentsTop.currentWidget().comboBox_2.currentText()
		self.dockWidgetContentsTop.setCurrentIndex(2)
		self.dockWidgetContentsTop.currentWidget().plainTextEdit.clear()
		self.dockWidgetContentsTop.currentWidget().pushButton.clicked.connect(self.setFourWidget)
		self.dockWidgetContentsTop.currentWidget().plainTextEdit.appendPlainText( open( os.path.join(self.projectDirectory, "Clustering_KSC", str(self.auxWord) ) ).read() )

	def setInputText(self):
		self.dockWidgetContentsTop.setCurrentIndex(2)
		self.dockWidgetContentsTop.currentWidget().plainTextEdit.clear()
		self.dockWidgetContentsTop.currentWidget().pushButton.clicked.connect(self.setOneWidget)
		self.dockWidgetContentsTop.currentWidget().plainTextEdit.appendPlainText( open( os.path.join(self.projectDirectory, "Data", "Input.txt")).read() )

	def setTestText(self):
		self.dockWidgetContentsTop.setCurrentIndex(2)
		self.dockWidgetContentsTop.currentWidget().plainTextEdit.clear()
		self.dockWidgetContentsTop.currentWidget().pushButton.clicked.connect(self.setOneWidget)
		self.dockWidgetContentsTop.currentWidget().plainTextEdit.appendPlainText( open( os.path.join(self.projectDirectory, "Data", "test.dat")).read() )

	def setTrainText(self):
		self.dockWidgetContentsTop.setCurrentIndex(2)
		self.dockWidgetContentsTop.currentWidget().plainTextEdit.clear()
		self.dockWidgetContentsTop.currentWidget().pushButton.clicked.connect(self.setOneWidget)
		self.dockWidgetContentsTop.currentWidget().plainTextEdit.appendPlainText( open( os.path.join(self.projectDirectory, "Data", "train.dat")).read() )

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	ex = Ui_MainWindow()
	ex.show()
	sys.exit(app.exec_())