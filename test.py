"""
Module Testcases
"""
import unittest

from main import main, get_words_for_number


class TestNumberToWord(unittest.TestCase):
    """
    A TestCase for testing number to word module
    """

    def test_main_with_valid_input(self):
        """
        testing main with integers
        :return: None
        """
        value = main("123")
        self.assertEqual(value, "one hundred and twenty-three")

    def test_main_with_invalid_input(self):
        """
        testing main with invalid integers
        :return: None
        """
        value = main("123.45")
        self.assertIsNone(value)

    def test_get_words_for_number_with_valid_input(self):
        """
        testing get_words_for_number with valid numbers
        :return: None
        """
        value = get_words_for_number("46")
        self.assertEqual(value, "forty-six")

        value = get_words_for_number("46.5")
        self.assertEqual(value, "forty-six point five")

        value = get_words_for_number(55)
        self.assertEqual(value, "fifty-five")

        value = get_words_for_number(55.6)
        self.assertEqual(value, "fifty-five point six")

        value = get_words_for_number(-55.6)
        self.assertEqual(value, "minus fifty-five point six")

        value = get_words_for_number("55.55.44")
        self.assertEqual(value, "fifty-five point five five four four")

    def test_get_words_for_number_with_invalid_input(self):
        """
        testing get_words_for_number with invalid input
        :return: None
        """
        value = get_words_for_number("forty-six")
        self.assertEqual(value, "zero")

        value = get_words_for_number("random")
        self.assertEqual(value, "zero")


if __name__ == "__main__":
    unittest.main()
