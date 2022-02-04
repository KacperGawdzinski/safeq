# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import app_files
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 1080)
        MainWindow.setStyleSheet("background: transparent;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background: transparent;")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: #424549;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(-3)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 120))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame_3.setStyleSheet("background-color: #36393e")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setMaximumSize(QtCore.QSize(120, 120))
        self.frame_7.setStyleSheet("background-color: #282b30;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_7)
        self.pushButton.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    border-image:url(:/home_icon/images/home_icon.png) 0 0 0 0 stretch stretch;\n"
                                      "    background: transparent;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background:#36393e;\n"
                                      "}")
        self.pushButton.setText("")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setStyleSheet("background-color: #282b30")
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.frame_11 = QtWidgets.QFrame(self.frame_9)
        self.frame_11.setGeometry(QtCore.QRect(0, 10, 35, 40))
        self.frame_11.setStyleSheet("border-image:url(:/small_logo_icon/images/small_logo_icon.png) 0 0 0 0 stretch stretch;\n"
                                    "background-repeat: no-repeat;\n"
                                    "background-position: center;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_9)
        self.textBrowser.setGeometry(QtCore.QRect(40, 10, 261, 61))
        self.textBrowser.setStyleSheet("border: none;\n"
                                       "font: 75 14pt \"Verdana\";\n"
                                       "color: white;")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_4 = QtWidgets.QLabel(self.frame_10)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 311, 41))
        self.label_4.setStyleSheet("border: none;\n"
                                   "color: rgb(225, 225, 225);\n"
                                   "font: \"Verdana\";\n"
                                   "font-size: 20px;\n"
                                   "")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.frame_10)
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777207))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_4.setStyleSheet("QFrame {\n"
                                   "    background-color: #282b30;\n"
                                   "    border: 0px\n"
                                   "}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.frame_4)
        self.listWidget.setEnabled(True)
        self.listWidget.setStatusTip("")
        self.listWidget.setStyleSheet("QScrollBar {\n"
                                      "    height:0px;\n"
                                      "    width:0px;\n"
                                      "}\n"
                                      "\n"
                                      "QListWidget {\n"
                                      "    color: white;\n"
                                      "}\n"
                                      "\n"
                                      "QListWidget::item {\n"
                                      "    color: white;\n"
                                      "}\n"
                                      "")
        self.listWidget.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setIconSize(QtCore.QSize(95, 95))
        self.listWidget.setModelColumn(0)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/fb_icon/images/fb_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/fb_icon/images/fb_icon.png"),
                       QtGui.QIcon.Selected, QtGui.QIcon.On)
        item.setIcon(icon)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            ":/steam_icon/images/steam_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(
            ":/steam_icon/images/steam_icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        item.setIcon(icon1)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setStatusTip("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_5)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.hello_label = QtWidgets.QLabel(self.page)
        self.hello_label.setGeometry(QtCore.QRect(10, 0, 681, 81))
        self.hello_label.setStyleSheet("font-size: 50px;\n"
                                       "color: white;\n"
                                       "")
        self.hello_label.setObjectName("hello_label")
        self.last_login_label = QtWidgets.QLabel(self.page)
        self.last_login_label.setGeometry(QtCore.QRect(10, 800, 681, 111))
        self.last_login_label.setStyleSheet("font-size: 40px;\n"
                                            "color: rgb(225, 225, 225);\n"
                                            "")
        self.last_login_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.last_login_label.setObjectName("last_login_label")
        self.frame_6 = QtWidgets.QFrame(self.page)
        self.frame_6.setGeometry(QtCore.QRect(10, 110, 471, 341))
        self.frame_6.setStyleSheet("QFrame#frame_6 {\n"
                                   "    border: 5px;\n"
                                   "    border-radius: 10;\n"
                                   "    border-style: solid;\n"
                                   "    border-color: black;\n"
                                   "}\n"
                                   "\n"
                                   "QFrame#frame_6::hover {\n"
                                   "    border-color: rgb(114,137,218);\n"
                                   "}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.add_new_account_button = QtWidgets.QPushButton(self.frame_6)
        self.add_new_account_button.setGeometry(QtCore.QRect(0, 0, 471, 341))
        self.add_new_account_button.setStyleSheet(
            "background-color: transparent;")
        self.add_new_account_button.setText("")
        self.add_new_account_button.setObjectName("add_new_account_button")
        self.label_8 = QtWidgets.QLabel(self.frame_6)
        self.label_8.setGeometry(QtCore.QRect(80, 20, 301, 61))
        self.label_8.setStyleSheet("font-size: 40px;\n"
                                   "color: white;\n"
                                   "\n"
                                   "")
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setGeometry(QtCore.QRect(130, 100, 211, 201))
        self.label.setStyleSheet("border-image: url(:/plus_icon/images/plus_icon.png) 0 0 0 0 stretch stretch;\n"
                                 "background-repeat: no-repeat;\n"
                                 "background-position: center;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_8.raise_()
        self.label.raise_()
        self.add_new_account_button.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.name_label = QtWidgets.QLabel(self.page_2)
        self.name_label.setGeometry(QtCore.QRect(290, 0, 421, 91))
        self.name_label.setStyleSheet("font-size: 50px;\n"
                                      "color: white;\n"
                                      "")
        self.name_label.setObjectName("name_label")
        self.username_label = QtWidgets.QLabel(self.page_2)
        self.username_label.setGeometry(QtCore.QRect(290, 190, 421, 101))
        self.username_label.setStyleSheet("font-size: 50px;\n"
                                          "color: white;\n"
                                          "")
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.page_2)
        self.password_label.setGeometry(QtCore.QRect(290, 330, 421, 101))
        self.password_label.setStyleSheet("font-size: 50px;\n"
                                          "color: white;\n"
                                          "")
        self.password_label.setObjectName("password_label")
        self.site_label = QtWidgets.QLabel(self.page_2)
        self.site_label.setGeometry(QtCore.QRect(290, 470, 421, 101))
        self.site_label.setStyleSheet("font-size: 50px;\n"
                                      "color: white;\n"
                                      "")
        self.site_label.setObjectName("site_label")
        self.update_button = QtWidgets.QPushButton(self.page_2)
        self.update_button.setGeometry(QtCore.QRect(40, 660, 261, 91))
        self.update_button.setStyleSheet("QPushButton {\n"
                                         "    background-color: #FED766;\n"
                                         "    font-size: 30px;\n"
                                         "    border-radius: 8px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    background:#36393e;\n"
                                         "    background-color: #D8BD62;\n"
                                         "}")
        self.update_button.setObjectName("update_button")
        self.delete_button = QtWidgets.QPushButton(self.page_2)
        self.delete_button.setGeometry(QtCore.QRect(400, 660, 261, 91))
        self.delete_button.setStyleSheet("QPushButton {\n"
                                         "    background-color: #bb4430;\n"
                                         "    font-size: 30px;\n"
                                         "    border-radius: 8px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: #A4432F;\n"
                                         "}")
        self.delete_button.setObjectName("delete_button")
        self.name_label_2 = QtWidgets.QLabel(self.page_2)
        self.name_label_2.setGeometry(QtCore.QRect(10, 0, 241, 91))
        self.name_label_2.setStyleSheet("font-size: 50px;\n"
                                        "color: white;\n"
                                        "")
        self.name_label_2.setObjectName("name_label_2")
        self.username_label_2 = QtWidgets.QLabel(self.page_2)
        self.username_label_2.setGeometry(QtCore.QRect(10, 190, 241, 101))
        self.username_label_2.setStyleSheet("font-size: 50px;\n"
                                            "color: white;\n"
                                            "")
        self.username_label_2.setObjectName("username_label_2")
        self.password_label_2 = QtWidgets.QLabel(self.page_2)
        self.password_label_2.setGeometry(QtCore.QRect(10, 330, 241, 101))
        self.password_label_2.setStyleSheet("font-size: 50px;\n"
                                            "color: white;\n"
                                            "")
        self.password_label_2.setObjectName("password_label_2")
        self.site_label_2 = QtWidgets.QLabel(self.page_2)
        self.site_label_2.setGeometry(QtCore.QRect(10, 470, 241, 101))
        self.site_label_2.setStyleSheet("font-size: 50px;\n"
                                        "color: white;\n"
                                        "")
        self.site_label_2.setObjectName("site_label_2")
        self.reveal_button = QtWidgets.QPushButton(self.page_2)
        self.reveal_button.setGeometry(QtCore.QRect(220, 780, 261, 91))
        self.reveal_button.setStyleSheet("QPushButton {\n"
                                         "    background-color: #00cc66;\n"
                                         "    font-size: 30px;\n"
                                         "    border-radius: 8px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: #00994d;\n"
                                         "}")
        self.reveal_button.setObjectName("reveal_button")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame_2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SafeQ"))
        self.textBrowser.setMarkdown(_translate("MainWindow", "SafeQ\n"
                                                "\n"
                                                ""))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Verdana\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
                                            "<p style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">SafeQ</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "| Home"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Facebook"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Steam"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.hello_label.setText(_translate("MainWindow", "Hello ${name}"))
        self.last_login_label.setText(_translate("MainWindow", "Last login:\n"
                                                 "{value}"))
        self.label_8.setText(_translate("MainWindow", "Add new account"))
        self.name_label.setText(_translate("MainWindow", "${company}"))
        self.username_label.setText(_translate("MainWindow", "${username}"))
        self.password_label.setText(_translate("MainWindow", "${password}"))
        self.site_label.setText(_translate("MainWindow", "${site}"))
        self.update_button.setText(_translate("MainWindow", "Update"))
        self.delete_button.setText(_translate("MainWindow", "Delete"))
        self.name_label_2.setText(_translate("MainWindow", "Source:"))
        self.username_label_2.setText(_translate("MainWindow", "Username:"))
        self.password_label_2.setText(_translate("MainWindow", "Password:"))
        self.site_label_2.setText(_translate("MainWindow", "Site:"))
        self.reveal_button.setText(_translate("MainWindow", "Reveal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())