from PyQt6 import QtCore, QtGui, QtWidgets
from style import button_style
from signals import Signal
from query import Query
from sign_up import User

class SignIn(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi()
        self.signal = Signal()

    def setupUi(self):
        self.resize(375, 475)
        self.setMinimumSize(QtCore.QSize(375, 475))
        self.setMaximumSize(QtCore.QSize(375, 475))

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")

        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 26, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.email = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.email.setMinimumSize(QtCore.QSize(300, 30))
        self.email.setMaximumSize(QtCore.QSize(300, 30))
        self.email.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;")
        self.email.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.email, 3, 0, 1, 1)

        self.passwd = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.passwd.setMinimumSize(QtCore.QSize(300, 30))
        self.passwd.setMaximumSize(QtCore.QSize(300, 30))
        self.passwd.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;")
        self.passwd.setMaxLength(15)
        self.passwd.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.passwd.setObjectName("lineEdit_3")

        self.gridLayout_2.addWidget(self.passwd, 5, 0, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(300, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(300, 30))

        font = QtGui.QFont()
        font.setPointSize(14)

        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(button_style)
        self.pushButton_2.setObjectName("pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 9, 0, 1, 1)

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(300, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(300, 30))

        font = QtGui.QFont()
        font.setPointSize(14)

        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(button_style)
        self.pushButton.setObjectName("pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 7, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 6, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem3, 8, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem4, 10, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem5, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.setWindowTitle("Sign in")
        self.label.setText("SIGN IN")
        self.email.setPlaceholderText("example@mail.ru")
        self.passwd.setPlaceholderText("**********")
        self.pushButton_2.setText("Sign up")
        self.pushButton_2.clicked.connect(self.goto_sign_up)

        self.pushButton.setText("Log in")
        self.pushButton.clicked.connect(self.submit)

    def goto_sign_up(self):
        self.email.clear()
        self.passwd.clear()
        self.signal.sign_up.emit()
        self.close()

    def submit(self):
        email = self.email.text()
        passwd = self.passwd.text()
        res = Query.sign_in(email, passwd)
        if res:
            user1 = User(res[0][0], res[0][1], res[0][2])
            self.message = QtWidgets.QMessageBox.about(self, "Signed in", "You are signed in")
            self.email.clear()
            self.passwd.clear()
            self.signal.main.emit()
            self.close()
            print(res)
        else:
            self.message = QtWidgets.QMessageBox.critical(self, "Signed in error", "email or password is incorrect")
            print(res)
