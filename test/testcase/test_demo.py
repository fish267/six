import unittest

from six import add, haha


class TestSixConfig(unittest.TestCase):
    def test_add(self):
        haha()
        self.assertEqual(3, add(1, 2))