import pytest
import sys
from config import *

sys.path.extend([Config.OFFICEPY_DIR, Config.RUMPY_DIR])

from officepy import Dir
from retweet import Bot


class TestCase:
    def test_main(self):
        Bot()

    def test_basic(self):
        Dir(BASEDIR).black()
