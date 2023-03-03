from PyQt6.QtCore import QObject, pyqtSignal

class Signal(QObject):
    sign_in = pyqtSignal()
    sign_up = pyqtSignal()
    main = pyqtSignal()
    form = pyqtSignal()