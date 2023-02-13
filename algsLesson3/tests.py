import unittest
import answer


class TestLast(unittest.TestCase):
    def test_given_input(self):
        actual = answer.summation([5, 10, -3,15, -999 ,13])
        self.assertEqual(actual, 30)
    def test_all_negatives(self):
        actual = answer.summation([-1, -1, -1, -1, -1])
        self.assertEqual(actual, None)
    def test_zero_grades(self):
        failure = answer.summation([0, 0, 0, 0, 0, 0])
        self.assertEqual(failure, 0)
    def test_test(self):
        weird_test = answer.summation([-1, 2, 4, 5, 7])
        self.assertEqual(weird_test, 18)
    

if __name__ == '__main__':
    unittest.main()        



