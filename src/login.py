# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import src.files_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(1007, 822)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.top_bar.setStyleSheet("background-color:#36393e")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("background-color: #424549")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_area = QtWidgets.QFrame(self.content)
        self.login_area.setMaximumSize(QtCore.QSize(450, 550))
        self.login_area.setStyleSheet("background-color: #F9FBFF;\n"
                                      "border-radius: 5px;")
        self.login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_area.setObjectName("login_area")
        self.logo = QtWidgets.QFrame(self.login_area)
        self.logo.setGeometry(QtCore.QRect(110, 30, 241, 311))
        self.logo.setStyleSheet("border-image:url(:/logo_icon/images/logo_icon.png) 0 0 0 0 stretch stretch;\n"
                                "background-repeat: no-repeat;\n"
                                "background-position: center;")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.user_line_edit = QtWidgets.QLineEdit(self.login_area)
        self.user_line_edit.setGeometry(QtCore.QRect(90, 350, 271, 41))
        self.user_line_edit.setStyleSheet("QLineEdit {\n"
                                          "    font: 75 12pt \"Verdana\";\n"
                                          "    border: 2px solid rgb(49, 87, 121);\n"
                                          "    border-radius: 5px;\n"
                                          "    padding: 15px;\n"
                                          "    padding-top: 5px;\n"
                                          "    padding-bottom: 5px; \n"
                                          "}\n"
                                          "\n"
                                          "QLineEdit:hover {\n"
                                          "    border: 2px solid rgb(54, 54, 54)\n"
                                          "}")
        self.user_line_edit.setText("")
        self.user_line_edit.setObjectName("user_line_edit")
        self.password_line_edit = QtWidgets.QLineEdit(self.login_area)
        self.password_line_edit.setGeometry(QtCore.QRect(90, 400, 271, 41))
        self.password_line_edit.setStyleSheet("QLineEdit {\n"
                                              "    font: 75 12pt \"Verdana\";\n"
                                              "    border: 2px solid rgb(49, 87, 121);\n"
                                              "    border-radius: 5px;\n"
                                              "    padding: 15px;\n"
                                              "    padding-top: 5px;\n"
                                              "    padding-bottom: 5px; \n"
                                              "}\n"
                                              "\n"
                                              "QLineEdit:hover {\n"
                                              "    border: 2px solid rgb(54, 54, 54)\n"
                                              "}")
        self.password_line_edit.setText("")
        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line_edit.setObjectName("password_line_edit")
        self.login_button = QtWidgets.QPushButton(self.login_area)
        self.login_button.setGeometry(QtCore.QRect(80, 460, 141, 41))
        self.login_button.setStyleSheet("QPushButton {\n"
                                        "    background-color: rgb(49, 87, 121);\n"
                                        "    font: 75 12pt \"Verdana\";\n"
                                        "    color: white;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background-color:rgb(61, 108, 150)\n"
                                        "}")
        self.login_button.setObjectName("login_button")
        self.register_button = QtWidgets.QPushButton(self.login_area)
        self.register_button.setGeometry(QtCore.QRect(230, 460, 141, 41))
        self.register_button.setStyleSheet("QPushButton {\n"
                                           "    background-color: rgb(49, 87, 121);\n"
                                           "    font: 75 12pt \"Verdana\";\n"
                                           "    color: white;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "    background-color:rgb(61, 108, 150)\n"
                                           "}")
        self.register_button.setObjectName("register_button")
        self.horizontalLayout.addWidget(self.login_area)
        self.verticalLayout.addWidget(self.content)
        self.bottom_bar = QtWidgets.QFrame(self.centralwidget)
        self.bottom_bar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bottom_bar.setStyleSheet("background-color: #36393e")
        self.bottom_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_bar.setObjectName("bottom_bar")
        self.verticalLayout.addWidget(self.bottom_bar)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1007, 22))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.user_line_edit.setPlaceholderText(
            _translate("LoginWindow", "USER"))
        self.password_line_edit.setPlaceholderText(
            _translate("LoginWindow", "PASSWORD"))
        self.login_button.setText(_translate("LoginWindow", "LOGIN"))
        self.register_button.setText(_translate("LoginWindow", "REGISTER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
