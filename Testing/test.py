import re
from main import do_stuff
import unittest


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = do_stuff(test_param)
        self.assertEqual(result, 20)

    def test_do_stuff2(self):
        test_param_2 = r'[a-zA-Z]'
        result = do_stuff(test_param_2)
        self.assertTrue(isinstance(result, ValueError))
        #can use self.assertIsInstance()

    def test_do_stuff3(self):
        test_param_3 = None
        result = do_stuff(test_param_3)
        self.assertEqual(result, 'Please enter number')
    
    def test_do_stuff4(self):
        test_param_4 = ''
        result = do_stuff(test_param_4)
        self.assertEqual(result, 'Please enter number')
    


unittest.main() #not based on the name of main.py file. 

# common practice is to try and break things until it becomes perfect. 
# readablilty is really important in tests so write more discriptive test code