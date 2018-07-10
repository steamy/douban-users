#!/usr/bin/python3 
# -*- coding: utf-8 -*-
# Filename:  db_engine.py
# Author： steam
# Time    : 2018/7/10 下午5:01

from  sqlalchemy import create_engine
from  sqlalchemy.orm import sessionmaker
from .config import get_db_connection_url



engine = create_engine(get_db_connection_url())

DBsession = sessionmaker(bind=engine)