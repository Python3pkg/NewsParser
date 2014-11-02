#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2014-11-02 12:43:04
# @Last Modified by:   bustta
# @Last Modified time: 2014-11-02 12:46:38
from AbstractNewsParseStrategy import AbstractNewsParseStrategy


class AnntwNewsParseStrategy(AbstractNewsParseStrategy):

    def isURLMatch(self, url):
        # http://www.anntw.com/articles/20141031-GrlZ
        return ".anntw.com" in url

    def getTitle(self, beautiful_soup_object):
        title = beautiful_soup_object.find(
            "div", "content-pad").h3.text.encode("utf-8").strip()
        return title

    def getAuthor(self, beautiful_soup_object):
        author = beautiful_soup_object.find(
            "div", "meta-block").a.text.encode("utf-8")
        return author

    def getContent(self, beautiful_soup_object):
        content_div = beautiful_soup_object.find(
            "div", "markdown-body").find_all("p")
        content = "\n".join(para.text.encode(
            "utf-8").strip() for para in content_div)

        return content

    def getPublishDate(self, beautiful_soup_object):
        time = beautiful_soup_object.find(
            "div", "meta-block").find_all("span")[1].text
        return time
