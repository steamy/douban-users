#!/usr/bin/python3 
# -*- coding: utf-8 -*-
# Filename:  douban_user_spider.py
# Author： steam
# Time    : 2018/7/10 上午9:55

import scrapy
import redis
from ..redis_pool import redisPool
from ..items import UserspiderItem
from ..loaders import UserLoader

class DoubanUserSpider(scrapy.Spider):
    name = 'users'
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES':{
            'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None,
            'userSpider.middlewares.MyUserAgentMiddleware': 400,
            'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 123,
            'userSpider.middlewares.MyHttpProxyMiddleware': 125,
            'userSpider.middlewares.UserspiderDownloaderMiddleware': 543,
        },
        'ITEM_PIPELINES':{
            'userSpider.pipelines.UserspiderPipeline': 300,
        }
    }

    def start_requests(self):
        base_url = 'https://www.douban.com/people/'


        # 从Redis中读取用户名，拼接url
        r = redis.Redis(connection_pool=redisPool)
        #除去userid_wanted中已经爬取的用户
        r.sdiffstore('userid_wanted', 'userid_wanted', 'userid_used')
        user_ids = r.smembers('userid_wanted')


        for user_id in user_ids:
            url = base_url + user_id
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        userLoader = UserLoader(item=UserspiderItem(), response=response)
        userLoader.add_xpath('user_id','//div[@class="basic-info"]//div[@class="user-info"]//div[@class="pl"]//text()')
        userLoader.add_xpath('user_nickname', '//h1/text()')
        userLoader.add_xpath('check_in_time', '//div[@class="basic-info"]//div[@class="user-info"]//div[@class="pl"]//text()')
        userLoader.add_xpath('location',
                             '//div[@class="basic-info"]//div[@class="user-info"]//a//text()')
        userLoader.add_xpath('signature','//h1//div[@class="signature_display pl"]//text()')
        userLoader.add_xpath('user_intro','//div[@class="user-intro"]//div[@class="j edtext pl"]//span//text()')
        # print(userLoader.load_item())
        userLoader.add_xpath('books_wanted','//div[@id="book"]//div[2]//ul//a//@title')
        userLoader.add_xpath('books_red', '//div[@id="book"]//div[1]//ul//a//@title')
        userLoader.add_xpath('movies_wanted', '//div[@id="movie"]//div[2]//ul//a//@title')
        userLoader.add_xpath('movies_watched', '//div[@id="movie"]//div[1]//ul//a//@title')
        userLoader.add_xpath('groups', '//div[@id="group"]//dd//a//text()|//div[@id="group"]//dd//span//text()')
        userLoader.add_xpath('dou_list', '//ul[@class="doulist-list"]//a//text()')
        userLoader.add_xpath('follow_by','//div[@id="friend"]//dl[@class="obu"]//dt//a//@href')
        return userLoader.load_item()
