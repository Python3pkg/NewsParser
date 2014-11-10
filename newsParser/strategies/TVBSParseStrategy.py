#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2014-11-08 15:08:01
# @Last Modified by:   bustta
# @Last Modified time: 2014-11-10 15:22:42

from AbstractNewsParseStrategy import AbstractNewsParseStrategy


class TVBSParseStrategy(AbstractNewsParseStrategy):

    def isURLMatch(self, url):
        # http://news.tvbs.com.tw/entry/553577
        return "news.tvbs.com" in url

    def getTitle(self, beautiful_soup_object):
        return beautiful_soup_object.select('title')[0].text

    def getAuthor(self, beautiful_soup_object):
        return beautiful_soup_object.select('.reporter')[0].text

    def getContent(self, beautiful_soup_object):
        beautiful_soup_object.find("div", "content").script.decompose()
        content = beautiful_soup_object.find(
            "div", "content").text.encode('utf-8').replace("\n", "")
        return content

    def getPublishDate(self, beautiful_soup_object):
        return beautiful_soup_object.select('#w3s')[0].text
