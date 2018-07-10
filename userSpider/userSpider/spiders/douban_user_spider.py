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

    def start_requests(self):
        base_url = 'https://www.douban.com/people/'


        # 从Redis中读取用户名，拼接url
        r = redis.Redis(connection_pool=redisPool)
        user_ids = r.smembers('userid_wanted')

        headers = {
            'User-Agent': ":Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"
        }

        for user_id in user_ids:
            url = base_url + user_id
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

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
