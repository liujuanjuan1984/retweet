# retweet

bot: retweet weibo/twitter to rum groups

### config

update [config.py](./coinfig.py) before running.

### requirements

```sh

pip install -r requirements.txt

```

and install modules:

- officepy: <https://github.com/liujuanjuan1984/officepy>
- rumpy: <https://github.com/liujuanjuan1984/rumpy>


### how to use

Simple as:

```python

from retweet import Bot

Bot().news() # get new-posts from social-network
Bot().post() # retweet to rum group.

```
