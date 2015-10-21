# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_task_form.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from sgtk.platform.qt import QtCore, QtGui

class Ui_NewTaskForm(object):
    def setupUi(self, NewTaskForm):
        NewTaskForm.setObjectName("NewTaskForm")
        NewTaskForm.resize(380, 270)
        NewTaskForm.setMinimumSize(QtCore.QSize(380, 270))
        self.verticalLayout = QtGui.QVBoxLayout(NewTaskForm)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtGui.QLabel(NewTaskForm)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.assigned_to = QtGui.QLabel(NewTaskForm)
        self.assigned_to.setObjectName("assigned_to")
        self.gridLayout.addWidget(self.assigned_to, 7, 2, 1, 1)
        self.label_6 = QtGui.QLabel(NewTaskForm)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.label_4 = QtGui.QLabel(NewTaskForm)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 1)
        self.pipeline_step = QtGui.QComboBox(NewTaskForm)
        self.pipeline_step.setObjectName("pipeline_step")
        self.gridLayout.addWidget(self.pipeline_step, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(10, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.entity = QtGui.QLabel(NewTaskForm)
        self.entity.setObjectName("entity")
        self.gridLayout.addWidget(self.entity, 8, 2, 1, 1)
        self.label = QtGui.QLabel(NewTaskForm)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(NewTaskForm)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.task_name = QtGui.QLineEdit(NewTaskForm)
        self.task_name.setObjectName("task_name")
        self.gridLayout.addWidget(self.task_name, 0, 2, 1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(20, 11, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.break_line = QtGui.QFrame(NewTaskForm)
        self.break_line.setFrameShape(QtGui.QFrame.HLine)
        self.break_line.setFrameShadow(QtGui.QFrame.Sunken)
        self.break_line.setObjectName("break_line")
        self.verticalLayout.addWidget(self.break_line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(12, 8, 12, 12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.cancel_btn = QtGui.QPushButton(NewTaskForm)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.create_btn = QtGui.QPushButton(NewTaskForm)
        self.create_btn.setDefault(True)
        self.create_btn.setObjectName("create_btn")
        self.horizontalLayout.addWidget(self.create_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(NewTaskForm)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL("clicked()"), NewTaskForm.close)
        QtCore.QMetaObject.connectSlotsByName(NewTaskForm)
        NewTaskForm.setTabOrder(self.task_name, self.pipeline_step)
        NewTaskForm.setTabOrder(self.pipeline_step, self.create_btn)
        NewTaskForm.setTabOrder(self.create_btn, self.cancel_btn)

    def retranslateUi(self, NewTaskForm):
        NewTaskForm.setWindowTitle(QtGui.QApplication.translate("NewTaskForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("NewTaskForm", "Create a new Task using the Name and Pipeline Step entered below.", None, QtGui.QApplication.UnicodeUTF8))
        self.assigned_to.setText(QtGui.QApplication.translate("NewTaskForm", "Mr John Smith", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("NewTaskForm", "Assigned to:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("NewTaskForm", "Entity:", None, QtGui.QApplication.UnicodeUTF8))
        self.entity.setText(QtGui.QApplication.translate("NewTaskForm", "Shot ABC 123", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NewTaskForm", "Pipeline Step:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("NewTaskForm", "Task Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("NewTaskForm", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.create_btn.setText(QtGui.QApplication.translate("NewTaskForm", "Create", None, QtGui.QApplication.UnicodeUTF8))

