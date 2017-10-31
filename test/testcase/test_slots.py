import unittest

from six_web.six import add

count = 1000000


class TestSlots(unittest.TestCase):
    def test_with_slots(self):
        print('with')
        # big_set = [WithSlots() for i in range(count)]
        self.assertEqual(3, add(1, 2))

    def test_without_slots(self):
        print('without')
        big_set = [WithoutSlots() for i in range(count)]
        self.assertEqual(3, add(1, 2))


class WithoutSlots():
    def __init(self, name, desc, props):
        self.name = name
        self.desc = desc
        self.props = props


class WithSlots():
    __slots__ = ('_name', '_desc', '_props')

    def __init(self, name, desc, props):
        self.name = name
        self.desc = desc
        self.props = props
