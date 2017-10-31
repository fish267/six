import sys
import unittest

from six_web import __version__
from six_web.cli import _main


class TestSixConfig(unittest.TestCase):
    def test_add(self):
        test_args = sys.argv
        test_args.append('--version')
        self.assertEqual(__version__, _main(test_args))
