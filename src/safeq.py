import string
import random
import base64
from login import Ui_LoginWindow
from app import Ui_MainWindow
from account import Ui_Dialog
from notification import Ui_Dialog as Notification
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QPropertyAnimation, QEvent
from PyQt5.QtWidgets import QListWidgetItem
from cryptography.fernet import Fernet
import sys
import mysql.connector
from datetime import date
from PyQt5.QtGui import QCursor
from pbkdf2 import crypt
import os
from inspect import getsourcefile
from os.path import abspath


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    auth_plugin="mysql_native_password",
    database="safeq"
)


main_window = None
nick = None
key = None

cursor = db.cursor(buffered=True)
cursor.execute("CREATE TABLE if not exists users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), salt VARCHAR(255), last_login VARCHAR(255))")

launch_path = abspath(getsourcefile(lambda: 0))
project_path = os.path.dirname(launch_path)
image_path = os.path.join(project_path, "images")


class Dialog(Ui_Dialog):
    '''Dialog class is used for adding new account to
    application and editing existing ones.'''

    def __init__(self) -> None:
        '''Class initializer'''
        self.update_f = None
        self.is_updating = None
        self.last_credentials = None
        self.last_name = None
        Ui_MainWindow.__init__(self)

    def init_controls(self) -> None:
        '''Method which gives initial state and connects signals to widgets'''
        if self.is_updating:
            self.buttonBox.accepted.connect(self.accept_update)
            (name, username, site, img) = self.last_credentials
            self.name_text.setText(name)
            self.username_text.setText(username)
            self.site_text.setText(site)
            self.image_text.setText(img)
            self.last_name = name
        else:
            self.buttonBox.accepted.connect(self.accept_add)

    def accept_add(self) -> None:
        '''Method launched on OK click in new account dialog. If user filled every field
        then new account is added to database. If not they will be informed about fail.'''
        name = self.name_text.toPlainText()
        username = self.username_text.toPlainText()
        password = self.password_text.toPlainText()
        site = self.site_text.toPlainText()
        image = self.image_text.toPlainText()
        if name == "" or username == "" or password == "" or site == "" or image == "":
            self.window = QtWidgets.QDialog()
            self.ui = Notification()
            self.ui.setupUi(self.window)
            self.ui.label.setText("Provide answer to every field!")
            self.window.show()
        else:
            sql = f"INSERT INTO user_{nick} (name, username, password, site, img) VALUES (%s, %s, %s, %s ,%s)"
            print(key)
            fernet = Fernet(key)
            enc_pass = fernet.encrypt(password.encode())
            val = (name, username, enc_pass.decode("utf-8"), site, image)
            cursor.execute(sql, val)
            db.commit()
            self.update_f()

    def accept_update(self) -> None:
        '''Method launched on OK click in edit account dialog. If user filled every field
        then new account is added to database. If not they will be informed about fail. By
        default every field but password are filled with previous data.'''
        name = self.name_text.toPlainText()
        username = self.username_text.toPlainText()
        password = self.password_text.toPlainText()
        site = self.site_text.toPlainText()
        image = self.image_text.toPlainText()
        if name == "" or username == "" or password == "" or site == "" or image == "":
            self.window = QtWidgets.QDialog()
            self.ui = Notification()
            self.ui.setupUi(self.window)
            self.ui.label.setText("Provide answer to every field!")
            self.window.show()
        else:
            sql = f"UPDATE user_{nick} SET name=%s, username=%s, password=%s, site=%s, img=%s WHERE name='{self.last_name}'"
            fernet = Fernet(key)
            enc_pass = fernet.encrypt(password.encode())
            val = (name, username, enc_pass.decode("utf-8"), site, image)
            cursor.execute(sql, val)
            db.commit()
            self.update_f()


