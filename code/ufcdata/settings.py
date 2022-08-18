#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   settings.py
@Time    :   2022/08/17 13:54:25
@Author  :   Neel Gokhale
@Contact :   neelg14@gmail.com
@License :   (C)Copyright 2020-2021, Neel Gokhale
'''

BOT_NAME = 'ufcdata'
SPIDER_MODULES = ['ufcdata.spider']
NEWSPIDER_MODULE = 'ufcdata.spider'

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'neelgokhale',
    'password': '',
    'database': 'ufcdata'
}