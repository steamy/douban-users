# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst

# def userid_


class UserspiderItem(scrapy.Item):
    user_id = scrapy.Field(

    )
    user_nickname = scrapy.Field()
    signature = scrapy.Field()
    location = scrapy.Field()
    check_in_time = scrapy.Field()
    user_intro = scrapy.Field()
    books_wanted = scrapy.Field()
    books_red = scrapy.Field()
    movies_wanted = scrapy.Field()
    movies_watched = scrapy.Field()
    groups = scrapy.Field()
    dou_list = scrapy.Field()
    follow_by = scrapy.Field()