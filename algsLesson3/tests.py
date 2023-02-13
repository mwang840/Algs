import unittest
import answer


class TestLast(unittest.TestCase):
    def test_given_input(self):
        actual = answer.summation([5, 10, -3,15, -999 ,13])
        self.assertEqual(actual, 30)
    def test_all_negatives(self):
        actual = answer.summation([-1, -1, -1, -1, -1])
        self.assertEqual(actual, "EMPTY")
    def test_zero_grades(self):
        failure = answer.summation([0, 0, 0, 0, 0, 0])
        self.assertEqual(failure, 0)
    def test_test(self):
        weird_test = answer.summation([-1, 2, 4, 5, 7])
        self.assertEqual(weird_test, 18)
    def test_hundreds(self):
        hundreds = answer.summation([100, 100, 100, 100, 100, 100, 100])
        self.assertEqual(hundreds, 700)
        self.assertNotEqual(hundreds, 500)
    def test_tens(self):
        tens = answer.summation([10, -5, 20, 30, -10, 40, -999, 60]) 
        self.assertEqual(tens, 100)   

if __name__ == '__main__':
    unittest.main()        