class App(Ui_MainWindow):
    '''App class is used for managing application state among with
    dealing with all user interactions.'''

    def __init__(self) -> None:
        '''Class initializer'''
        self.package = ()
        Ui_MainWindow.__init__(self)

    def init_controls(self) -> None:
        '''Method which gives initial state according to data from
        database, connects signals to widgets and sets styles which
        were not available in CSS.'''
        self.update_account_list()

        self.frame_4.enterEvent = self.side_panel_extend
        self.frame_4.leaveEvent = self.side_panel_close

        self.add_new_account_button.setCursor(
            QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.update_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.reveal_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.add_new_account_button.clicked.connect(
            self.open_add_account_dialog)
        self.listWidget.itemClicked.connect(self.load_account_info)
        self.pushButton.clicked.connect(self.home_button_clicked)
        self.delete_button.clicked.connect(self.delete_account)
        self.reveal_button.clicked.connect(self.reveal_password)
        self.update_button.clicked.connect(self.update_account)

        self.stackedWidget.setCurrentIndex(0)
        self.hello_label.setText(f"Hello {self.package[0]}")
        if key is not None:
            self.last_login_label.setText(f"Last login:\n{self.package[1]}")
        else:
            self.last_login_label.setText("Last login:\nNever")

    def side_panel_extend(self, _event: QEvent) -> None:
        '''Handler for left application panel expand animation.'''
        self.left_tab_animation = QPropertyAnimation(
            self.frame_4, b"maximumWidth")
        self.left_tab_animation.setDuration(100)
        self.left_tab_animation.setStartValue(120)
        self.left_tab_animation.setEndValue(300)
        self.left_tab_animation.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.left_tab_animation.start()

    def side_panel_close(self, _event: QEvent) -> None:
        '''Handler for left application panel close animation.'''
        self.left_tab_animation = QPropertyAnimation(
            self.frame_4, b"maximumWidth")
        self.left_tab_animation.setDuration(100)
        self.left_tab_animation.setStartValue(300)
        self.left_tab_animation.setEndValue(120)
        self.left_tab_animation.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.left_tab_animation.start()

    def open_add_account_dialog(self) -> None:
        '''Handler for launching new account widget.'''
        update_f = self.update_account_list
        self.window = QtWidgets.QDialog()
        self.ui = Dialog()
        self.ui.setupUi(self.window)
        self.ui.is_updating = False
        self.ui.update_f = update_f
        self.ui.init_controls()
        self.window.show()

    def update_account_list(self) -> None:
        '''Method which refreshes application account state.
        Firstly pulls new data from database, then rerenders
        left application panel.'''
        cursor.execute(f"SELECT name, img FROM user_{nick}")
        result = cursor.fetchall()
        self.listWidget.clear()
        for entry in result:
            (name, img) = entry
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setPointSize(20)
            item.setFont(font)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(os.path.join(
                image_path, img)), QtGui.QIcon.Normal, QtGui.QIcon.On)
            icon.addPixmap(QtGui.QPixmap(os.path.join(
                image_path, img)), QtGui.QIcon.Selected, QtGui.QIcon.On)
            item.setIcon(icon)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            if len(name) == 1:
                item.setText(f" {name} ")
            else:
                item.setText(name)
            self.listWidget.addItem(item)
        self.stackedWidget.setCurrentIndex(0)

    def load_account_info(self, item: QListWidgetItem) -> None:
        '''Method which loads username and site from database.
        Password is not loaded because by default it's hidden.
        When needed reveal_password function will be launched.'''
        name = item.text().strip()
        cursor.execute(
            f"SELECT username, site FROM user_{nick} WHERE name='{name}'")
        result = cursor.fetchall()
        (username, site) = result[0]
        self.name_label.setText(name)
        self.username_label.setText(username)
        self.password_label.setText("********")
        self.site_label.setText(site)
        self.label_4.setText("| Account")
        self.stackedWidget.setCurrentIndex(1)

    def home_button_clicked(self) -> None:
        '''Method which switches main page back to home page.'''
        self.stackedWidget.setCurrentIndex(0)
        self.label_4.setText("| Home")

    def delete_account(self) -> None:
        '''Method which is launched after agreeing upon
        deleting account info from application.'''
        name = self.name_label.text().strip()
        sql = f"DELETE FROM user_{nick} WHERE name='{name}'"
        cursor.execute(sql)
        db.commit()
        self.update_account_list()
        self.stackedWidget.setCurrentIndex(0)

    def reveal_password(self) -> None:
        '''Method which pulls and decodes given password with
        user token key generated with successful login.'''
        name = self.name_label.text().strip()
        cursor.execute(
            f"SELECT password FROM user_{nick} WHERE name='{name}'")
        result = cursor.fetchall()
        password = result[0][0]
        fernet = Fernet(key)
        enc_pass = fernet.decrypt(password.encode())
        passwd_utf8 = enc_pass.decode("utf-8")
        self.password_label.setText(passwd_utf8)

    def update_account(self) -> None:
        '''Handler for launching edit account widget.'''
        cursor.execute(
            f"SELECT img FROM user_{nick} WHERE name='{self.name_label.text()}'")
        res = cursor.fetchall()
        img = res[0][0]
        update_f = self.update_account_list
        self.window = QtWidgets.QDialog()
        self.ui = Dialog()
        self.ui.setupUi(self.window)
        self.ui.is_updating = True
        self.ui.update_f = update_f
        self.ui.last_credentials = (self.name_label.text(
        ), self.username_label.text(), self.site_label.text(), img)
        self.ui.init_controls()
        self.window.show()


