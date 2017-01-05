# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../QtDesignerCode/MainInputWindow.ui'
#
# Created: Tue Jan  3 15:39:23 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import MainWindow

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

class Ui_Dialog(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)


	def setupUi(self, Dialog):
		Dialog.setObjectName(_fromUtf8("Dialog"))
		Dialog.resize(400, 300)
		self.verticalLayout = QtGui.QVBoxLayout(Dialog)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.label = QtGui.QLabel(Dialog)
		self.label.setObjectName(_fromUtf8("label"))
		self.horizontalLayout.addWidget(self.label)
		self.lineEdit = QtGui.QLineEdit(Dialog)
		self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
		self.horizontalLayout.addWidget(self.lineEdit)
		self.lineEdit.setReadOnly(True)
		self.pushButton = QtGui.QPushButton(Dialog)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.horizontalLayout.addWidget(self.pushButton)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.gridLayout_3 = QtGui.QGridLayout()
		self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
		self.spinBox = QtGui.QSpinBox(Dialog)
		self.spinBox.setObjectName(_fromUtf8("spinBox"))
		self.spinBox.setValue(80)
		self.gridLayout_3.addWidget(self.spinBox, 1, 2, 1, 1)
		self.radioButton = QtGui.QRadioButton(Dialog)
		self.radioButton.setObjectName(_fromUtf8("radioButton"))
		self.radioButton.setChecked(True)
		self.gridLayout_3.addWidget(self.radioButton, 0, 0, 1, 1)
		self.radioButton_2 = QtGui.QRadioButton(Dialog)
		self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
		self.gridLayout_3.addWidget(self.radioButton_2, 1, 0, 1, 1)
		self.label_2 = QtGui.QLabel(Dialog)
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.gridLayout_3.addWidget(self.label_2, 1, 1, 1, 1)
		self.label_3 = QtGui.QLabel(Dialog)
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.gridLayout_3.addWidget(self.label_3, 1, 3, 1, 1)
		self.verticalLayout.addLayout(self.gridLayout_3)
		self.buttonBox = QtGui.QDialogButtonBox(Dialog)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.verticalLayout.addWidget(self.buttonBox)

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(_translate("Dialog", "Input File", None))
		self.label.setText(_translate("Dialog", "File Directory", None))
		self.pushButton.setText(_translate("Dialog", "...", None))
		self.radioButton.setText(_translate("Dialog", "Random ", None))
		self.radioButton_2.setText(_translate("Dialog", "Sequential", None))
		self.label_2.setText(_translate("Dialog", "              Train", None))
		self.label_3.setText(_translate("Dialog", "%", None))
		self.buttonBox.button(QtGui.QDialogButtonBox.Cancel).clicked.connect(self.close)
		#self.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.checkOkButton)
		self.pushButton.clicked.connect(self.getFile)

	def getFile(self):
		dialog = QtGui.QFileDialog(self)
		dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
		dialog.setNameFilters(['TXT(*.txt)','CSV(*.csv)'])
		#dialog.setOption(QtGui.QFileDialog.ShowDirsOnly, True)

		if dialog.exec_():
			for d in dialog.selectedFiles():
				self.lineEdit.setText(d)
				#print d

	'''def checkOkButton(self):
		if not self.lineEdit.text().isEmpty():
			if self.radioButton.isChecked():
				# Fazer o CheckFile Aqui
				print "RAndom"
			elif self.radioButton_2.isChecked():
				# Fazer o CheckFile Aqui
				print "Sequential"
				print self.spinBox.value()
			else:
				sys.exit()
		else:
			self.createErrorBox('The operation can not be completed because the file directory is empty')

	def createErrorBox(self,notification):
		msg = QtGui.QMessageBox()
		msg.setIcon(QtGui.QMessageBox.Critical)

		msg.setText(notification)
		msg.setWindowTitle("Erro")
		msg.setStandardButtons(QtGui.QMessageBox.Ok)	
		retval = msg.exec_()'''


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	ex = Ui_Dialog()
	ex.show()
	sys.exit(app.exec_())
