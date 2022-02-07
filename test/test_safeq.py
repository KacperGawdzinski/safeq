from unittest.mock import MagicMock
import unittest
import sys
import src.safeq
from PyQt5 import QtCore, QtWidgets, QtGui
import sys
from pbkdf2 import crypt
from inspect import getsourcefile
from os.path import abspath
from unittest import mock
import os


class TestApp(unittest.TestCase):
    def test_accept_add_fail_test(self):
        _app = QtWidgets.QApplication(sys.argv)
        main_window = QtWidgets.QDialog()
        dialog = src.safeq.Dialog()
        dialog.setupUi(main_window)
        dialog.init_controls()
        dialog.is_updating = False

        self.assertIsNone(dialog.last_name)

    def test_expect_last_name_when_is_updating(self):
        _app = QtWidgets.QApplication(sys.argv)
        main_window = QtWidgets.QDialog()
        dialog = src.safeq.Dialog()
        dialog.setupUi(main_window)
        dialog.is_updating = True
        dialog.last_credentials = ("abc", "", "", "")
        dialog.init_controls()

        self.assertEqual(dialog.last_name, "abc")

    def test_not_add_if_all_fields_not_empty(self):
        _app = QtWidgets.QApplication(sys.argv)
        main_window = QtWidgets.QDialog()
        dialog = src.safeq.Dialog()
        dialog.setupUi(main_window)
        dialog.name_text.setText("abc")
        dialog.accept_add()

        self.assertEqual("Provide answer to every field!",
                         dialog.ui.label.text())

    def test_last_date_should_not_display_if_doesnt_exist(self):
        _app = QtWidgets.QApplication(sys.argv)
        main_window = QtWidgets.QMainWindow()
        main_app = src.safeq.App()
        main_app.setupUi(main_window)
        src.safeq.nick = "test_acc"
        src.safeq.key = None
        main_app.package = ("test_acc")
        main_app.init_controls()

        self.assertEqual("Last login:\nNever",
                         main_app.last_login_label.text())

    def test_last_date_should_display_if_exists(self):
        _app = QtWidgets.QApplication(sys.argv)
        main_window = QtWidgets.QMainWindow()
        main_app = src.safeq.App()
        main_app.setupUi(main_window)
        src.safeq.nick = "test_acc"
        src.safeq.key = "abc"
        main_app.package = ("test_acc", "14 feb")
        main_app.init_controls()

        self.assertEqual("Last login:\n14 feb",
                         main_app.last_login_label.text())

    def test_account_name_if_with_spaces(self):
        _app = QtWidgets.QApplication(sys.argv)
        main_window = QtWidgets.QMainWindow()
        main_app = src.safeq.App()
        main_app.setupUi(main_window)
        src.safeq.nick = "test_acc"
        main_app.update_account_list()
        itemsTextList = [str(main_app.listWidget.item(i).text())
                         for i in range(main_app.listWidget.count())]

        self.assertEqual(itemsTextList[0], " 1 ")

    def test_account_name_if_not_with_spaces(self):
        _app = QtWidgets.QApplication(sys.argv)
        main_window = QtWidgets.QMainWindow()
        main_app = src.safeq.App()
        main_app.setupUi(main_window)
        src.safeq.nick = "test_acc"
        main_app.update_account_list()
        itemsTextList = [str(main_app.listWidget.item(i).text())
                         for i in range(main_app.listWidget.count())]

        self.assertEqual(itemsTextList[1], "23")

    def test_image_folder_path(self):
        launch_path = abspath(getsourcefile(lambda: 0))
        project_path = os.path.dirname(os.path.dirname(launch_path))
        image_path = os.path.join(project_path, "src", "images")

        self.assertEqual(src.safeq.image_path, image_path)

    def test_random_string_should_have_desired_length(self):
        self.assertEqual(len(src.safeq.get_random_string(32)), 32)

    def test_password_should_be_hidden_by_default(self):
        _app = QtWidgets.QApplication(sys.argv)
        main_window = QtWidgets.QMainWindow()
        main_app = src.safeq.App()
        main_app.setupUi(main_window)
        src.safeq.nick = "test_acc"
        main_app.update_account_list()
        itemsList = [main_app.listWidget.item(i)
                     for i in range(main_app.listWidget.count())]
        main_app.load_account_info(itemsList[0])
        self.assertEqual(main_app.password_label.text(), "********")


if __name__ == '__main__':
    unittest.main()
