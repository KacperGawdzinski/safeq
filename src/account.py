# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'account.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("background-color: #424549;")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(120, 240, 161, 32))
        self.buttonBox.setStyleSheet("background-color: white;")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.name_text = QtWidgets.QTextEdit(Dialog)
        self.name_text.setGeometry(QtCore.QRect(80, 20, 241, 31))
        self.name_text.setStyleSheet("border: 0px;\n"
                                     "color: white;\n"
                                     "font-size: 20px;\n"
                                     "")
        self.name_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.name_text.setObjectName("name_text")
        self.username_text = QtWidgets.QTextEdit(Dialog)
        self.username_text.setGeometry(QtCore.QRect(80, 60, 241, 31))
        self.username_text.setStyleSheet("border: 0px;\n"
                                         "color: white;\n"
                                         "font-size: 20px;\n"
                                         "")
        self.username_text.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.username_text.setObjectName("username_text")
        self.password_text = QtWidgets.QTextEdit(Dialog)
        self.password_text.setGeometry(QtCore.QRect(80, 100, 241, 31))
        self.password_text.setStyleSheet("border: 0px;\n"
                                         "color: white;\n"
                                         "font-size: 20px;\n"
                                         "")
        self.password_text.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.password_text.setObjectName("password_text")
        self.site_text = QtWidgets.QTextEdit(Dialog)
        self.site_text.setGeometry(QtCore.QRect(80, 140, 241, 31))
        self.site_text.setStyleSheet("border: 0px;\n"
                                     "color: white;\n"
                                     "font-size: 20px;\n"
                                     "")
        self.site_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.site_text.setObjectName("site_text")
        self.image_text = QtWidgets.QTextEdit(Dialog)
        self.image_text.setGeometry(QtCore.QRect(80, 180, 241, 31))
        self.image_text.setStyleSheet("border: 0px;\n"
                                      "color: white;\n"
                                      "font-size: 20px;\n"
                                      "")
        self.image_text.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.image_text.setObjectName("image_text")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Account"))
        self.name_text.setPlaceholderText(_translate("Dialog", "Name..."))
        self.username_text.setPlaceholderText(
            _translate("Dialog", "Username..."))
        self.password_text.setPlaceholderText(
            _translate("Dialog", "Password..."))
        self.site_text.setPlaceholderText(_translate("Dialog", "Site..."))
        self.image_text.setPlaceholderText(
            _translate("Dialog", "Image path..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
