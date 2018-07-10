#!/usr/bin/python3 
# -*- coding: utf-8 -*-
# Filename:  start_spider.py
# Author： steam
# Time    : 2018/7/10 下午12:59

from scrapy import cmdline

cmdline.execute('scarpy crawl users'.split())