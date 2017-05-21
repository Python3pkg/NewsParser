#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: DinoLai
# @Date:   2014-11-08 23:06:56
# @Last Modified by:   DinoLai
# @Last Modified time: 2014-11-09 01:54:31

from .AbstractNewsParseStrategy import AbstractNewsParseStrategy


class StormMediaGroupParseStrategy(AbstractNewsParseStrategy):

    def isURLMatch(self, url):
        return ".stormmediagroup.com" in url

    def getTitle(self, beautiful_soup_object):
        return beautiful_soup_object.select('.innerBigNewsTitle')[0].text

    def getAuthor(self, beautiful_soup_object):
        return beautiful_soup_object.select('.innerNewsInfo > a')[0].text

    def getContent(self, beautiful_soup_object):
        #beautiful_soup_object.select('.newsDescBlk')[0].style.decompose()
        return beautiful_soup_object.select('.newsDescBlk')[0].text

    def getPublishDate(self, beautiful_soup_object):
        return beautiful_soup_object.select('.innerNewsInfo')[0].text
