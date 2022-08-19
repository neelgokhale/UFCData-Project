#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   items.py
@Time    :   2022/08/15 22:02:49
@Author  :   Neel Gokhale
@Contact :   neelg14@gmail.com
@License :   (C)Copyright 2020-2021, Neel Gokhale
'''

from scrapy import Field, Item
# from scrapy.loader.processors import TakeFirst
from itemloaders.processors import TakeFirst

class Event(Item):
    event_id = Field(output_processor=TakeFirst())
    event_name = Field(output_processor=TakeFirst())
    event_date = Field(output_processor=TakeFirst())
    event_city = Field(output_processor=TakeFirst())
    event_country = Field(output_processor=TakeFirst())
    event_type = Field(output_processor=TakeFirst())
    num_fights = Field(output_processor=TakeFirst())
    create_date = Field(output_processor=TakeFirst())
    

class Fight(Item):
    fight_id = Field(output_processor=TakeFirst())
    event_id = Field(output_processor=TakeFirst())
    weight_class = Field(output_processor=TakeFirst())
    rds_sched = Field(output_processor=TakeFirst())
    method = Field(output_processor=TakeFirst())
    rd_ended = Field(output_processor=TakeFirst())
    time_last_rd = Field(output_processor=TakeFirst())
    referee = Field(output_processor=TakeFirst())
    bonus = Field(output_processor=TakeFirst())
    fighter_1_id = Field(output_processor=TakeFirst())
    fighter_2_id = Field(output_processor=TakeFirst())
    winner_id = Field(output_processor=TakeFirst())
    create_date = Field(output_processor=TakeFirst())
    

class Round(Item):
    rd_id = Field(output_processor=TakeFirst())
    fight_id = Field(output_processor=TakeFirst())
    rd_num = Field(output_processor=TakeFirst())
    rd_length = Field(output_processor=TakeFirst())
    create_date = Field(output_processor=TakeFirst())
    

class RoundStat(Item):
    # IDENTIFIERS
    rd_result_id = Field(output_processor=TakeFirst())
    fight_id = Field(output_processor=TakeFirst())
    fighter_id = Field(output_processor=TakeFirst())
    opponent_id = Field(output_processor=TakeFirst())
    rd_id = Field(output_processor=TakeFirst())
    create_date = Field(output_processor=TakeFirst())
    
    # OFFENSIVE
    kd = Field(output_processor=TakeFirst())
    sig_head_made = Field(output_processor=TakeFirst())
    sig_head_att = Field(output_processor=TakeFirst())
    sig_body_made = Field(output_processor=TakeFirst())
    sig_body_att = Field(output_processor=TakeFirst())
    sig_leg_made = Field(output_processor=TakeFirst())
    sig_leg_att = Field(output_processor=TakeFirst())
    sig_clinch_made = Field(output_processor=TakeFirst())
    sig_clinch_att = Field(output_processor=TakeFirst())
    sig_dist_made = Field(output_processor=TakeFirst())
    sig_dist_att = Field(output_processor=TakeFirst())
    sig_ground_made = Field(output_processor=TakeFirst())
    sig_ground_att = Field(output_processor=TakeFirst())
    tot_str_made = Field(output_processor=TakeFirst())
    tot_str_att = Field(output_processor=TakeFirst())
    takedown_made = Field(output_processor=TakeFirst())
    takedown_att = Field(output_processor=TakeFirst())
    sub_att = Field(output_processor=TakeFirst())
    reversals = Field(output_processor=TakeFirst())
    ctrl = Field(output_processor=TakeFirst())
    
    # DEFENSIVE
    opp_kd = Field(output_processor=TakeFirst())
    opp_sig_head_made = Field(output_processor=TakeFirst())
    opp_sig_head_att = Field(output_processor=TakeFirst())
    opp_sig_body_made = Field(output_processor=TakeFirst())
    opp_sig_body_att = Field(output_processor=TakeFirst())
    opp_sig_leg_made = Field(output_processor=TakeFirst())
    opp_sig_leg_att = Field(output_processor=TakeFirst())
    opp_sig_clinch_made = Field(output_processor=TakeFirst())
    opp_sig_clinch_att = Field(output_processor=TakeFirst())
    opp_sig_dist_made = Field(output_processor=TakeFirst())
    opp_sig_dist_att = Field(output_processor=TakeFirst())
    opp_sig_ground_made = Field(output_processor=TakeFirst())
    opp_sig_ground_att = Field(output_processor=TakeFirst())
    opp_tot_str_made = Field(output_processor=TakeFirst())
    opp_tot_str_att = Field(output_processor=TakeFirst())
    opp_takedown_made = Field(output_processor=TakeFirst())
    opp_takedown_att = Field(output_processor=TakeFirst())
    opp_sub_att = Field(output_processor=TakeFirst())
    opp_reversals = Field(output_processor=TakeFirst())
    opp_ctrl = Field(output_processor=TakeFirst())
    

class Fighter():
    fighter_id = Field(output_processor=TakeFirst())
    first_name = Field(output_processor=TakeFirst())
    last_name = Field(output_processor=TakeFirst())
    nickname = Field(output_processor=TakeFirst())
    dob = Field(output_processor=TakeFirst())
    gender = Field(output_processor=TakeFirst())
    reach = Field(output_processor=TakeFirst())
    height = Field(output_processor=TakeFirst())
    weight = Field(output_processor=TakeFirst())
    stance = Field(output_processor=TakeFirst())
    status = Field(output_processor=TakeFirst())
    wins = Field(output_processor=TakeFirst())
    losses = Field(output_processor=TakeFirst())
    draws = Field(output_processor=TakeFirst())
    belt = Field(output_processor=TakeFirst())
    last_fight_date = Field(output_processor=TakeFirst())
    latest_weight_class = Field(output_processor=TakeFirst())
    create_date = Field(output_processor=TakeFirst())
