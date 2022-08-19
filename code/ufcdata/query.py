#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   query.py
@Time    :   2022/08/17 13:31:10
@Author  :   Neel Gokhale
@Contact :   neelg14@gmail.com
@License :   (C)Copyright 2020-2021, Neel Gokhale
'''

import datetime
from itertools import product

import pandas as pd
from itemadapter import ItemAdapter
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from unidecode import unidecode

from ufcdata.models import *


class DatabaseQuery():
    def __init__(self):
        """
        Initialize database connection and session maker.
        """
        
        self.engine = db_connect()
        self.Sesion = sessionmaker(bind=self.engine)
        
    # UPDATING RECORDS
    
    def update_judge_scores(self, fight_id, scores):
        """Update judge scores

        Args:
            `fight_id` (`str`): unique fight id
            `scores` (`tuple`): scores of judges
        """
        
        try:
            update_command = 'UPDATE fights SET {}=\'{}\' WHERE fight_id=\'{}\''
            self.engine.execute(update_command.format('judge1_fighter1', scores[0], fight_id))
            self.engine.execute(update_command.format('judge1_fighter2', scores[1], fight_id))
            self.engine.execute(update_command.format('judge2_fighter1', scores[2], fight_id))
            self.engine.execute(update_command.format('judge2_fighter2', scores[3], fight_id))
            self.engine.execute(update_command.format('judge3_fighter1', scores[4], fight_id))
            self.engine.execute(update_command.format('judge3_fighter2', scores[5], fight_id))
        except:
            pass
        
    def update_deductions(self, fight_id, deductions):
        """Update deductions

        Args:
            `fight_id` (`str`): unique fight id
            `deductions` (`str`): deductions
        """
        try:
            self.engine.execute(f'UPDATE fights SET deductions=\'{deductions}\' WHERE fight_id=\'{fight_id}\'')
        except:
            pass
    
    def update_judge_names(self, fight_id, judge_names):
        """Update judge names

        Args:
            `fight_id` (`str`): unique fight id
            `judge_names` (`str`): judge names
        """
        
        try:
            update_command = 'UPDATE fights SET {}=\'{}\' WHERE fight_id=\'{}\''
            self.engine.execute(update_command.format('judge1', judge_names[0], fight_id))
            self.engine.execute(update_command.format('judge2', judge_names[1], fight_id))
            self.engine.execute(update_command.format('judge3', judge_names[2], fight_id))
        except:
            pass
        
    def update_round_scores(self, fight_id, scores):
        """Update round scores

        Args:
            `fight_id` (`str`): unique fight id
            `scores` (`tuple`): scores for round
        """
        
        try:
            update_command = 'UPDATE rounds SET {}=\'{}\' WHERE rd_id=\'{}\''
            for i in range(len(scores[0])):
                self.engine.execute(update_command.format('judge1_fighter1', scores[0][i], fight_id+'-'+str(i + 1)))
                self.engine.execute(update_command.format('judge1_fighter2', scores[1][i], fight_id+'-'+str(i + 1)))
                self.engine.execute(update_command.format('judge2_fighter1', scores[2][i], fight_id+'-'+str(i + 1)))
                self.engine.execute(update_command.format('judge2_fighter2', scores[3][i], fight_id+'-'+str(i + 1)))
                self.engine.execute(update_command.format('judge3_fighter1', scores[4][i], fight_id+'-'+str(i + 1)))
                self.engine.execute(update_command.format('judge3_fighter2', scores[5][i], fight_id+'-'+str(i + 1)))
        except:
            pass

    # DELETING RECORDS
        
    def delete_event_record(self, event_id):
        self.engine.execute('DELETE FROM events WHERE event_id=\'' + event_id + '\'')
    
    def delete_fight_record(self, fight_id):
        self.engine.execute('DELETE FROM fights WHERE fight_id=\'' + fight_id + '\'')
    
    def delete_round_record(self, rd_id):
        self.engine.execute('DELETE FROM rounds WHERE rd_id=\'' + rd_id + '\'')
    
    def delete_round_result_record(self, rd_result_id):
        self.engine.execute('DELETE FROM round_stats WHERE rd_result_id=\'' + rd_result_id + '\'')
    
    def delete_fighter_record(self, fighter_id):
        self.engine.execute('DELETE FROM fighters WHERE fighter_id=\'' + fighter_id + '\'')    
    
    # GENERAL QUERIES
        
    def query_event_list(self):
        db_events = self.engine.execute('SELECT event_id FROM events')
        return [x.event_id for x in db_events]
    
    def query_last_fight(self, fighter_id) -> dict:
        """Determines a fighter's most recent fight and returns details.

        Args:
            `fighter_id` (`str`): unique fighter id
            
        Returns:
            `dict`: latest fight details
        """
        
        last_fight = self.engine.execute(
            'SELECT fights.event_id, weightclass, fighter_1_id, fighter_2_id, event_date FROM fights ' + 
            'INNER JOIN events ON fights.event_id=events.event_id ' +
            'WHERE fighter_1_id=\''+fighter_id+'\' or fighter_2_id=\''+fighter_id+'\' ' +
            'ORDER BY event_date DESC ' + 
            'LIMIT 1')
        
        return last_fight
        
    def query_fight_id(self, fighter_1, fighter_2, date, last_only=False) -> list:
        """Given date and fighter pairs, finds the fight id

        Args:
            `fighter_1` (`str`): fighter 1 name
            `fighter_2` (`str`): fighter 2 name
            `date` (`str`): event date
            `last_only` (`bool`, optional): use only last names in search. Defaults to False.

        Returns:
            `list`: list of fight ids
        """
        
        # converting names into standard formats and account for potential spaces in names
        if last_only:
            f1_last_1 = unidecode(fighter_1).lower().replace(r"'", r"''")
            f2_last_1 = unidecode(fighter_2).lower().replace(r"'", r"''")
            f1_last_names = [f1_last_1]
            f2_last_names = [f2_last_1]
        
        else:
            f1_first_1 = unidecode(fighter_1[0]).lower().replace(r"'", r"''")
            f1_first_2 = unidecode(' '.join(fighter_1[0:1])).lower().replace(r"'", r"''")
            f1_last_1 = unidecode(fighter_1[-1]).lower().replace(r"'", r"''")
            f1_last_2 = unidecode(' '.join(fighter_1[1:])).lower().replace(r"'", r"''")

            f2_first_1 = unidecode(fighter_2[0]).lower().replace(r"'", r"''")
            f2_first_2 = unidecode(' '.join(fighter_2[0:1])).lower().replace(r"'", r"''")
            f2_last_1 = unidecode(fighter_2[-1]).lower().replace(r"'", r"''")
            f2_last_2 = unidecode(' '.join(fighter_2[1:])).lower().replace(r"'", r"''")
            
            f1_last_names = [f1_last_1, f1_last_2]
            f2_last_names = [f2_last_1, f2_last_2]
            f1_first_names = [f1_first_1, f1_first_2]
            f2_first_names = [f2_first_1, f2_first_2]
            
        # create a range of dates close to the actual date to avoid mismatch on different webpages
        date_format = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        dates = [date_format.strftime('%Y-%m-%d'),
                 (date_format + datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
                 (date_format - datetime.timedelta(days=1)).strftime('%Y-%m-%d')]
        
        fight_id = []
        
        sql_selection = (
            'SELECT fights.fight_id FROM fights ' +
            'INNER JOIN events ON fights.event_id=events.event_id ' +
            'INNER JOIN fighters fighter_1 ON fights.fighter_1_id=fighter_1.figher_id ' +
            'INNER JOIN fighters fighter_2 ON fights.fighter_2_id=fighter_2.fighter_id ')
        
        # first-pass: search by combination of last names and date
        for x in product(f1_last_names, f2_last_names, dates):
            fight_id = self.engine.execute(sql_selection +
                'WHERE ((lower(fighter_1.last_name)=\''+x[0]+'\' ' +
                'AND lower(fighter_2.last_name)=\''+x[1]+'\') ' +
                'OR (lower(fighter_1.last_name)=\''+x[1]+'\' ' +
                'AND lower(fighter_2.last_name)=\''+x[0]+'\')) ' +
                'AND events.event_date=\''+x[2]+'\'')
            
            fight_id = [x.fight_id for x in fight_id]
            if fight_id:
                break
        
        # second-pass: search by combinations of fighter 1 names and date
        if not fight_id and not last_only:
            for x in product(f1_first_names, f1_last_names, dates):
                fight_id = self.engine.execute(sql_selection +
                    'WHERE ((lower(fighter_1.last_name)=\''+x[1]+'\' ' +
                    'AND lower(fighter_1.first_name)=\''+x[0]+'\') ' +
                    'OR (lower(fighter_1.last_name)=\''+x[0]+'\' ' +
                    'AND lower(fighter_1.first_name)=\''+x[1]+'\')) ' +
                    'OR ((lower(fighter_2.last_name)=\''+x[1]+'\' ' +
                    'AND lower(fighter_2.first_name)=\''+x[0]+'\') ' +
                    'OR (lower(fighter_2.last_name)=\''+x[0]+'\' ' +
                    'AND lower(fighter_2.first_name)=\''+x[1]+'\')) ' +
                    'AND events.event_date=\''+x[2]+'\'')
                
                fight_id = [x.fight_id for x in fight_id]
                if fight_id:
                    break
                
        # third-pass: search by combinations of fighter 2 names and date
        if not fight_id and not last_only:
            for x in product(f2_first_names, f2_last_names, dates):
                fight_id = self.engine.execute(sql_selection +
                    'WHERE ((lower(fighter_1.last_name)=\''+x[1]+'\' ' +
                    'AND lower(fighter_1.first_name)=\''+x[0]+'\') ' +
                    'OR (lower(fighter_1.last_name)=\''+x[0]+'\' ' +
                    'AND lower(fighter_1.first_name)=\''+x[1]+'\')) ' +
                    'OR ((lower(fighter_2.last_name)=\''+x[1]+'\' ' +
                    'AND lower(fighter_2.first_name)=\''+x[0]+'\') ' +
                    'OR (lower(fighter_2.last_name)=\''+x[0]+'\' ' +
                    'AND lower(fighter_2.first_name)=\''+x[1]+'\')) ' +
                    'AND events.event_date=\''+x[2]+'\'')
                
                fight_id = [x.fight_id for x in fight_id]
                if fight_id:
                    break
        
        # TODO: check if name-flipping script addition is required
            
        return fight_id
    
    def query_last_names(self, fight_id) -> any:
        """Given fight id, return last names of both fighters

        Args:
            `fight_id` (`str`): unique fight id

        Returns:
            `any`: both fighter last names
        """
        
        last_names = self.engine.execute(
            'SELECT fighter1.last_name AS f1_last, fighter2.last_name AS f2_last FROM fights ' + 
            'INNER JOIN fighters fighter1 ON fights.fighter_1_id=fighter1.fighter_id ' +
            'INNER JOIN fighters fighter2 ON fights.fighter_2_id=fighter2.fighter_id ' +
            'WHERE fights.fight_id =\''+fight_id+'\' ')
        
        return last_names.fetchone()
    
    def query_latest_decision_date(self) -> str:
        """Return date of the latest event with a decision

        Returns:
            `str`: date of event
        """
        
        latest_date = self.engine.execute(
            'SELECT e.event_date FROM events AS e ' +
            'INNER JOIN fights ON e.event_id=fights.event_id ' +
            'WHERE fights.judge1_fighter1 > 0 ' +
            'ORDER BY e.event_date DESC ' +
            'LIMIT 1')
        
        return latest_date.fetchone()[0]
    