import unittest

import pkg
from pkg import CA_Lab1,Maths


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(CA_Lab1.run(), 'This will print something to the screen',"Test 1 PASS")
        self.assertEqual(Maths.numbers(), "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]","Test 2 PASS")
        self.assertNotEqual(Maths.numbers(), "[1, 2, 3, 4, 5, 6, 7, 8, 0]","Test 3 PASS")
        

if __name__ == '__main__':
    unittest.main()
