import unittest
import answer


class TestLast(unittest.TestCase):
    def test_canvasTest(self):
        exampleAssignment = ["14",
            '507 P 10 58\n',
            '507 P 165 56\n',
            '507 P 333 10\n',
            '507 S 426 27\n',
            '507 T 112 31\n',
            '507 T 362 23\n',
            '507 P 427 11\n',
            '507 S 296 60\n',
            '507 S 318 38\n',
            '507 P 306 20\n',
            '507 S 109 20\n',
            '507 T 360 57\n',
            '507 S 119 50\n',
            '507 P 386 55\n']
        self.assertEqual(exampleAssignment, "507 10 386 253\n")
        
   


if __name__ == '__main__':
    unittest.main()        

