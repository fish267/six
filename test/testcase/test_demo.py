import unittest

from six_web.config import CallClass
from six_web.six import add, haha


class TestSixConfig(unittest.TestCase):
    def test_add(self):
        haha()
        self.assertEqual(3, add(1, 2))

    def test_call(self):
        call = CallClass(3)
        call(1)
        call(1)
        print(call.value)



