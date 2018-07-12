#!/usr/bin/python3 
# -*- coding: utf-8 -*-
# Filename:  start.py
# Author： steam
# Time    : 2018/7/10 上午11:02

'''
    爬虫控制程序
'''
import redis
from userSpider.redis_pool import redisPool

# redisPool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)

def initializeRedis():
    '''
    初始化Redis数据库
    :return:
    '''
    #清空userid_used, userid_wanted
    r=redis.Redis(connection_pool=redisPool)
    r.delete('userid_used', 'userid_wanted')
    #初始化userid_wanted
    r.sadd('userid_wanted', '147681591')
    r.sadd('userid_used','404')
    # 'bedtimepoem', 'huangxiaoer', 'ArchiHY', '41745938')

if __name__ == '__main__':
    initializeRedis()

