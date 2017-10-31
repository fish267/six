import sys
import unittest

from six_web.cli import _cli_parse


class TestSixConfig(unittest.TestCase):
    def test_add(self):
        test_args = sys.argv
        test_args.append('--version')
        test_args.append('-bind 127.0.0.1:8888')
        _cli_parse(test_args)
