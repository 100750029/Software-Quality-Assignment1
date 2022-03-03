import unittest
from wordlegame import find_fully_correct, remove_fully_correct, find_colour_correct, valid

class Testgametest(unittest.TestCase):
     
    def test_find_fully_correct(self):
        
        self.assertEqual(find_fully_correct(['h','e','l','l','o'], ['h','h','h','h','h']), ['b'], "hello with the guess hhhhh is b")
        
        self.assertEqual(find_fully_correct(['h','e','l','l','o'], ['h','h','h','l','l']), ['b','b'], "hello with the guess hhhhll is bb")

        self.assertEqual(find_fully_correct(['h','e','l','l','o'], ['h','e','l','o','h']), ['b','b','b'], "hello with the guess heloh is bbb")

    
    def test_remove_fully_correct(self):
        
        self.assertEqual(remove_fully_correct(['h','e','l','l','o'], ['h','l','l','h','h']), ['e','l','o'], "hello with the guess hllhh is elo")
        
        self.assertEqual(remove_fully_correct(['h','e','l','l','o'], ['h','o','h','h','o']), ['e','l','l'], "hello with the guess hohho is ell")

        self.assertEqual(remove_fully_correct(['h','e','l','l','o'], ['h','e','l','o','h']), ['l','o'], "hello with the guess heloh is lo")
        
    def test_find_colour_correct(self):
        
        self.assertTrue(find_colour_correct(['y','p','g'], ['g','g','o']) == ['w'], "ypg with the guess ggo is w")
        
        self.assertTrue(find_colour_correct(['w','o','r','s','l'], ['w','o','r','l','s']) == ['w','w'], "worsl with the guess worls is ww")
        
        self.assertTrue(find_colour_correct(['o','p','g','w'], ['w','g','p','o']) == ['w','w','w','w'], "opgw with the guess wgpo is wwww")
        
    def test_valid (self):
        
        self.assertTrue(valid(['h','h','l','l','h'], ['h','e','l','l','o'], 5) == True, "hhllh is a valid guess for the word hello with 5 letters")
        
        self.assertFalse(valid(['h','e','l','l','o'], ['h','e','l'], 5) == True, "hello isn't a valid guess for the word hel with 5 letters")
        
        self.assertTrue(valid(['h','s','s'], ['h','e','l','l','o','s'], 3) == True, "hss is a valid guess for the word hellos with 3 letters")
        
        
        
        
