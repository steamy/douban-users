#!/usr/bin/python3 
# -*- coding: utf-8 -*-
# Filename:  user.py
# Author： steam
# Time    : 2018/7/10 下午5:01

from  sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
Base = declarative_base()

class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(30), nullable=False, default='')
    user_nickname = Column(String(30), nullable=False, default='')
    signature = Column(String(50), nullable=False, default='')
    location = Column(String(20), nullable=False, default='')
    check_in_time = Column(String(30), nullable=False, default='')
    user_intro = Column(String(200), nullable=False, default='')
    books_wanted = Column(String(200), nullable=False, default='')
    books_red = Column(String(200), nullable=False, default='')
    movies_wanted = Column(String(200), nullable=False, default='')
    movies_watched = Column(String(200), nullable=False, default='')
    groups = Column(String(200), nullable=False, default='')
    dou_list= Column(String(200), nullable=False, default='')


