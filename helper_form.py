# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helper_form.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btnDeactivate = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeactivate.setObjectName("btnDeactivate")
        self.gridLayout.addWidget(self.btnDeactivate, 2, 8, 1, 1)
        self.btnConnect = QtWidgets.QPushButton(self.centralwidget)
        self.btnConnect.setObjectName("btnConnect")
        self.gridLayout.addWidget(self.btnConnect, 1, 0, 1, 10)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 4, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 10)
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setObjectName("btnAdd")
        self.gridLayout.addWidget(self.btnAdd, 2, 6, 1, 1)
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setObjectName("btnDelete")
        self.gridLayout.addWidget(self.btnDelete, 2, 9, 1, 1)
        self.btnActivate = QtWidgets.QPushButton(self.centralwidget)
        self.btnActivate.setObjectName("btnActivate")
        self.gridLayout.addWidget(self.btnActivate, 2, 7, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.spBxCount = QtWidgets.QSpinBox(self.centralwidget)
        self.spBxCount.setMaximum(999999)
        self.spBxCount.setProperty("value", 50)
        self.spBxCount.setObjectName("spBxCount")
        self.gridLayout.addWidget(self.spBxCount, 2, 1, 1, 1)
        self.dspBxStart = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dspBxStart.setMaximum(9999.99)
        self.dspBxStart.setSingleStep(0.1)
        self.dspBxStart.setProperty("value", 0.1)
        self.dspBxStart.setObjectName("dspBxStart")
        self.gridLayout.addWidget(self.dspBxStart, 2, 3, 1, 1)
        self.dspBxEnd = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dspBxEnd.setMaximum(9999.99)
        self.dspBxEnd.setSingleStep(0.1)
        self.dspBxEnd.setProperty("value", 1.0)
        self.dspBxEnd.setObjectName("dspBxEnd")
        self.gridLayout.addWidget(self.dspBxEnd, 2, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Database helper 3000"))
        self.btnDeactivate.setText(_translate("MainWindow", "Deactivate"))
        self.btnConnect.setText(_translate("MainWindow", "Connect"))
        self.label_3.setText(_translate("MainWindow", "End"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.btnActivate.setText(_translate("MainWindow", "Activate"))
        self.label.setText(_translate("MainWindow", "Count"))
        self.label_2.setText(_translate("MainWindow", "Start"))
