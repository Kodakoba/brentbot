import unittest
import datetime
from freezegun import freeze_time
from unittest import mock
from unittest.mock import patch
from Utilities.filereader import FileReader
from Utilities.regex import Regex
from Utilities.greeting import Greeting
#---------------------------------------------
#Utilities\filereader.py      17     13    24%
#Utilities\greeting.py        13      2    85%
#Utilities\regex.py           14      1    93%
#tests.py                     53     16    70%
#---------------------------------------------
#TOTAL                        97     32    67%
#TOTAL (WITHOUT TEST)         44     16    67% (lmao)




class TestSystem(unittest.TestCase):
    def test_file_reader(self):
        file_reader = FileReader("tests.py")
        self.assertEqual(file_reader.filename, "tests.py")

    #to properly test this file

    def test_regex(self):
        registry_expression = Regex()
        bob = registry_expression.text_to_regex("hi", False, True)
        self.assertEqual(registry_expression.escape_regex("test"),"test")
        self.assertEqual(bob, "(?i)hi")

    def test_greeting(self):
        new_greeting = Greeting("test")
        self.assertEqual(new_greeting.greeting("test"), "Hello test, i am brent")

    @patch('datetime.datetime')
    #@mock.patch("datetime.datetime", wraps=datetime)
    @freeze_time("2000-10-10 10:10:10")
    def test_morning_greeting(self, mock_datetime):
        new_greeting = Greeting("test")
        mock_datetime.return_value = datetime.datetime(2000, 10, 10, 10, 10, 10)
        result = new_greeting.greet_based_on_input("test")
        self.assertEqual(result, "Good Morning test")
        registry_expression = Regex()
        bob = registry_expression.text_to_regex("hi", False, True)
        result2 = new_greeting.greet_based_on_input(bob)
        self.assertEqual(result2, "Good Morning (?i)hi")

    @patch('datetime.datetime')
    @freeze_time("2000-10-10 12:10:10")
    def test_morning_greeting(self, mock_datetime):
        new_greeting = Greeting("test")
        mock_datetime.return_value = datetime.datetime(2000, 10, 10, 12, 10, 10)
        result = new_greeting.greet_based_on_input("test")
        self.assertEqual(result, "Good Afternoon test")
        registry_expression = Regex()
        bob = registry_expression.text_to_regex("hi", False, True)
        result2 = new_greeting.greet_based_on_input(bob)
        self.assertEqual(result2, "Good Afternoon (?i)hi")

    @patch('datetime.datetime')
    @freeze_time("2000-10-10 18:10:10") #this actually helped fix a weird issue with mock thanks python
    def test_morning_greeting(self, mock_datetime):
        new_greeting = Greeting("test")
        mock_datetime.return_value = datetime.datetime(2000, 10, 10, 18, 10, 10)
        result = new_greeting.greet_based_on_input("test")
        self.assertEqual(result, "Good Evening test")
        registry_expression = Regex()
        bob = registry_expression.text_to_regex("hi", False, True)
        result2 = new_greeting.greet_based_on_input(bob)
        self.assertEqual(result2, "Good Evening (?i)hi")


