from PyQt5.QtCore import pyqtSignal, QObject


class Communicate(QObject):
    newMessage = pyqtSignal()
    newPrice = pyqtSignal()
    buySignal = pyqtSignal()
    sellSignal = pyqtSignal()
    newClient = pyqtSignal()
    newSignal = pyqtSignal()
    updateBuyCount = pyqtSignal()
    updateSellCount = pyqtSignal()
    addClient = pyqtSignal(dict, int)
    deinitTable = pyqtSignal()
    enableUI = pyqtSignal()
    disableUI = pyqtSignal()

    def setMessage(self, mes):
        self.message = mes
        # ('-------setMess----------')
        # print(com.message)

    def setBuyMess(self, mes):
        self.BuyMess = mes

    def setSellMess(self, mes):
        self.SellMess = mes

    def setPrice(self, mes):
        self.price = mes

    def setVolume(self, mes):
        self.volume = mes

    def setTime(self, mes):
        self.time = mes

    def setClient(self, mes):
        self.client = mes

    def setFlag(self, mes):
        self.flag = mes

    def setBuyCount(self, count):
        self.buyCount = count

    def setSellCount(self, count):
        self.sellCount = count
