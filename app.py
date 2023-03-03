from sign_in import SignIn
from sign_up import SignUp
from main import MainWindow
from form import Form
from PyQt6.QtWidgets import QApplication
from sys import argv

if __name__ == "__main__":
    app = QApplication(argv)

    sign_in = SignIn()
    sign_in.show()

    sign_up = SignUp()

    main = MainWindow()

    form = Form()
    form.signal.main.connect(main.show)

    main.signal.form.connect(form.show)

    sign_in.signal.sign_up.connect(sign_up.show)
    sign_in.signal.main.connect(main.show)
    
    sign_up.signal.sign_in.connect(sign_in.show)
    sign_up.signal.main.connect(main.show)

    app.exec()