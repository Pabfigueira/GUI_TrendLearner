# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../QtDesignerCode/NewProjectWindow.ui'
#
# Created: Sat Dec  3 13:08:28 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import sys
import InitialWindow
import MainWindow
import string

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

class Ui_NewProject(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setupUi(self)

	def setupUi(self, NewProject):
		self.move(QtGui.QApplication.desktop().screen().rect().center()- self.rect().center())
		NewProject.setObjectName(_fromUtf8("NewProject"))
		NewProject.resize(453, 165)
		self.gridLayout_2 = QtGui.QGridLayout(NewProject)
		self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
		self.buttonBox = QtGui.QDialogButtonBox(NewProject)
		self.buttonBox.setEnabled(True)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)
		self.gridLayout = QtGui.QGridLayout()
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.name_label = QtGui.QLabel(NewProject)
		self.name_label.setObjectName(_fromUtf8("name_label"))
		self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)
		self.browser_btn = QtGui.QPushButton(NewProject)
		self.browser_btn.setObjectName(_fromUtf8("browser_btn"))
		self.gridLayout.addWidget(self.browser_btn, 3, 1, 1, 1)
		self.location_label = QtGui.QLabel(NewProject)
		self.location_label.setObjectName(_fromUtf8("location_label"))
		self.gridLayout.addWidget(self.location_label, 2, 0, 1, 1)
		self.location_lineEdit = QtGui.QLineEdit(NewProject)
		self.location_lineEdit.setObjectName(_fromUtf8("location_lineEdit"))
		self.location_lineEdit.setReadOnly(True)
		self.location_lineEdit.setText(os.path.expanduser("~"))
		self.gridLayout.addWidget(self.location_lineEdit, 3, 0, 1, 1)
		self.name_lineEdit = QtGui.QLineEdit(NewProject)
		self.name_lineEdit.setObjectName(_fromUtf8("name_lineEdit"))
		self.gridLayout.addWidget(self.name_lineEdit, 1, 0, 1, 2)
		self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
		self.retry = True

		self.retranslateUi(NewProject)
		QtCore.QMetaObject.connectSlotsByName(NewProject)

	def retranslateUi(self, NewProject):
		NewProject.setWindowTitle(_translate("NewProject", "New Project", None))
		self.name_label.setText(_translate("NewProject", "Project Name:", None))
		self.browser_btn.setText(_translate("NewProject", "...", None))
		self.location_label.setText(_translate("NewProject", "Location:", None))
		self.buttonBox.button(QtGui.QDialogButtonBox.Cancel).clicked.connect(self.retryToMain)
		self.browser_btn.clicked.connect(self.getFolder)
		self.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.okAction)

	def retryToMain(self):
		self.close()

	'''def getfiles(self):
		dlg = QtGui.QFileDialog()
		dlg.setFileMode(QtGui.QFileDialog.AnyFile)
		dlg.setFilter("Text files (*.txt)")
		filenames = QtCore.QStringList()
			
		if dlg.exec_():
			filenames = dlg.selectedFiles()
			f = open(filenames[0], 'r')
				
			with f:
				data = f.read()
				self.contents.setText(data)'''

	def okAction(self):

		if self.isOkNameLabel():
			directory = unicode(self.location_lineEdit.text().toUtf8(), encoding="UTF-8") 
			directory += "/"
			directory += unicode(self.name_lineEdit.text().toUtf8(), encoding="UTF-8")
			if not os.path.exists(directory):
				os.makedirs(directory)
				self.retry = False
				self.close()
			else: 
				self.createErrorBox('The operation can not be completed because the directory "' + directory + '" already exists')
		else:
			self.createErrorBox('Please enter only letters and/or numbers')
		

	def isOkNameLabel(self):
		if self.name_lineEdit.text().size() == 0 :
			return False
		for letter in self.name_lineEdit.text():
			c = unicode(letter.toUtf8(), encoding="UTF-8")
			if (not c.isdigit()) and c not in string.ascii_letters:
				return False
		return True

	def getFolder(self):
		dialog = QtGui.QFileDialog(self)
		dialog.setFileMode(QtGui.QFileDialog.Directory)
		dialog.setOption(QtGui.QFileDialog.ShowDirsOnly, True)

		if dialog.exec_():
			for d in dialog.selectedFiles():
				self.location_lineEdit.setText(d)
				#print d

	def closeEvent(self, evnt):
		if( self.retry ):
			self.mainWin = InitialWindow.Ui_Form()
			self.mainWin.show()
		else:
			self.mainWin = MainWindow.Ui_MainWindow()
			self.mainWin.projectDirectory = unicode(self.location_lineEdit.text().toUtf8(),encoding="UTF-8") + "/" + unicode(self.name_lineEdit.text().toUtf8(), encoding="UTF-8")
			self.mainWin.show()
			#print "Ha"

	def createErrorBox(self,notification):
		msg = QtGui.QMessageBox()
		msg.setIcon(QtGui.QMessageBox.Critical)

		msg.setText(notification)
		msg.setWindowTitle("Erro")
		msg.setStandardButtons(QtGui.QMessageBox.Ok)	
		retval = msg.exec_()	
