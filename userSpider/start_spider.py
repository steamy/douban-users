#!/usr/bin/python3 
# -*- coding: utf-8 -*-
# Filename:  start_spider.py
# Author： steam
# Time    : 2018/7/10 下午12:59

import subprocess
import time
num = 1

while True:
    start_ip_cmd = 'scrapy crawl users -s LOG_FILE=user'+str(num)+'.log'
    print(start_ip_cmd)
    user = subprocess.Popen(start_ip_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    user.wait()
    num = num + 1
    time.sleep(300)
