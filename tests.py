import unittest

import pkg


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(pkg.smile(), ":)")


if __name__ == '__main__':
    unittest.main()
