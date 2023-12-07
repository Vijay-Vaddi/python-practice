import unittest
from num_guess import guess_num

class TestMain(unittest.TestCase):
      
    def test_number_range(self):
        
        result = guess_num(5,5)
        self.assertTrue(result)
    
    def test_number_range2(self):
        
        result = guess_num(-1,5)
        self.assertFalse(result)
    
    def test_string(self):
        
        result = guess_num('',5)
        self.assertEqual('TypeError', result)


if __name__== '__main__':
    unittest.main()