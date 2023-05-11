import unittest
import answer as ApproximationAnswer

class MyTestCase(unittest.TestCase):
    def test_given(self):
        self.assertEqual(ApproximationAnswer.get_ada_location_bf(ApproximationAnswer.to_matrix("0 3 4 2 7\n 3 0 4 6 3\n 4 4 0 5 8\n 2 6 5 0 6\n 7 3 8 6 0\n")), "0\n1\n2\n3\n4\n25")  # add assertion here
    def test_large(self):
        self.assertEqual(ApproximationAnswer.get_ada_location_bf(ApproximationAnswer.to_matrix("0 29 82 46 68 52 72 42 51 55 29 74 23 72 46\n 29 0 55 46 42 43 43 23 23 31 41 51 11 52 21\n 82 55 0 68 46 55 23 43 41 29 79 21 64 31 51\n 46 46 68 0 82 15 72 31 62 42 21 51 51 43 64\n 68 42 46 82 0 74 23 52 21 46 82 58 46 65 23\n 52 43 55 15 74 0 61 23 55 31 33 37 51 29 59\n 72 43 23 72 23 61 0 42 23 31 77 37 51 46 33\n 42 23 43 31 52 23 42 0 33 15 37 33 33 31 37\n 51 23 41 62 21 55 23 33 0 29 62 46 29 51 11\n 55 31 29 42 46 31 31 15 29 0 51 21 41 23 37\n 29 41 79 21 82 33 77 37 62 51 0 65 42 59 61\n 74 51 21 51 58 37 37 33 46 21 65 0 61 11 55\n 23 11 64 51 46 51 51 33 29 41 42 61 0 62 23\n 72 52 31 43 65 29 46 31 51 23 59 11 62 0 59\n46 21 51 64 23 59 33 37 11 37 61 55 23 59 0\n")), "0\n9\n7\n12\n1\n6\n13\n11\n2\n5\n3\n14\n8\n4\n10\n512\n")
    def test_empty(self):
        self.assertEqual(ApproximationAnswer.get_ada_location_bf(ApproximationAnswer.to_matrix("")), "")
    def test_one(self):
        self.assertEqual(ApproximationAnswer.get_ada_location_bf(ApproximationAnswer.to_matrix("1\n")), "0\n 0\n")
    def test_two(self):
        self.assertEqual(ApproximationAnswer.get_ada_location_bf(ApproximationAnswer.to_matrix("0 3\n 3 0\n")), "0\n 1\n 6\n")
    def test_three(self):
        self.assertEqual(ApproximationAnswer.get_ada_location_bf("0 3 5\n 3 0 7\n 5 7 0\n"), "0\n 1\n 2\n 15\n")
    def test_five(self):
        self.assertEqual(ApproximationAnswer.get_ada_location_bf("0 3 5 9\n 3 0 7 6\n 5 7 0 4\n 9 6 4 0\n"), "0\n 1\n 3\n 2\n 18\n")
if __name__ == '__main__':
    unittest.main()
