#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2014-10-25 22:53:39
# @Last Modified by:   bustta
# @Last Modified time: 2014-10-25 23:45:18
from AbstractNewsParseStrategy import AbstractNewsParseStrategy

class WorldYamParseStrategy(AbstractNewsParseStrategy):

    def isURLMatch(self, url):
        # http://world.yam.com/post.php?id=2732
        return "world.yam.com" in url

    def getTitle(self, beautiful_soup_object):
        article_area = beautiful_soup_object.find("article", "mainBox")
        title = article_area.find("header").h2.text.encode('utf-8')
        return title

    def getAuthor(self, beautiful_soup_object):
        return "WorldYam"

    def getContent(self, beautiful_soup_object):
        article_area = beautiful_soup_object.find("article", "mainBox")
        all_paragraph = article_area.find_all("p")
        content = ""
        for idx in range(len(all_paragraph)):
            content += all_paragraph[idx].text.encode('utf-8').strip()

        return content

    def getPublishDate(self, beautiful_soup_object):
        article_area = beautiful_soup_object.find("article", "mainBox")
        time = article_area.find("header").time.text.encode('utf-8')
        return time
