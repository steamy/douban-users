#!/usr/bin/python3 
# -*- coding: utf-8 -*-
# Filename:  config.py
# Author： steam
# Time    : 2018/7/10 下午5:00

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}"

def get_db_connection_url():

    return DB_URI.format(
        user = 'root',
        password = 'steam',
        host = '127.0.0.1',
        port = '3306',
        db = 'douban'
    )