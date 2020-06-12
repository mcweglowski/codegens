from PyQt5 import QtWidgets
from cgconsole.console_gui import main_window


def run():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_wnd = main_window.main_window()
    sys.exit(app.exec_())