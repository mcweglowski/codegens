from PyQt5 import QtWidgets


class main_window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interface()

    def interface(self):
        self.resize(300, 100)
        self.setWindowTitle("Simple calc")
        self.show()