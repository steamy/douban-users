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
import subprocess
import datetime
import time

# redisPool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)

def initializeRedis():
    '''
    初始化Redis数据库
    :return:
    '''
    #清空userid_used, userid_wanted
    r=redis.Redis(connection_pool=redisPool)
    r.delete('userid_used', 'userid_wanted','ip_pool')
    #初始化userid_wanted
    r.sadd('userid_wanted', '147681591','bedtimepoem', 'huangxiaoer', 'ArchiHY', '41745938')
    r.sadd('userid_used','404')
    r.sadd('ip_pool','none')


if __name__ == '__main__':
    # initializeRedis()
    num = 1
    while True:
        start_ip_cmd = 'scrapy crawl proxy -s LOG_FILE=ip.'+str(num)+'log'
        proxy = subprocess.Popen(start_ip_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        proxy.wait()
        print(proxy.pid)
        time.sleep(200)
        num = num + 1
        print(num)







