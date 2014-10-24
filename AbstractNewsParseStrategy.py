#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Balicanta.Yao
# @Date:   2014-10-24 13:34:05
# @Last Modified by:   balicanta
# @Last Modified time: 2014-10-25 00:10:19
 
from abc import ABCMeta, abstractmethod

class AbstractNewsParseStrategy():
 
	__metaclass__ = ABCMeta
 
	# 檢驗傳入的 URL 是否符合用此 Strategy
	@abstractmethod
	def isURLMatch(self, url):
		pass
 
	# 取得新聞的標題
	@abstractmethod
	def getTitle(self, html_content):
		pass
 
	# 取得記者名稱
	@abstractmethod
	def getAuthor(self, html_content):
		pass
 
	@abstractmethod
	def getAuthor(self, html_content):
		pass
 
	def getPublishDate(self, html_content):
		pass
 
 
