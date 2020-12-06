from PyQt5 import QtWidgets
import sys
from DataBaseRequests import DBConnector
from Communicate import Communicate
from helper_form import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal, QObject, QSize, Qt, QSettings, QCoreApplication
import random
import threading


com = Communicate()


class helper_DB(QtWidgets.QMainWindow):
    def __init__(self, comunicate):
        print("Starting")
        super(helper_DB, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.commm = comunicate

        self.DB = DBConnector('213.59.135.187', 8080)
        self.int_table_clients()

        self.ui.btnConnect.clicked.connect(self.on_connect_button_click)
        self.ui.btnAdd.clicked.connect(self.on_add_button_click)
        self.ui.btnActivate.clicked.connect(self.on_activate_button)
        self.ui.btnDeactivate.clicked.connect(self.on_deactivate_button)
        self.ui.btnDelete.clicked.connect(self.on_delete_button)
        self.ui.btnChange.clicked.connect(self.on_change_button_click)

        # self.ui.tableWidget.cellClicked.connect(self.on_cell_click)
        self.ui.tableWidget.itemSelectionChanged.connect(self.on_cell_click)

        self.commm.addClient.connect(self.add_client_to_table)
        self.commm.deinitTable.connect(self.deinit_tables)
        self.commm.enableUI.connect(self.enable_ui)

        self.ui.groupBox.setEnabled(False)

    def activate(self):
        clients = self.DB.getClients()
        for cl in clients:
            ID = cl['bins']['ID']
            self.DB.activateClient(ID)
        self.deinit_tables()
        self.on_connect_button_click()

    def on_activate_button(self):
        self.disable_ui()
        thread_act = threading.Thread(target=self.activate, args=())
        thread_act.setDaemon(True)
        thread_act.start()

    def on_delete_button(self):
        self.disable_ui()
        thread_del = threading.Thread(target=self.delete, args=())
        thread_del.setDaemon(True)
        thread_del.start()

    def delete(self):
        self.DB.deleteAllClients()
        self.on_connect_button_click()

    def deactivate(self):
        clients = self.DB.getClients()
        for cl in clients:
            ID = cl['bins']['ID']
            self.DB.deactivateClient(ID)
        self.deinit_tables()
        self.on_connect_button_click()

    def on_deactivate_button(self):
        self.disable_ui()
        thread_deact = threading.Thread(target=self.deactivate, args=())
        thread_deact.setDaemon(True)
        thread_deact.start()

    def add(self):
        try:
            count = self.ui.spBxCount.value()
            self.commm.deinitTable.emit()
            # self.deinit_tables()
            self.DB.deleteAllClients()
            st = self.ui.dspBxStart.value()
            end = self.ui.dspBxEnd.value()
            for i in range(1, count+1):
                print("curr ID", i)
                bins = {
                    'ID': i,
                    'Instrument': "QGCG21",
                    'Diff_long': round(random.uniform(st, end), 1),  # 0.3,
                    'Diff_short': -round(random.uniform(st, end), 1),  # 0.3,
                    'Logic': 1,
                    'Delay': 0,
                    'Active': 1,
                    'Flag': 0,
                    'Change_fl': 1,
                    'Stop_on_execute': 1,
                    "IP": "666.777.888.999"
                }
                print(bins)
                self.DB.setClient(i, bins)

            self.on_connect_button_click()
            # self.commm.enableUI.emit()
        except Exception as e:
            print("add_button", e)

    def on_add_button_click(self):
        self.disable_ui()
        thread_add = threading.Thread(target=self.add, args=())
        thread_add.setDaemon(True)
        thread_add.start()

    def disable_ui(self):
        self.ui.tableWidget.setEnabled(False)
        self.ui.btnDeactivate.setEnabled(False)
        self.ui.btnActivate.setEnabled(False)
        self.ui.btnAdd.setEnabled(False)
        self.ui.btnConnect.setEnabled(False)
        self.ui.btnDelete.setEnabled(False)

    def enable_ui(self):
        self.ui.tableWidget.setEnabled(True)
        self.ui.btnDeactivate.setEnabled(True)
        self.ui.btnActivate.setEnabled(True)
        self.ui.btnAdd.setEnabled(True)
        self.ui.btnConnect.setEnabled(True)
        self.ui.btnDelete.setEnabled(True)

    def connect(self):
        clients = self.DB.getClients()
        i = 0
        for cl in clients:
            client = cl['bins']
            self.ui.tableWidget.insertRow(i)
            # self.add_client_to_table(client, i)
            self.commm.addClient.emit(client, i)
            i = i + 1
        self.commm.enableUI.emit()

    def on_connect_button_click(self):
        self.disable_ui()
        thread_connect = threading.Thread(target=self.connect, args=())
        thread_connect.setDaemon(True)
        thread_connect.start()

    def int_table_clients(self):
        """
        Initialisation of client table
        :return:
        """
        headers = ["ID", "Instrument", "Diff long", "Diff short", "Logic (Str/Rev)", "Delay", "Active", "Flag", "Stop",
                   "IP"]
        count = len(headers)
        self.ui.tableWidget.setColumnCount(count)
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)
        for i in range(count):
            self.ui.tableWidget.horizontalHeaderItem(i).setTextAlignment(Qt.AlignHCenter)
        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.setColumnWidth(2, 70)
        self.ui.tableWidget.setColumnWidth(3, 70)
        self.ui.tableWidget.setColumnWidth(5, 50)
        self.ui.tableWidget.setColumnWidth(6, 50)
        self.ui.tableWidget.setColumnWidth(7, 50)

    def deinit_tables(self):
        """
        Function removes all clients from client table
        :return:
        """
        rows = self.ui.tableWidget.rowCount()
        for i in range(rows):
            self.ui.tableWidget.removeRow(0)

    def add_client_to_table(self, client, row):
        """
        Function adds client to table on form
        :param client: dict that contains info about client
        :param row: number of row for client
        :return: none
        """
        item = QtWidgets.QTableWidgetItem(str(client['ID']))
        self.ui.tableWidget.setItem(row, 0, item)
        print('client', client, row)

        item = QtWidgets.QTableWidgetItem(client['Instrument'])
        self.ui.tableWidget.setItem(row, 1, item)

        item = QtWidgets.QTableWidgetItem(str(client['Diff_long']))
        self.ui.tableWidget.setItem(row, 2, item)

        item = QtWidgets.QTableWidgetItem(str(client['Diff_short']))
        self.ui.tableWidget.setItem(row, 3, item)

        item = QtWidgets.QTableWidgetItem(str(client['Logic']))
        self.ui.tableWidget.setItem(row, 4, item)

        item = QtWidgets.QTableWidgetItem(str(client['Delay']))
        self.ui.tableWidget.setItem(row, 5, item)

        item = QtWidgets.QTableWidgetItem(str(client['Active']))
        self.ui.tableWidget.setItem(row, 6, item)

        item = QtWidgets.QTableWidgetItem(str(client['Flag']))
        self.ui.tableWidget.setItem(row, 7, item)

        item = QtWidgets.QTableWidgetItem(str(client['Stop_on_execute']))
        self.ui.tableWidget.setItem(row, 8, item)

        item = QtWidgets.QTableWidgetItem(str(client['IP']))
        self.ui.tableWidget.setItem(row, 9, item)

        self.ui.tableWidget.update()
        self.ui.tableWidget.activateWindow()

        com.setMessage("Client " + str(client['ID']) + " was changed")
        com.newMessage.emit()

    def change(self):
        selected_items = self.ui.tableWidget.selectedItems()
        if len(selected_items) == 0:
            return
        # print(row, col)
        ID = int(self.ui.sBxID.value())
        Instrument = self.ui.leInstrument.text()
        Buy = self.ui.dsBxBuy.value()
        Sell = self.ui.dsBxSell.value()
        Logic = self.ui.chBxLogic.isChecked()
        Delay = self.ui.sBxDelay.value()
        Active = self.ui.chBxActive.isChecked()
        Stop = self.ui.chBxStop.isChecked()
        IP = self.ui.leIP.text()

        bins = {
            'ID': ID,
            'Instrument': Instrument,
            'Diff_long': Buy,
            'Diff_short': Sell,
            'Logic': Logic,
            'Delay': Delay,
            'Active': Active,
            'Flag': 0,
            'Change_fl': 1,
            'Stop_on_execute': Stop,
            "IP": IP
        }
        print(bins)
        ch = self.DB.editClient(ID, bins)
        print("ch is", ch)
        self.on_connect_button_click()

    def on_change_button_click(self):
        self.disable_ui()
        self.ui.groupBox.setEnabled(False)
        thread_change = threading.Thread(target=self.change, args=())
        thread_change.setDaemon(True)
        thread_change.start()

    def on_cell_click(self):
        selected_items = self.ui.tableWidget.selectedItems()
        if len(selected_items) == 0:
            return
        # print(row, col)
        ID = int(selected_items[0].text())
        Instrument = selected_items[1].text()
        Buy = float(selected_items[2].text())
        Sell = float(selected_items[3].text())
        Logic = int(selected_items[4].text())
        Delay = int(selected_items[5].text())
        Active = int(selected_items[6].text())
        Flag = bool(selected_items[7].text())
        Stop = int(selected_items[8].text())
        IP = selected_items[9].text()

        if Logic == 0:
            Logic = False
        else:
            Logic = True

        if Active == 0:
            Active = False
        else:
            Active = True

        if Stop == 0:
            Stop = False
        else:
            Stop = True
        print("bool", Logic, Active, Stop)

        self.ui.sBxID.setValue(ID)
        self.ui.leInstrument.setText(Instrument)
        self.ui.dsBxBuy.setValue(Buy)
        self.ui.dsBxSell.setValue(Sell)
        self.ui.chBxLogic.setChecked(Logic)
        self.ui.sBxDelay.setValue(Delay)
        self.ui.chBxActive.setChecked(Active)
        self.ui.chBxStop.setChecked(Stop)
        self.ui.leIP.setText(IP)
        self.ui.groupBox.setEnabled(True)

app = QtWidgets.QApplication([])
application = helper_DB(com)
application.show()

sys.exit(app.exec())