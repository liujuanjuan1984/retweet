import os
from rumpyconfig import RumpyConfig


class RetweetConfig:
    RETWEET_BASEDIR = os.path.dirname(__file__)
    print(RETWEET_BASEDIR)

    DATA_DIR = {
        "WEIBO": os.path.join(RETWEET_BASEDIR, "..", "..", "weibo"),
        "TWITTER": os.path.join(RETWEET_BASEDIR, "..", "..", "twitter"),
    }

    USERS = {
        "WEIBO": {"新浪区块链": "https://weibo.com/6522911909"},
        "TWITTER": {},
    }

    PTTN = {
        "WEIBO": {
            "new": r'//a[starts-with(@href,"https://weibo.com/")]',
            "text": r'//*[@id="app"]/div[1]/div[2]/div[2]/main//div/div/div[2]/article/div[2]/div/div[1]/div',
            "post": r'//*[@id="app"]/div[1]/div[2]/div[2]/main/div/div/div[2]/article/div[2]',
        },
        "TWITTER": {},
    }

    GROUPS = {
        "WEIBO": "d4368f3e-98c4-4dac-8f3f-e64337b8a793",
        "TWITTER": "d4368f3e-98c4-4dac-8f3f-e64337b8a793",
    }

    GROUP_NAME_WEIBO = "TA们在微博说了啥"
    GROUP_NAME_TWITTER = "TA们在推特说了啥"
    CLIENT_PARAMS = RumpyConfig.CLIENT_PARAMS

    @staticmethod
    def init_app(app):
        pass
