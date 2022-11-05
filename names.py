'''
A unit test verifies that one specific aspect of a function’s behavior is correct. 
A test case is a collection of unit tests that together prove
that a function behaves as it’s supposed to, within the full range of situations you expect it to handle.
To write a test case for a function, import the unittest module
and the function you want to test. Then create a class that inherits from
unittest.TestCase, and write a series of methods to test different aspects of
your function’s behavior
 '''

# Here’s a test case with one method that verifies that the function get_formatted_name() works correctly when given a first and last name:

import unittest
from TestingYourCode import get_formatted_name
class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name(
        'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()


'''
Assert methods verify that a result you received matches the result you
expected to receive. In this case, because we know get_formatted_name() is
supposed to return a capitalized, properly spaced full name, we expect
the value in formatted_name to be Janis Joplin. 

Compare the value in formatted_name to the string 'Janis Joplin'. If
they are equal as expected, fine. But if they don’t match, let me know!”
The line unittest.main() tells Python to run the tests in this file. 
'''

