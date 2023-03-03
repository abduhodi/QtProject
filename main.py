from PyQt6 import QtCore, QtGui, QtWidgets
import requests
from query import Query
from signals import Signal
# from sign_in import user1




class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi()
        self.signal = Signal()


    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(657, 515)
        self.setMinimumSize(QtCore.QSize(657, 515))
        self.setMaximumSize(QtCore.QSize(657, 515))
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 661, 501))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.category_list = QtWidgets.QListWidget(parent=self.frame)
        self.category_list.setGeometry(QtCore.QRect(20, 120, 221, 141))
        self.category_list.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.category_list.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.category_list.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.category_list.setObjectName("category_list")
        item = QtWidgets.QListWidgetItem()
        self.category_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.category_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.category_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.category_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.category_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.category_list.addItem(item)
        self.logo = QtWidgets.QLabel(parent=self.frame)
        self.logo.setGeometry(QtCore.QRect(20, 20, 111, 31))
        self.logo.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.logo.setObjectName("logo")
        self.category_label = QtWidgets.QLabel(parent=self.frame)
        self.category_label.setGeometry(QtCore.QRect(20, 70, 111, 31))
        self.category_label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.category_label.setObjectName("category_label")
        self.search_field = QtWidgets.QLineEdit(parent=self.frame)
        self.search_field.setGeometry(QtCore.QRect(160, 20, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.search_field.setFont(font)
        self.search_field.setStyleSheet("border-radius: 15px;\n"
"border: 1px solid black;")
        self.search_field.setCursorPosition(0)
        self.search_field.setObjectName("search_field")
        self.Cart_logo = QtWidgets.QLabel(parent=self.frame)
        self.Cart_logo.setGeometry(QtCore.QRect(590, 20, 31, 31))
        self.Cart_logo.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Cart_logo.setText("")

        self.Cart_logo.setPixmap(QtGui.QPixmap("img/shopping-cart.png"))
        self.Cart_logo.setScaledContents(True)
        self.Cart_logo.setObjectName("Cart_logo")
        self.user_logo = QtWidgets.QLabel(parent=self.frame)
        self.user_logo.setGeometry(QtCore.QRect(530, 20, 31, 31))
        self.user_logo.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.user_logo.setText("")
        self.user_logo.setPixmap(QtGui.QPixmap("img/user.png"))
        self.user_logo.setScaledContents(True)
        self.user_logo.setObjectName("user_logo")
        self.cart_label = QtWidgets.QLabel(parent=self.frame)
        self.cart_label.setGeometry(QtCore.QRect(594, 50, 41, 16))
        self.cart_label.setObjectName("cart_label")
        self.username_label = QtWidgets.QLabel(parent=self.frame)
        self.username_label.setGeometry(QtCore.QRect(510, 50, 71, 16))
        self.username_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(250, 80, 391, 311))
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")


        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(625, 20, 25, 16))
        self.label.setStyleSheet("font: 500 8pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.setCentralWidget(self.centralwidget)


        QtCore.QMetaObject.connectSlotsByName(self)

        self.category_list.setSortingEnabled(False)
        item = self.category_list.item(0)
        item.setText("Products")
        item = self.category_list.item(1)
        item.setText("Computers and Office")
        item = self.category_list.item(2)
        item.setText("Electronics")
        item = self.category_list.item(3)
        item.setText("Mobile phone and accessories")
        item = self.category_list.item(4)
        item.setText("Watches")
        item = self.category_list.item(5)
        item.setText("Shoes")
        self.logo.setText("AliExpress")
        self.category_label.setText("Categories>")
        self.search_field.setPlaceholderText(" I\'m looking for...")
        self.cart_label.setText("Basket")

        self.username_label.setText("username")
        # self.username_label.setText(user1.username)
        self.label.setText("0")
        # self.category_list.setCurrentRow(0)
        self.category_list.currentRowChanged.connect(self.change_category)

    def show_items(self, category:str):
        data = []
        data = Query.get_data(category)
        print(data)
        if data:
            self.next_btn = QtWidgets.QPushButton('', parent=self)
            self.next_btn.show()
            self.next_btn.setStyleSheet("background-color: transparent;")
            self.next_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            self.next_btn.setIcon(QtGui.QIcon(QtGui.QPixmap("img/next.png")))
            self.next_btn.setGeometry(QtCore.QRect(450, 380, 20, 20))
            self.next_btn.clicked.connect(self.next_item)

            self.previous_btn = QtWidgets.QPushButton('', parent=self)
            self.previous_btn.show()
            self.previous_btn.setStyleSheet("background-color: transparent;")
            self.previous_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            self.previous_btn.setIcon(QtGui.QIcon(QtGui.QPixmap("img/previous.png")))
            self.previous_btn.setGeometry(QtCore.QRect(400, 380, 20, 20))
            self.previous_btn.clicked.connect(self.previous_item)

            for dat in data:
                self.page = QtWidgets.QWidget()
                self.page.setStyleSheet("background-color: rgb(255, 255, 255);")
                
                self.image = QtWidgets.QLabel(parent=self.page)
                self.image.setGeometry(QtCore.QRect(0, 80, 200, 200))
                self.image.setAutoFillBackground(False)
                self.image.setText("")
                self.image.setTextFormat(QtCore.Qt.TextFormat.AutoText)
                image = QtGui.QImage()
                image.loadFromData(requests.get(dat[2]).content)
                self.image.setPixmap(QtGui.QPixmap(image))
                self.image.setScaledContents(True)
                self.image.setWordWrap(False)
                self.image.setOpenExternalLinks(False)
                self.image.setObjectName("image")

                self.price = QtWidgets.QLabel(parent=self.page)
                self.price.setGeometry(QtCore.QRect(230, 80, 141, 41))
                self.price.setStyleSheet("font: 500 16pt \"MS Shell Dlg 2\";\n"
        "color: rgb(0, 0, 0);")
                self.price.setObjectName("price")
                self.price.setText(f"USD {dat[1]}")

                self.label_9 = QtWidgets.QLabel(parent=self.page)
                self.label_9.setGeometry(QtCore.QRect(230, 120, 141, 16))
                self.label_9.setStyleSheet("color: rgb(0, 170, 0);")
                self.label_9.setObjectName("label_9")

                self.deliverydate = QtWidgets.QLabel(parent=self.page)
                self.deliverydate.setGeometry(QtCore.QRect(230, 150, 161, 30))

                font = QtGui.QFont()
                font.setPointSize(8)
                self.deliverydate.setFont(font)
                self.deliverydate.setObjectName("deliverydate")

                self.addToCartBtn = QtWidgets.QPushButton(parent=self.page)
                self.addToCartBtn.setGeometry(QtCore.QRect(230, 190, 110, 35))
                self.addToCartBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                self.addToCartBtn.setStyleSheet("background-color: rgb(34,34,34);\n"
        "color: rgb(255, 255, 255);\n"
        "font: 600 10pt \"MS Shell Dlg 2\";\n"
        "border-radius: 16px;")
                self.addToCartBtn.setObjectName("addToCartBtn")
                self.addToCartBtn.clicked.connect(self.add_cart)

                self.buyNowBtn = QtWidgets.QPushButton(parent=self.page)
                self.buyNowBtn.setGeometry(QtCore.QRect(230, 240, 110, 35))

                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(10)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)

                self.buyNowBtn.setFont(font)
                self.buyNowBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                self.buyNowBtn.setStyleSheet("background-color: rgb(204,41,10);\n"
        "color: rgb(255, 255, 255);\n"
        "font: 600 10pt \"MS Shell Dlg 2\";\n"
        "border-radius: 16px;")
                self.buyNowBtn.setObjectName("butNowBtn")

                self.likeLabel = QtWidgets.QLabel(parent=self.page)
                self.likeLabel.setGeometry(QtCore.QRect(350, 220, 30, 30))
                self.likeLabel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                self.likeLabel.setText("")
                # self.likeLabel.setStyleSheet("background-color: transparent;")
                self.likeLabel.setPixmap(QtGui.QPixmap("img/heart-full.png"))
                self.likeLabel.setScaledContents(True)
                self.likeLabel.setObjectName("likeLabel")
                # self.likeLabel.clicked.connect(self.like_btn)

                self.description = QtWidgets.QLabel(parent=self.page)
                self.description.setGeometry(QtCore.QRect(10, 10, 341, 51))
                self.description.setStyleSheet("font: 200 14pt \"MS Shell Dlg 2\";")
                self.description.setObjectName("description")
                self.description.setText(dat[0])

                self.label_9.setText("There is free shipping")
                self.deliverydate.setText("Delivery by Mail 09 Apr")
                self.addToCartBtn.setText("Add to Cart")
                self.buyNowBtn.setText("Buy now")
                self.buyNowBtn.clicked.connect(self.form)



                self.stackedWidget.addWidget(self.page)
            
            self.currentIndex = 0
            self.stackedWidget.setCurrentIndex(self.currentIndex)

    def form(self):
        self.signal.form.emit()
              
        
    def next_item(self):
        self.currentIndex += 1
        if self.currentIndex == self.stackedWidget.count():
            self.currentIndex = 0
        self.stackedWidget.setCurrentIndex(self.currentIndex)
        print(self.currentIndex)

    def previous_item(self):
        self.currentIndex -= 1
        if self.currentIndex < 0:
            self.currentIndex = self.stackedWidget.count() - 1
        self.stackedWidget.setCurrentIndex(self.currentIndex)
        print(self.currentIndex)

    def change_category(self):
        category = self.category_list.currentItem().text()
        while self.stackedWidget.count():
            self.stackedWidget.setCurrentIndex(0)
            widget = self.stackedWidget.currentWidget()
            self.stackedWidget.removeWidget(widget)
        self.show_items(category)
        print(category)


    def add_cart(self):
        cnt = int(self.label.text())
        cnt += 1
        self.label.setText(str(cnt))

    def like_btn(self):
        self.likeLabel.setIcon(QtGui.QIcon("img/heart-full.png"))
        print("clicked")


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     ui = MainWindow()
#     ui.show()
#     sys.exit(app.exec())
