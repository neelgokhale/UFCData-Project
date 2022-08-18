#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   spider.py
@Time    :   2022/08/17 13:22:54
@Author  :   Neel Gokhale
@Contact :   neelg14@gmail.com
@License :   (C)Copyright 2020-2021, Neel Gokhale
'''

from scrapy.spiders import Spider
from scrapy.loader import ItemLoader
from scrapy.exceptions import CloseSpider
from scrapy import signals

from ufcdata.items import *

class PerformanceSpider(Spider):
    name = 'performance'
    start_urls = ['http://ufcstats.com/statistics/events/completed?page=all']
    
    def __init__(self, *args, **kwargs):
        super(PerformanceSpider, self).__init__(*args, **kwargs)
        
    