#!/usr/bin/python3 
# -*- coding: utf-8 -*-
# Filename:  redis_pool.py
# Author： steam
# Time    : 2018/7/10 上午11:44

from redis import ConnectionPool

redisPool = ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
