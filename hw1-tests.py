import unittest
import hw1

# This is the test suite; it contains test cases for the addone function
class TestAddOne(unittest.TestCase):
    
    # test addone when called on an empty list
    def test_empty(self):
        # self.assertEqual takes two arguments. If they are NOT equal
        # then the test fails
        result = hw1.addone([])
        expected = []
        self.assertEqual(result, expected)
    
    # test addone when called on a list containing one element
    def test_one(self):
        result = hw1.addone([10])
        expected = [11]
        self.assertEqual(result, expected)
        
    # test addone when called on a list with lots of elements
    
    
    # testaddone when called on a list containing one element
    # and make sure that addone does not modify the original list
    
    
    # testaddone when called on a list containing lots of elements
    # and make sure that addone does not modify the original list 
    

if __name__ == '__main__':
    unittest.main()