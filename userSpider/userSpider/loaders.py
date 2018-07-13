#!/usr/bin/python3 
# -*- coding: utf-8 -*-
# Filename:  loaders.py
# Author： steam
# Time    : 2018/7/10 下午2:28

from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity, TakeFirst, MapCompose, Join, Compose

def filter_user_id(text):
    return text.strip()

def format_nickname(text):
    return text.replace('\n','')
def format_checkin_time(text):
    return text.replace('加入','').strip()
def format_books(text):
    return text.replace('\n',' ')
def format_movies(text):
    return text.replace('\n',' ')
def format_group(text):
    return text.replace('\n','')
def get_userid_from_followby(url):
    return url.split('/')[-2]

def test(r):
    print(r)

class UserLoader(ItemLoader):
    default_output_processor = TakeFirst()

    user_id_in = Compose(lambda v: v[0], str.strip)
    check_in_time_in = Compose(lambda v: v[1], format_checkin_time)
    user_nickname_in = MapCompose(str.strip, format_nickname)
    location_in = MapCompose(str.strip)
    signature_in = Identity()
    user_intro_out = Join('\n')

    books_red_in = MapCompose(format_books)
    books_wanted_in = MapCompose(format_books)
    books_wanted_out = Join(';')
    books_red_out = Join(';')

    movies_wanted_in = MapCompose(format_movies)
    movies_wanted_out = Join(';')

    movies_watched_in = MapCompose(format_movies)
    movies_watched_out = Join(';')

    groups_in = MapCompose(format_group)
    groups_out = Join(';')

    dou_list_out = Join(';')

    follow_by_in = MapCompose(get_userid_from_followby)
    follow_by_out = Join()