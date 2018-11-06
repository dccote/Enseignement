from PyQt5.QtWidgets import QMainWindow
from labJackStream.streamLabJack import StreamLabJack
from labJackStream.interface.mainWindowUi import Ui_streamWindow


class MainWindow(QMainWindow, Ui_streamWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.stream = StreamLabJack(self.streamMpl.canvas)
        self.buttonMain.clicked.connect(self.startStreamGraph)

    def startStreamGraph(self):
        self.stream.startStream()

        self.buttonMain.clicked.disconnect()
        self.buttonMain.setText("Stop")
        self.buttonMain.clicked.connect(self.stream.stopStream)
