#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   pipelines.py
@Time    :   2022/08/18 12:31:31
@Author  :   Neel Gokhale
@Contact :   neelg14@gmail.com
@License :   (C)Copyright 2020-2021, Neel Gokhale
'''

from itemadapter import ItemAdapter
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from ufcdata.items import *
from ufcdata.models import *


class UfcDataPipeline():
    def __init__(self):
        """
        Initializes database connection and session, creates postgres table
        """
        
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)
        
    def process_item(self, item, spider) -> Item:
        """Load scrapy Item to postgres database

        Args:
            `item` (`Item`): scrapy Item

        Returns:
            `Item`: scrapy Item
        """
        
        session = self.Session()
        
        if isinstance(item, Event):
            ufc_item = EventTable(**item)
        elif isinstance(item, Fight):
            ufc_item = FightTable(**item)
        elif isinstance(item, Round):
            ufc_item = RoundTable(**item)
        elif isinstance(item, RoundStat):
            ufc_item = RoundStatsTable(**item)
        elif isinstance(item, Fighter):
            ufc_item = FighterTable(**item)
        else:
            return item
        
        try:
            session.add(ufc_item)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
            
        return item
