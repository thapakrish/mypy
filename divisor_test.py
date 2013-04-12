import unittest
import divisor


class TestRemoveShared(unittest.TestCase):
    """Tests for function gcd within divisor which finds the greatest common divisor
        of two given numbers"""

    def test_even_numbers(self):
        """
        Test gcd between two even numbers.
        """
        expected = 2
        actual = divisor.gcd(2,4)        
        self.assertEqual(expected, actual)


    def test_odd_numbers(self):
        """
        Test gcd between two odd numbers.
        """
        expected = 5
        actual = divisor.gcd(5,15)        
        self.assertEqual(expected, actual)

    def test_zero_case(self):
        """
        Test gcd between two odd numbers.
        """
        expected = 10
        actual = divisor.gcd(10,0)        
        self.assertEqual(expected, actual)        

if __name__ == '__main__':
    unittest.main(exit=False)
