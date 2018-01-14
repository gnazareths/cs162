import unittest
import prime


class PrimeTests(unittest.TestCase):
    """Tests for `prime.py`."""

    def test_is_seven_prime(self):
        """Is five prime according to the lib?"""
        self.assertTrue(prime.is_prime(7))

    def test_bigger_prime_of_twelve(self):
        self.assertEqual(prime.get_next_prime(12), 13)

    def test_bigger_prime_of_thirteen(self):
        self.assertEqual(prime.get_next_prime(13), 13)


if __name__ == '__main__':
    unittest.main()
