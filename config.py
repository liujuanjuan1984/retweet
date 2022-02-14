import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    officepy: https://github.com/liujuanjuan1984/officepy
    rumpy: https://github.com/liujuanjuan1984/rumpy
    """

    OFFICEPY_DIR = r"D:\Jupyter\officepy"
    RUMPY_DIR = r"D:\Jupyter\rumpy"
    DATA_DIR = {
        "WEIBO": os.path.join(BASEDIR, "..", "..", "weibo"),
        "TWITTER": os.path.join(BASEDIR, "..", "..", "twitter"),
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

    @staticmethod
    def init_app(app):
        pass


class QuorumConfig(Config):

    HOST = "127.0.0.1"
    PORT = 50415
    SERVER_CRT_FILEPATH = r"C:\Users\75801\AppData\Local\Programs\prs-atm-app\resources\quorum_bin\certs\server.crt"
    GROUP_NAME_WEIBO = "TA们在微博说了啥"
    GROUP_NAME_TWITTER = "TA们在推特说了啥"

    @property
    def as_dict(self):
        return {
            "port": self.PORT,
            "host": self.HOST,
            "appid": "peer",
            "crtfile": self.SERVER_CRT_FILEPATH,
        }
