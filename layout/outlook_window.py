# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'outlook_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Mailing Machine")
        MainWindow.resize(869, 897)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/miko5/Desktop/TDS/outlook/static/img/email_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.table_widget_data_from_data_frame = QtWidgets.QTableWidget(self.centralwidget)
        self.table_widget_data_from_data_frame.setMinimumSize(QtCore.QSize(0, 300))
        self.table_widget_data_from_data_frame.setMaximumSize(QtCore.QSize(850, 300))
        self.table_widget_data_from_data_frame.setObjectName("table_widget_data_from_data_frame")
        self.table_widget_data_from_data_frame.setColumnCount(0)
        self.table_widget_data_from_data_frame.setRowCount(0)
        self.gridLayout_6.addWidget(self.table_widget_data_from_data_frame, 0, 0, 1, 2)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_email.setObjectName("label_email")
        self.gridLayout_5.addWidget(self.label_email, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.fontComboBox = QtWidgets.QFontComboBox(self.centralwidget)
        self.fontComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fontComboBox.setObjectName("fontComboBox")
        self.gridLayout_5.addWidget(self.fontComboBox, 0, 3, 1, 1, QtCore.Qt.AlignTop)
        self.text_edit_email_body = QtWidgets.QTextEdit(self.centralwidget)
        self.text_edit_email_body.setObjectName("text_edit_email_body")
        self.gridLayout_5.addWidget(self.text_edit_email_body, 0, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 9, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 3, 1, 1)
        self.push_button_send = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_send.setMaximumSize(QtCore.QSize(70, 16777215))
        self.push_button_send.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_send.setObjectName("push_button_send")
        self.gridLayout_3.addWidget(self.push_button_send, 0, 1, 1, 1)
        self.push_button_test_send = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_test_send.setMaximumSize(QtCore.QSize(70, 16777215))
        self.push_button_test_send.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_test_send.setObjectName("push_button_test_send")
        self.gridLayout_3.addWidget(self.push_button_test_send, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 10, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.push_button_clean_list = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_clean_list.setMinimumSize(QtCore.QSize(100, 0))
        self.push_button_clean_list.setMaximumSize(QtCore.QSize(50, 16777215))
        self.push_button_clean_list.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_clean_list.setObjectName("push_button_clean_list")
        self.gridLayout.addWidget(self.push_button_clean_list, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.push_button_copy_selected = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_copy_selected.setMinimumSize(QtCore.QSize(100, 0))
        self.push_button_copy_selected.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_copy_selected.setObjectName("push_button_copy_selected")
        self.gridLayout.addWidget(self.push_button_copy_selected, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.push_button_add_variable = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_add_variable.setMinimumSize(QtCore.QSize(100, 0))
        self.push_button_add_variable.setMaximumSize(QtCore.QSize(50, 16777215))
        self.push_button_add_variable.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_add_variable.setObjectName("push_button_add_variable")
        self.gridLayout.addWidget(self.push_button_add_variable, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.push_button_remove_variable = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_remove_variable.setMinimumSize(QtCore.QSize(100, 0))
        self.push_button_remove_variable.setMaximumSize(QtCore.QSize(50, 16777215))
        self.push_button_remove_variable.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_remove_variable.setObjectName("push_button_remove_variable")
        self.gridLayout.addWidget(self.push_button_remove_variable, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.push_button_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_refresh.setMaximumSize(QtCore.QSize(150, 16777215))
        self.push_button_refresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_button_refresh.setObjectName("push_button_refresh")
        self.gridLayout.addWidget(self.push_button_refresh, 0, 0, 1, 1)
        self.push_button_change_separator = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_change_separator.setObjectName("push_button_change_separator")
        self.gridLayout.addWidget(self.push_button_change_separator, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        self.list_widget_columns = QtWidgets.QListWidget(self.centralwidget)
        self.list_widget_columns.setMaximumSize(QtCore.QSize(250, 16777215))
        self.list_widget_columns.setObjectName("list_widget_columns")
        self.gridLayout_2.addWidget(self.list_widget_columns, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.list_selected_variables = QtWidgets.QListWidget(self.centralwidget)
        self.list_selected_variables.setMaximumSize(QtCore.QSize(250, 16777215))
        self.list_selected_variables.setObjectName("list_selected_variables")
        self.gridLayout_2.addWidget(self.list_selected_variables, 1, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 5, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_subject = QtWidgets.QLabel(self.centralwidget)
        self.label_subject.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_subject.setObjectName("label_subject")
        self.gridLayout_4.addWidget(self.label_subject, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 3, 6, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 3, 2, 1, 1)
        self.label_addresses = QtWidgets.QLabel(self.centralwidget)
        self.label_addresses.setObjectName("label_addresses")
        self.gridLayout_4.addWidget(self.label_addresses, 1, 0, 1, 1)
        self.line_edit_subject = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_subject.setMaximumSize(QtCore.QSize(300, 16777215))
        self.line_edit_subject.setObjectName("line_edit_subject")
        self.gridLayout_4.addWidget(self.line_edit_subject, 3, 1, 1, 1)
        self.line_edit_addresses = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_addresses.setMaximumSize(QtCore.QSize(150, 16777215))
        self.line_edit_addresses.setObjectName("line_edit_addresses")
        self.gridLayout_4.addWidget(self.line_edit_addresses, 1, 1, 1, 1)
        self.push_button_copy_addresses = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_copy_addresses.setMaximumSize(QtCore.QSize(110, 16777215))
        self.push_button_copy_addresses.setObjectName("push_button_copy_addresses")
        self.gridLayout_4.addWidget(self.push_button_copy_addresses, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 7, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 869, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_data_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_data_file.setObjectName("actionOpen_data_file")
        self.menuFile.addAction(self.actionOpen_data_file)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Mailing Machine", "Mailing Machine"))
        self.label_email.setText(_translate("MainWindow", "Email body:"))
        self.push_button_send.setText(_translate("MainWindow", "Send "))
        self.push_button_test_send.setText(_translate("MainWindow", "Test send"))
        self.push_button_clean_list.setText(_translate("MainWindow", "Clean"))
        self.push_button_copy_selected.setText(_translate("MainWindow", "Copy selected"))
        self.push_button_add_variable.setText(_translate("MainWindow", "Add"))
        self.push_button_remove_variable.setText(_translate("MainWindow", "Remove"))
        self.push_button_refresh.setText(_translate("MainWindow", "Refresh list of columns"))
        self.push_button_change_separator.setText(_translate("MainWindow", "Change separator"))
        self.label.setText(_translate("MainWindow", "Columns"))
        self.label_2.setText(_translate("MainWindow", "Selected variables"))
        self.list_selected_variables.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_subject.setText(_translate("MainWindow", "Subject:"))
        self.label_addresses.setText(_translate("MainWindow", "Addresses:"))
        self.push_button_copy_addresses.setText(_translate("MainWindow", "Copy addresses"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_data_file.setText(_translate("MainWindow", "Open data file"))
        self.actionOpen_data_file.setShortcut(_translate("MainWindow", "Ctrl+N"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
