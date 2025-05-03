import unittest
from Utilities.filereader import FileReader

class TestSystem(unittest.TestCase):
    def test_file_reader(self):
        file_reader = FileReader("tests.py")
        self.assertEqual(file_reader.filename, "tests.py")


