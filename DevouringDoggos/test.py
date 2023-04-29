import unittest
import answer as dogAnswer

class TestDevour():
     def test_given_input(self):
        actual = dogAnswer.dog_devour("5 15 Textbook 4 50 HardDrive 10 2 DogFood 10 5 FavoriteGame 20 60 SuperComputer 100 100")
        self.assertEqual(actual, "Textbook DogFood 55")
     def test_zeros(self):
        actual = dogAnswer.dog_devour("5 15 Textbook 0 0 HardDrive 0 0 DogFood 0 0 FavoriteGame 0 0 SuperComputer 0 0")
        self.assertEqual(actual, "Textbook DogFood 0")
     def test_wild(self):
         actual = dogAnswer.dog_devour("4 15 Snake 5 55 DogFood 10 5 Snail 15 1 Fish 10 10")   
         self.assertEqual(actual, "DogFood Fish 65")

if __name__ == '__main__':
    unittest.main() 
