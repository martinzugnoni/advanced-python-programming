import unittest

# --rmotr: required imports--
# from main import human_readable_type
from solutions import human_readable_type
# --rmotr: required imports--

from datetime import datetime


class HumanReadableTypeTestCase(unittest.TestCase):
    def test_strings_returns_String(self):
        """Should return String"""
        self.assertEqual(human_readable_type("Hello Rmotr.com"), "String")

    def test_integer_returns_Number(self):
        """Should return Number"""
        self.assertEqual(human_readable_type(33), "Number")

    def test_False_returns_Boolean(self):
        """Should return Boolean"""
        self.assertEqual(human_readable_type(False), "Boolean")

    def test_True_returns_Boolean(self):
        """Should return Boolean"""
        self.assertEqual(human_readable_type(True), "Boolean")

    def test_None_returns_None(self):
        """Should return None"""
        self.assertEqual(human_readable_type(None), "None")

    def test_other_obj_returns_Other(self):
        """Should return Other"""
        self.assertEqual(human_readable_type(datetime.now()), "Other")
