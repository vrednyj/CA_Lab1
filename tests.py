import unittest

import pkg
from pkg import CA_Lab1,Maths


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(CA_Lab1.run(), 'This will print something to the screen')
        self.run(Maths.numbers())


if __name__ == '__main__':
    unittest.main()
