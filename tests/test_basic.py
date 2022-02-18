import pytest
import sys
from officepy import Dir
from retweet import Bot


class TestCase:
    def test_main(self):
        Bot()

    def test_basic(self):
        from retweetconfig import RetweetConfig as FIG

        Dir(FIG.RETWEET_BASEDIR).black()
