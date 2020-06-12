from PyQt5.QtWidgets import QWidget


class main_window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interface()

    def interface(self):
        self.resize(300, 100)
        self.setWindowTitle("Simple calc")
        self.show()