"""
Sample tests for the app module.
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """
    Test the calc module.
    """

    def test_add_numbers(self):
        """Test adding two numbers together."""
        res = calc.add(1, 2)

        self.assertEqual(res, 3)

    def test_subtract_numbers(self):
        """Test subtracting two numbers."""
        res = calc.subtract(5, 11)

        self.assertEqual(res, 6)
