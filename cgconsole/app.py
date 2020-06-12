from PyQt5.QtWidgets import QApplication
from cgconsole.console_gui import main_window


def run():
    import sys

    app = QApplication(sys.argv)
    okno = main_window.main_window()
    sys.exit(app.exec_())