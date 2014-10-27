#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: balicanta
# @Date:   2014-10-25 09:57:26
# @Last Modified by:   bustta
# @Last Modified time: 2014-10-27 23:22:08

from NewsParser import NewsParser
from requests.utils import get_encodings_from_content

test_fixtures = [
    {"url": "http://udn.com/NEWS/NATIONAL/NAT3/9017464.shtml",
        "title": "聯合報直擊", "author": "呂思逸"},
    {"url": "http://world.yam.com/post.php?id=2732",
        "title": "海潮人潮兇", "content": "這座遊人如織的水都"},
    {"url": "http://news.ltn.com.tw/news/business/breakingnews/1142153",
        "title": "魏家退出101", "content": "財政部次長吳當傑今天傍晚表示"}
]


def test_parser():

    for test_fixture in test_fixtures:
        parser = NewsParser(test_fixture['url'])
        title = parser.getTitle()
        author = parser.getAuthor()
        content = parser.getContent()

        assert test_fixture['title'] in title.encode('utf-8')
        assert test_fixture['author'] in author.encode('utf-8')
        assert test_fixture['content'] in content.encode('utf-8')
