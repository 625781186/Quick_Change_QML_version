# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(316, 172)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.TextLabel1 = QtWidgets.QLabel(Form)
        self.TextLabel1.setObjectName("TextLabel1")
        self.gridLayout_2.addWidget(self.TextLabel1, 0, 0, 1, 1)
        self.findtextCombo = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.findtextCombo.sizePolicy().hasHeightForWidth())
        self.findtextCombo.setSizePolicy(sizePolicy)
        self.findtextCombo.setEditable(True)
        self.findtextCombo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.findtextCombo.setDuplicatesEnabled(False)
        self.findtextCombo.setObjectName("findtextCombo")
        self.gridLayout_2.addWidget(self.findtextCombo, 0, 1, 1, 1)
        self.replaceLabel = QtWidgets.QLabel(Form)
        self.replaceLabel.setObjectName("replaceLabel")
        self.gridLayout_2.addWidget(self.replaceLabel, 1, 0, 1, 1)
        self.replacetextCombo = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.replacetextCombo.sizePolicy().hasHeightForWidth())
        self.replacetextCombo.setSizePolicy(sizePolicy)
        self.replacetextCombo.setEditable(True)
        self.replacetextCombo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.replacetextCombo.setDuplicatesEnabled(False)
        self.replacetextCombo.setObjectName("replacetextCombo")
        self.gridLayout_2.addWidget(self.replacetextCombo, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.filterCheckBox = QtWidgets.QCheckBox(Form)
        self.filterCheckBox.setEnabled(False)
        self.filterCheckBox.setChecked(True)
        self.filterCheckBox.setObjectName("filterCheckBox")
        self.gridLayout.addWidget(self.filterCheckBox, 2, 0, 1, 1)
        self.regexpCheckBox = QtWidgets.QCheckBox(Form)
        self.regexpCheckBox.setObjectName("regexpCheckBox")
        self.gridLayout.addWidget(self.regexpCheckBox, 0, 1, 1, 1)
        self.filterEdit = QtWidgets.QLineEdit(Form)
        self.filterEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterEdit.sizePolicy().hasHeightForWidth())
        self.filterEdit.setSizePolicy(sizePolicy)
        self.filterEdit.setObjectName("filterEdit")
        self.gridLayout.addWidget(self.filterEdit, 2, 1, 1, 1)
        self.feelLikeCheckBox = QtWidgets.QCheckBox(Form)
        self.feelLikeCheckBox.setObjectName("feelLikeCheckBox")
        self.gridLayout.addWidget(self.feelLikeCheckBox, 1, 1, 1, 1)
        self.caseCheckBox = QtWidgets.QCheckBox(Form)
        self.caseCheckBox.setObjectName("caseCheckBox")
        self.gridLayout.addWidget(self.caseCheckBox, 0, 0, 1, 1)
        self.wordCheckBox = QtWidgets.QCheckBox(Form)
        self.wordCheckBox.setObjectName("wordCheckBox")
        self.gridLayout.addWidget(self.wordCheckBox, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn3 = QtWidgets.QPushButton(Form)
        self.btn3.setObjectName("btn3")
        self.gridLayout_3.addWidget(self.btn3, 0, 2, 1, 1)
        self.btn1 = QtWidgets.QPushButton(Form)
        self.btn1.setObjectName("btn1")
        self.gridLayout_3.addWidget(self.btn1, 0, 0, 1, 1)
        self.btn2 = QtWidgets.QPushButton(Form)
        self.btn2.setObjectName("btn2")
        self.gridLayout_3.addWidget(self.btn2, 0, 1, 1, 1)
        self.btn4 = QtWidgets.QPushButton(Form)
        self.btn4.setObjectName("btn4")
        self.gridLayout_3.addWidget(self.btn4, 1, 0, 1, 1)
        self.btn5 = QtWidgets.QPushButton(Form)
        self.btn5.setObjectName("btn5")
        self.gridLayout_3.addWidget(self.btn5, 1, 1, 1, 1)
        self.btn6 = QtWidgets.QPushButton(Form)
        self.btn6.setObjectName("btn6")
        self.gridLayout_3.addWidget(self.btn6, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.TextLabel1.setText(_translate("Form", "Find text:"))
        self.findtextCombo.setToolTip(_translate("Form", "Enter the search text or regular expression"))
        self.replaceLabel.setText(_translate("Form", "Replace text:"))
        self.replacetextCombo.setToolTip(_translate("Form", "Enter the replacement text or regular expression"))
        self.filterCheckBox.setToolTip(_translate("Form", "Select to filter the files by a given filename pattern"))
        self.filterCheckBox.setText(_translate("Form", "Filter(format:*.qml;*.py)"))
        self.regexpCheckBox.setToolTip(_translate("Form", "Select if the searchtext is a regular expression"))
        self.regexpCheckBox.setText(_translate("Form", "&Regular Expression"))
        self.filterEdit.setToolTip(_translate("Form", "Enter the filename wildcards separated by \';\'"))
        self.filterEdit.setText(_translate("Form", "*.qml"))
        self.feelLikeCheckBox.setToolTip(_translate("Form", "Select to open the first occurence automatically"))
        self.feelLikeCheckBox.setText(_translate("Form", "Feeling Like"))
        self.caseCheckBox.setToolTip(_translate("Form", "Select to match case sensitive"))
        self.caseCheckBox.setText(_translate("Form", "&Match upper/lower case"))
        self.wordCheckBox.setToolTip(_translate("Form", "Select to match whole words only"))
        self.wordCheckBox.setText(_translate("Form", "&Whole word"))
        self.btn3.setText(_translate("Form", "PushButton"))
        self.btn1.setText(_translate("Form", "QtQuick 2.*"))
        self.btn2.setText(_translate("Form", "Controls 2.*"))
        self.btn4.setText(_translate("Form", "PushButton"))
        self.btn5.setText(_translate("Form", "PushButton"))
        self.btn6.setText(_translate("Form", "PushButton"))