class Login(Ui_LoginWindow):
    '''Login class used for validating user data and provides
    easy login & register system.'''

    def __init__(self) -> None:
        '''Class initializer'''
        Ui_LoginWindow.__init__(self)

    def init_controls(self) -> None:
        '''Method which connects signals to widgets on initiate.'''
        self.login_button.clicked.connect(self.handle_login)
        self.register_button.clicked.connect(self.handle_register)

    def handle_register(self) -> None:
        '''Method which handles registration process. After
        verifying that new user doesn't exist already creates
        their profile.'''
        login = self.user_line_edit.text()
        passwd = self.password_line_edit.text()
        cursor.execute(f"SELECT * FROM users WHERE username='{login}'")
        duplicate = cursor.fetchall()
        if len(duplicate) == 0:
            salt = get_random_string(32)
            temp = crypt(passwd, "", iterations=10000)
            hash = crypt(temp, salt, iterations=10000)
            sql = "INSERT INTO users (username, password, salt) VALUES (%s, %s, %s)"
            val = (login, hash, salt)
            cursor.execute(sql, val)
            db.commit()

    def handle_login(self) -> None:
        '''Method which handles logging process. To determine
        whether user provided valid password encryption key is
        being first pulled and then used to decrypt saved
        password.'''
        global key, nick
        login = self.user_line_edit.text()
        passwd = self.password_line_edit.text()
        cursor.execute(
            f"SELECT password, salt, last_login FROM users WHERE username='{login}'")
        result = cursor.fetchall()
        if len(result) == 1:
            (hashed_passwd, salt, last_login) = result[0]

            key = crypt(passwd, "", iterations=10000)
            hash = crypt(key, salt, iterations=10000)
            key = key[0:32]
            key = base64.urlsafe_b64encode(key.encode())

            if hash == hashed_passwd:
                nick = login
                cursor.execute(
                    f"UPDATE users SET last_login = '{date.today().strftime('%B %d, %Y')}' WHERE username = '{login}'")
                cursor.execute(
                    f"CREATE TABLE if not exists user_{login} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), username VARCHAR(255), password VARCHAR(255), site VARCHAR(255), img VARCHAR(255))")
                main_window.close()
                self.window = QtWidgets.QMainWindow()
                self.ui = App()
                self.ui.setupUi(self.window)
                self.ui.package = (login, last_login)
                self.ui.init_controls()
                self.window.show()


def get_random_string(length) -> str:
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Login()
    ui.setupUi(main_window)
    ui.init_controls()
    main_window.show()
    sys.exit(app.exec_())

# pyuic5 -x app.ui -o app.py
# pyuic5 -x account.ui -o account.py
# pyuic5 -x notification.ui -o notification.py
# pyuic5 -x form.ui -o login.py
# pyrcc5 -o files.py files_rc.qrc
