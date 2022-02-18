import os
from time import sleep
from datetime import datetime
from PIL import Image
from typing import List, Dict
from retweetconfig import RetweetConfig as FIG
from officepy import Dir, JsonFile, Scrawler
from rumpy import RumClient


class Bot:
    """bot: retweet weibo/twitter to rum groups"""

    def __init__(self, env=""):
        """
        users: dict for  `nickname`: `user's homepage url`
        datadir: local dirpath for datastore
        """
        self.env = env.upper() or "WEIBO"

    def news(self, times=1, seconds=1, driver=None):
        """get new content from weibo/twitter"""
        driver = driver or Scrawler().driver

        for i in range(times):
            for user in FIG.USERS[self.env]:
                self._user_news(user, driver)
            sleep(seconds)

    def post(self, times=1, seconds=1, rumclient=None):
        """post content to rum group"""

        rumclient = rumclient or RumClient(**FIG.CLIENT_PARAMS[self.env])

        for i in range(times):
            for user in FIG.USERS[self.env]:
                self._post_to_rum(rumclient, user)
            sleep(seconds)

    def _get_new_posts(self, driver, url: str, data):
        for ir in driver.find_elements_by_xpath(FIG.PTTN[self.env]["new"]):
            i = ir.get_attribute("href")
            name = url.split("/")[-1]
            if i not in data and name in i and "photo" not in i and "?" not in i:
                data[i] = {"add_at": str(datetime.now())}
        return data

    def _user_datafile(self, user):
        dirpath = os.path.join(FIG.DATA_DIR[self.env], user)
        Dir(dirpath).check()
        newsfile = os.path.join(dirpath, "news.json")
        return dirpath, newsfile

    def _user_news(self, user, driver):
        # 每个人创建专属目录
        dirpath, newsfile = self._user_datafile(user)
        data = JsonFile(newsfile).read({})

        url = FIG.USERS[self.env][user]
        driver.get(url)
        sleep(20)
        # 读取新内容
        data = self._get_new_posts(driver, url, data)
        JsonFile(newsfile).write(data)

        for iurl in data:
            if "pic_at" not in data[iurl]:
                driver.get(iurl)
                sleep(10)
                pic_filepath = dirpath + "\\" + iurl.split("/")[-1] + ".png"
                try:
                    text = self._one_post_to_pic(driver, pic_filepath)
                    data[iurl]["text"] = "".join(
                        [user, ": ", text, "\n\norgin: ", iurl]
                    )
                    data[iurl]["pic_at"] = str(datetime.now())
                    data[iurl]["pic"] = pic_filepath
                except Exception as e:
                    print(iurl)
                    print(e)
                    continue

        JsonFile(newsfile).write(data)

    def _one_post_to_pic(self, driver, pic_filepath: str):
        """read one post ,store post screen png, return post text"""

        text = driver.find_element_by_xpath(FIG.PTTN[self.env]["text"]).text
        post = driver.find_element_by_xpath(FIG.PTTN[self.env]["post"])
        temp_pic = os.path.join(FIG.DATA_DIR[self.env], "temp.png")
        driver.save_screenshot(temp_pic)

        """计算页面元素的在整个页面上的坐标"""
        left = post.location["x"]
        top = post.location["y"]
        right = post.size["width"] + left
        bottom = post.size["height"] + top
        sleep(2)

        """"根据页面元素的坐标，截图元素"""
        ele = Image.open(temp_pic)
        ele = ele.crop((left, top, right, bottom))
        ele.save(pic_filepath)
        return text

    def _post_to_rum(self, rumclient, user: str):
        dirpath, newsfile = self._user_datafile(user)

        data = JsonFile(newsfile).read({})

        for url in data:
            if "push_at" not in data[url]:
                if "text" in data[url] and "pic" in data[url]:
                    rumclient.group.send_note(
                        FIG.GROUPS[self.env],
                        content=data[url]["text"],
                        image=[data[url]["pic"]],
                    )
                    data[url]["push_at"] = str(datetime.now())
                    sleep(30)
        JsonFile(newsfile).write(data)
