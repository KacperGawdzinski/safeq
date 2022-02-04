from unittest.mock import MagicMock
import unittest
import sys
from src.safeq import Dialog


class TestApp(unittest.TestCase):
    def accept_add_fail_test(self):
        dialog = Dialog()
        dialog.is_updating = False
        dialog.init_controls()
        self.assertIsNone(dialog.last_name)

    def expect_last_name_when_is_updating(self):
        dialog = Dialog()
        dialog.is_updating = True
        dialog.last_credentials = ("abc", "", "", "")
        dialog.init_controls()
        self.assertEqual(dialog.last_name, "abc")


if __name__ == '__main__':
    unittest.main()
