import sys
import can
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

class BUS_configure(QObject):
    dataChanged = pyqtSignal(int)
    nextNumber = pyqtSignal(int)
    
    def __init__(self):
        QObject.__init__(self)

    
    @pyqtSlot()
    def getBUS_configuration(self):
            bus_Obj = senderW.findChild(QObject, "bustype_in")
            ch_Obj = senderW.findChild(QObject, "channel_in")
            bit_Obj = senderW.findChild(QObject, "bitrate_in")
            bustype = bus_Obj.property("currentText")
            channel = ch_Obj.property("currentText")
            bitrate = int(bit_Obj.property("text"))
            bus = can.interface.Bus(bustype=bustype, channel=channel, bitrate=bitrate)
            print("THE BUS HAS BEEN INITIATED")
            print("bustype=",bustype,"\nchannel=",channel,"\nbitrate=",bitrate)
        

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    
    bus_configure = BUS_configure()
    engine.rootContext().setContextProperty("busconfigure", bus_configure)
    
    engine.load("bus_configuration.qml")
    senderW = engine.rootObjects()[0]
    
    if not engine.rootObjects():
        sys.exit(-1)    
    
    sys.exit(app.exec_())