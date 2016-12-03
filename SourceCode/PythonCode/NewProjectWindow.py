# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../QtDesignerCode/NewProjectWindow.ui'
#
# Created: Sat Dec  3 13:08:28 2016
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

class Ui_NewProject(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setupUi(self)

	def setupUi(self, NewProject):
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
		self.gridLayout.addWidget(self.location_lineEdit, 3, 0, 1, 1)
		self.name_lineEdit = QtGui.QLineEdit(NewProject)
		self.name_lineEdit.setObjectName(_fromUtf8("name_lineEdit"))
		self.gridLayout.addWidget(self.name_lineEdit, 1, 0, 1, 2)
		self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

		self.retranslateUi(NewProject)
		QtCore.QMetaObject.connectSlotsByName(NewProject)

	def retranslateUi(self, NewProject):
		NewProject.setWindowTitle(_translate("NewProject", "New Project", None))
		self.name_label.setText(_translate("NewProject", "Project Name:", None))
		self.browser_btn.setText(_translate("NewProject", "...", None))
		self.location_label.setText(_translate("NewProject", "Location:", None))
		#self.buttonBox.button(QtGui.QDialogButtonBox.Cancel).clicked.connect(self.printHi)

	

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_NewProject()
    ex.show()
    sys.exit(app.exec_())