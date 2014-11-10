#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: balicanta
# @Date:   2014-10-25 09:57:26
# @Last Modified by:   bustta
# @Last Modified time: 2014-11-10 15:24:09


from ..NewsParser import NewsParser
from requests.utils import get_encodings_from_content

test_fixtures = [
    {"url": "http://udn.com/NEWS/NATIONAL/NAT3/9017464.shtml",
        "title": "聯合報直擊", "author": "呂思逸","content":"是由陳老闆批了棉花棒"},
    {"url": "http://world.yam.com/post.php?id=2732",
        "title": "海潮人潮兇", "author":"", "content": "這座遊人如織的水都"},
    {"url": "http://news.ltn.com.tw/news/business/breakingnews/1142153",
        "title": "魏家退出101", "author":"", "content": "財政部次長吳當傑今天傍晚表示"},
    {"url": "http://www.anntw.com/articles/20141031-GrlZ",
        "title": "立法治樹典範", "author":"杜胤廣", "content": "因看見偏鄉農民生活困"},
    {"url": "http://www.coolloud.org.tw/node/80590",
        "title": "澳洲打工遭台商剝削", "author":"王顥中", "content": "青年勞動九五聯盟29日上午召開記者會"},
    {"url": "http://www.peoplenews.tw/news/80a3de53-1c06-4d30-a330-b76e335132f7",
        "title": "協助弱勢募款", "author":"朱蒲青", "content": "沒有什麼假想敵啦"},
    {"url": "http://news.tvbs.com.tw/entry/553577",
        "title": "柯文稿得人心", "author":"盧冠妃", "content": "我說過我是墨綠"}
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
