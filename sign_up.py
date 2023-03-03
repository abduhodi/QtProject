from PyQt6 import QtCore, QtGui, QtWidgets
from style import button_style
from signals import Signal
import check
from query import Query
from user import User

class SignUp(QtWidgets.QMainWindow):
        def __init__(self) -> None:
                super().__init__()
                self.setupUi()
                self.signal = Signal()


        def setupUi(self):
                self.resize(375, 517)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
                self.setSizePolicy(sizePolicy)
                self.setMinimumSize(QtCore.QSize(375, 517))
                self.setMaximumSize(QtCore.QSize(375, 517))
                self.centralwidget = QtWidgets.QWidget(self)
                self.centralwidget.setObjectName("centralwidget")
                self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
                self.gridLayout.setObjectName("gridLayout")
                self.gridLayout_2 = QtWidgets.QGridLayout()
                self.gridLayout_2.setObjectName("gridLayout_2")
                self.name = QtWidgets.QLineEdit(parent=self.centralwidget)
                self.name.setMinimumSize(QtCore.QSize(300, 40))
                self.name.setMaximumSize(QtCore.QSize(300, 30))
                self.name.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
        "border-radius: 10px;")
                self.name.setObjectName("lineEdit")
                self.gridLayout_2.addWidget(self.name, 3, 0, 1, 1)
                spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
                self.gridLayout_2.addItem(spacerItem, 6, 0, 1, 1)
                spacerItem1 = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
                self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
                self.label = QtWidgets.QLabel(parent=self.centralwidget)
                self.label.setMinimumSize(QtCore.QSize(0, 40))
                self.label.setMaximumSize(QtCore.QSize(16777215, 60))
                self.label.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";")
                self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.label.setObjectName("label")
                self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
                spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
                self.gridLayout_2.addItem(spacerItem2, 4, 0, 1, 1)
                self.email = QtWidgets.QLineEdit(parent=self.centralwidget)
                self.email.setMinimumSize(QtCore.QSize(300, 40))
                self.email.setMaximumSize(QtCore.QSize(300, 30))
                self.email.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
        "border-radius: 10px;")
                self.email.setObjectName("lineEdit_2")
                self.gridLayout_2.addWidget(self.email, 5, 0, 1, 1)
                self.passwd = QtWidgets.QLineEdit(parent=self.centralwidget)
                self.passwd.setMinimumSize(QtCore.QSize(300, 40))
                self.passwd.setMaximumSize(QtCore.QSize(300, 30))
                self.passwd.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
        "border-radius: 10px;")
                self.passwd.setMaxLength(15)
                self.passwd.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
                self.passwd.setObjectName("lineEdit_3")
                self.gridLayout_2.addWidget(self.passwd, 7, 0, 1, 1)
                self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
                self.pushButton_2.setMinimumSize(QtCore.QSize(300, 40))
                self.pushButton_2.setMaximumSize(QtCore.QSize(300, 30))
                self.pushButton_2.setObjectName("pushButton_2")
                self.pushButton_2.setStyleSheet(button_style)
                self.gridLayout_2.addWidget(self.pushButton_2, 11, 0, 1, 1)
                self.checkBox = QtWidgets.QCheckBox(parent=self.centralwidget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
                self.checkBox.setSizePolicy(sizePolicy)
                self.checkBox.setMinimumSize(QtCore.QSize(300, 30))
                self.checkBox.setMaximumSize(QtCore.QSize(300, 30))
                self.checkBox.setSizeIncrement(QtCore.QSize(0, 0))
                self.checkBox.setBaseSize(QtCore.QSize(0, 0))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.checkBox.setFont(font)
                self.checkBox.setAutoFillBackground(False)
                self.checkBox.setStyleSheet("")
                self.checkBox.setIconSize(QtCore.QSize(30, 30))
                self.checkBox.setObjectName("checkBox")
                self.gridLayout_2.addWidget(self.checkBox, 8, 0, 1, 1)
                self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
                self.pushButton.setMinimumSize(QtCore.QSize(300, 40))
                self.pushButton.setMaximumSize(QtCore.QSize(300, 30))
                self.pushButton.setStyleSheet(button_style)
                self.pushButton.setObjectName("pushButton")
                self.gridLayout_2.addWidget(self.pushButton, 9, 0, 1, 1)
                spacerItem3 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
                self.gridLayout_2.addItem(spacerItem3, 10, 0, 1, 1)
                spacerItem4 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
                self.gridLayout_2.addItem(spacerItem4, 12, 0, 1, 1)
                spacerItem5 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
                self.gridLayout_2.addItem(spacerItem5, 2, 0, 1, 1)
                self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
                self.setCentralWidget(self.centralwidget)

                self.setWindowTitle("MainWindow")
                self.name.setPlaceholderText("username")
                self.label.setText("SIGN UP")
                self.email.setPlaceholderText("example@mail.ru")
                self.passwd.setPlaceholderText("**********")
                self.pushButton_2.setText("Back to Sign in")
                self.pushButton_2.clicked.connect(self.back_to_sign_in)
                self.checkBox.setText("I agree with terms and policy")
                self.pushButton.setText("Submit")
                self.pushButton.clicked.connect(self.submit)


        def back_to_sign_in(self):
                self.name.clear()
                self.email.clear()
                self.passwd.clear()
                self.signal.sign_in.emit()
                self.close()

        def submit(self):
                name = self.name.text()
                email = self.email.text()
                passwd = self.passwd.text()
                if not check.check_name(name):
                        self.message = QtWidgets.QMessageBox.critical(self, "Name error", "Name input error")
                elif not check.check_email(email):
                        self.message = QtWidgets.QMessageBox.critical(self, "Email error", "Email input error")
                elif not check.check_passwd(passwd):
                        self.message = QtWidgets.QMessageBox.critical(self, "Password error", "Password input error")
                elif not self.checkBox.isChecked():
                        self.message = QtWidgets.QMessageBox.critical(self, "Terms error", "You have to check terms and conditions")
                else:
                        if Query.register(name, email, passwd):
                                global newUser
                                newUser = User(name, email, passwd)
                                self.message = QtWidgets.QMessageBox.about(self, "Signed up", "Successfully signed up ")
                                self.name.clear()
                                self.email.clear()
                                self.passwd.clear()
                                self.checkBox.setChecked(False)
                                self.signal.main.emit()
                                self.close()
                        else:
                                self.message = QtWidgets.QMessageBox.critical(self, "Sign up error", "This email already exists")