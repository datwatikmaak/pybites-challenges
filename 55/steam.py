from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    d = feedparser.parse(FEED_URL)

    steam_rss = []

    for entry in d["entries"]:
        title = entry.title
        link = entry.link

        steam_rss.append((title, link))

    print(steam_rss)
    print(type(steam_rss))


get_games()
