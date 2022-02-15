import pytest
import sys
from officepy import Dir
from retweet import Bot


class TestCase:
    def test_main(self):
        Bot()

    def test_basic(self):
        from config import Config

        Dir(Config.BASE_DIR).black()
