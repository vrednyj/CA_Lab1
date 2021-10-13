import unittest

import pkg
from pkg import CA_Lab1,Maths


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(CA_Lab1.run(), 'This will print something to the scree')
        self.run(Maths())


if __name__ == '__main__':
    unittest.main()
