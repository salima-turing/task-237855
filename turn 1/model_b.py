import unittest
import datetime


class TestDateValidation(unittest.TestCase):
    def setUp(self):
        # Initialize the default date format
        self.date_format = '%Y-%m-%d'

    def test_valid_date(self):
        # Test for a valid date in the default format
        date_str = '2023-07-31'
        self.assertTrue(is_valid_date(date_str, self.date_format))

    def test_invalid_date(self):
        # Test for an invalid date in the default format
        date_str = '2023-02-30'
        self.assertFalse(is_valid_date(date_str, self.date_format))

    def test_custom_date_format(self):
        # Adapt the test to handle a custom date format
        custom_format = '%m/%d/%Y'
        date_str = '07/31/2023'
        self.assertTrue(is_valid_date(date_str, custom_format))

    def test_minimum_date(self):
        # Adapt the test to check for a minimum date constraint
        min_date = datetime.date(2023, 1, 1)
        date_str = '2023-01-02'
        self.assertTrue(is_valid_date(date_str, self.date_format, min_date=min_date))

    def test_maximum_date(self):
        # Adapt the test to check for a maximum date constraint
        max_date = datetime.date(2023, 12, 31)
        date_str = '2023-12-30'
        self.assertTrue(is_valid_date(date_str, self.date_format, max_date=max_date))


if __name__ == '__main__':
    unittest.main()
