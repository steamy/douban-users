# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .db.db_engine import DBsession
from .models.user import User
from .redis_pool import redisPool
import redis

class UserspiderPipeline(object):
    def process_item(self, item, spider):
        # 存入Mysql
        session = DBsession()
        new_user = User(user_id=item['user_id'],
                        user_nickname=item['user_nickname'],
                        signature=item['signature'],
                        location=item['location'],
                        check_in_time=item['check_in_time'],
                        user_intro=item['user_intro'],
                        books_wanted=item['books_wanted'],
                        books_red=item['books_red'],
                        movies_wanted=item['movies_wanted'],
                        movies_watched=item['movies_watched'],
                        groups=item['groups'],
                        dou_list=item['dou_list'])
        session.add(new_user)
        session.commit()
        session.close()
        #将关注人的用户id存入Redis
        user_ids = item['follow_by'].split(' ')
        r = redis.Redis(connection_pool=redisPool)
        #将'userid_wanted'中的数据存入'userid_used'
        r.sunionstore('userid_used', 'userid_used', 'userid_wanted')
        #清除'userid_wanted'
        # r.delete('userid_wanted')
        #将该用户关注的人写入'userid_wanted'
        r.sadd('userid_wanted', *user_ids)
        #diff存储
        r.sdiffstore('userid_wanted', 'userid_wanted', 'userid_used')
        return item
