#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: balicanta
# @Date:   2014-10-25 09:57:26
# @Last Modified by:   balicanta
# @Last Modified time: 2014-10-25 10:47:53

from NewsParser import NewsParser
from requests.utils import get_encodings_from_content

test_fixtures = [
    {"url": "http://udn.com/NEWS/NATIONAL/NAT3/9017464.shtml",
        "title": "聯合報直擊", "author": "呂思逸"}
]


def test_parser():

    for test_fixture in test_fixtures:
        parser = NewsParser(test_fixture['url'])
        title = parser.getTitle()
        author = parser.getAuthor()

        assert test_fixture['title'] in title.encode('utf-8')
        assert test_fixture['author'] in author.encode('utf-8')
