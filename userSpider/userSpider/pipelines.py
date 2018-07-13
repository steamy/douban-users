# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .db.db_engine import DBsession
from .models.user import User
import redis
from telnetlib import Telnet
from multiprocessing.dummy import Pool as ThreadPool
import datetime
from .redis_pool import redisPool
from redis import Redis

class UserspiderPipeline(object):
    def process_item(self, item, spider):

        if True:
            # 存入Mysql
            session = DBsession()
            new_user = User(user_id=item.get('user_id', ''),
                            user_nickname=item.get('user_nickname', ''),
                            signature=item.get('signature', ''),
                            location=item.get('location', ''),
                            check_in_time=item.get('user_nickname', ''),
                            user_intro=item.get('user_intro', ''),
                            books_wanted=item.get('books_wanted', ''),
                            books_red=item.get('books_red', ''),
                            movies_wanted=item.get('movies_wanted', ''),
                            movies_watched=item.get('movies_watched', ''),
                            groups=item.get('groups', ''),
                            dou_list=item.get('dou_list', ''))

            session.add(new_user)
            session.commit()
            session.close()
        if True:
            # 将关注人的用户id存入Redis
            user_ids = item.get('follow_by', '').split(' ')
            r = redis.Redis(connection_pool=redisPool)
            # 将'userid_wanted'中的数据存入'userid_used'
            # r.sunionstore('userid_used', 'userid_used', 'userid_wanted')
            # 清除'userid_wanted'
            # r.delete('userid_wanted')
            # 将该用户关注的人写入'userid_wanted'
            r.sadd('userid_wanted', *user_ids)
            r.sadd('userid_used',item.get('user_id',''))
        return item


class ProxyIpspiderPipeline(object):

    def telnet_test(self, url):
        ip = url.split('/')[2]
        host, port = ip.split(':')
        try:
            Telnet(host, port=port, timeout=2)
        except:
            return 'unavail'
        else:
            return url

    def process_item(self, item, spider):
        all_ips = list(set(item.get('xici_ips',[])).union(item.get('data5u_ips',[]), item.get('ip66_ips',[])))
        # 测试ip是否可用
        pool = ThreadPool(10)
        available_ips = list(set(pool.map(self.telnet_test,all_ips)))
        pool.close()
        pool.join()
        available_ips.remove('unavail')
        print(available_ips)
        #存入redis中
        r = Redis(connection_pool=redisPool)
        r.delete('ip_pool')
        r.sadd('ip_pool', *available_ips)
