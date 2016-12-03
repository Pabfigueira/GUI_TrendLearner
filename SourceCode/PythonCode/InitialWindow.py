# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../QtDesignerCode/InitialWindow.ui'
#
# Created: Sat Dec  3 10:42:13 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import NewProjectWindow

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

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(312, 238)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.name_label = QtGui.QLabel(Form)
        self.name_label.setObjectName(_fromUtf8("name_label"))
        self.verticalLayout.addWidget(self.name_label)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.newProject_btn = QtGui.QPushButton(Form)
        self.newProject_btn.setObjectName(_fromUtf8("newProject_btn"))
        self.verticalLayout.addWidget(self.newProject_btn)
        self.openProject_btn = QtGui.QPushButton(Form)
        self.openProject_btn.setObjectName(_fromUtf8("openProject_btn"))
        self.verticalLayout.addWidget(self.openProject_btn)
        self.about_btn = QtGui.QPushButton(Form)
        self.about_btn.setObjectName(_fromUtf8("about_btn"))
        self.verticalLayout.addWidget(self.about_btn)
        self.exit_btn = QtGui.QPushButton(Form)
        self.exit_btn.setObjectName(_fromUtf8("exit_btn"))
        self.verticalLayout.addWidget(self.exit_btn)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Initial", None))
        self.name_label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">TrendLearnerApp</span></p></body></html>", None))
        self.newProject_btn.setText(_translate("Form", "New Project", None))
        self.openProject_btn.setText(_translate("Form", "Open Project", None))
        self.about_btn.setText(_translate("Form", "About TrendLearnerApp", None))
        self.exit_btn.setText(_translate("Form", "Exit", None))
        self.exit_btn.clicked.connect(self.closeWindow)
        self.newProject_btn.clicked.connect(self.openNewProjectWindow)
        self.openProject_btn.clicked.connect(self.getProject)

    def closeWindow(self):
        self.close()

    def openNewProjectWindow(self):
        self.newProjectWin = NewProjectWindow.Ui_NewProject()
        self.newProjectWin.show()
        self.close()

    def getProject(self):
        dialog = QtGui.QFileDialog(self)
        dialog.setFileMode(QtGui.QFileDialog.Directory)
        dialog.setOption(QtGui.QFileDialog.ShowDirsOnly, True)

        if dialog.exec_():
            for d in dialog.selectedFiles():
                print d

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())