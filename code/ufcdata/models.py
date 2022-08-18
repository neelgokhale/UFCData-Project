from sqlalchemy import Column, DateTime, Float, Integer, String, create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

import ufcdata.settings

DeclarativeBase = declarative_base()

def db_connect():
    """Performs database connection using settings in settings.py module

    Returns:
        sqlalchemy.create_engine: returns create_engine instance with database URL
    """
    
    return create_engine(URL(**ufcdata.settings.DATABASE))

def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)
    

class EventTable(DeclarativeBase):
    
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True)
    event_id = Column('event_id', String, nullable=True, unique=True)
    event_name = Column('event_name', String, nullable=True)
    event_date = Column('event_date', String, nullable=True)
    event_city = Column('event_city', String, nullable=True)
    event_country = Column('event_country', String, nullable=True)
    num_fights = Column('num_fights', Integer, nullable=True)
    create_date = Column('create_date', String, nullable=True)
    

class FightTable(DeclarativeBase):
    
    __tablename__ = 'fights'
    
    id = Column(Integer, primary_key=True)
    fight_id = Column('fight_id', String, nullable=True, unique=True)
    event_id = Column('event_id', String, nullable=True)
    weightclass = Column('weightclass', String, nullable=True)
    rds_sched = Column('rds_sched', String, nullable=True)
    rd_ended = Column('rd_ended', String, nullable=True)
    method = Column('method', String, nullable=True)
    time_last_rd = Column('time_last_rd', String, nullable=True)
    referee = Column('referee', String, nullable=True)
    bonus = Column('bonus', String, nullable=True)
    fighter_1_id = Column('fighter_1_id', String, nullable=True)
    fighter_2_id = Column('fighter_2_id', String, nullable=True)
    winner_id = Column('winner_id', String, nullable=True)
    judge1 = Column('judge1', String, nullable=True)
    judge2 = Column('judge2', String, nullable=True)
    judge3 = Column('judge3', String, nullable=True)
    judge1_fighter1 = Column('judge1_fighter1', Integer, nullable=True)
    judge1_fighter2 = Column('judge1_fighter2', Integer, nullable=True)
    judge2_fighter1 = Column('judge2_fighter1', Integer, nullable=True)
    judge2_fighter2 = Column('judge2_fighter2', Integer, nullable=True)
    judge3_fighter1 = Column('judge3_fighter1', Integer, nullable=True)
    judge3_fighter2 = Column('judge3_fighter2', Integer, nullable=True)
    deductions = Column('deductions', String, nullable=True)
    create_date = Column('create_date', String, nullable=True)
    

class RoundTable(DeclarativeBase):
    
    __tablename__ = 'rounds'
    
    id = Column(Integer, primary_key=True)
    rd_id = Column('rd_id', String, nullable=True, unique=True)
    fight_id = Column('fight_id', String, nullable=True)
    rd_num = Column('rd_num', Integer, nullable=True)
    rd_length = Column('rd_length', Integer, nullable=True)
    judge1_fighter1 = Column('judge1_fighter1', Integer, nullable=True)
    judge1_fighter2 = Column('judge1_fighter2', Integer, nullable=True)
    judge2_fighter1 = Column('judge2_fighter1', Integer, nullable=True)
    judge2_fighter2 = Column('judge2_fighter2', Integer, nullable=True)
    judge3_fighter1 = Column('judge3_fighter1', Integer, nullable=True)
    judge3_fighter2 = Column('judge3_fighter2', Integer, nullable=True)
    create_date = Column('create_date', String, nullable=True)
    

class RoundStatsTable(DeclarativeBase):
    
    __tablename__ = 'round_stats'
    
    # IDENTIFIERS
    id = Column(Integer, primary_key=True)
    rd_result_id = Column('rd_result_id', String, nullable=True, unique=True)
    fighter_id = Column('fighter_id', String, nullable=True)
    opponent_id = Column('opponent_id', String, nullable=True)
    rd_id = Column('rd_id', String, nullable=True)
    create_date = Column('create_date', String, nullable=True)
    
    # OFFENSIVE
    kd = Column('kd', Integer, nullable=True)
    sig_head_made = Column('sig_head_made', Integer, nullable=True)
    sig_head_att = Column('sig_head_att', Integer, nullable=True)
    sig_body_made = Column('sig_body_made', Integer, nullable=True)
    sig_body_att = Column('sig_body_att', Integer, nullable=True)
    sig_leg_made = Column('sig_leg_made', Integer, nullable=True)
    sig_leg_att = Column('sig_leg_att', Integer, nullable=True)
    sig_clinch_made = Column('sig_clinch_made', Integer, nullable=True)
    sig_clinch_att = Column('sig_clinch_att', Integer, nullable=True)
    sig_dist_made = Column('sig_dist_made', Integer, nullable=True)
    sig_dist_att = Column('sig_dist_att', Integer, nullable=True)
    sig_ground_made = Column('sig_ground_made', Integer, nullable=True)
    sig_ground_att = Column('sig_ground_att', Integer, nullable=True)
    tot_str_made = Column('tot_str_made', Integer, nullable=True)
    tot_str_att = Column('tot_str_att', Integer, nullable=True)
    takedown_made = Column('takedown_made', Integer, nullable=True)
    takedown_att = Column('takedown_att', Integer, nullable=True)
    sub_att = Column('sub_att', Integer, nullable=True)
    reversals = Column('reversals', Integer, nullable=True)
    ctrl = Column('ctrl', Integer, nullable=True)
    create_date = Column('create_date', String, nullable=True)
    
    # DEFENSIVE
    
    opp_kd = Column('opp_kd', Integer, nullable=True)
    opp_sig_head_made = Column('opp_sig_head_made', Integer, nullable=True)
    opp_sig_head_att = Column('opp_sig_head_att', Integer, nullable=True)
    opp_sig_body_made = Column('opp_sig_body_made', Integer, nullable=True)
    opp_sig_body_att = Column('opp_sig_body_att', Integer, nullable=True)
    opp_sig_leg_made = Column('opp_sig_leg_made', Integer, nullable=True)
    opp_sig_leg_att = Column('opp_sig_leg_att', Integer, nullable=True)
    opp_sig_clinch_made = Column('opp_sig_clinch_made', Integer, nullable=True)
    opp_sig_clinch_att = Column('opp_sig_clinch_att', Integer, nullable=True)
    opp_sig_dist_made = Column('opp_sig_dist_made', Integer, nullable=True)
    opp_sig_dist_att = Column('opp_sig_dist_att', Integer, nullable=True)
    opp_sig_ground_made = Column('opp_sig_ground_made', Integer, nullable=True)
    opp_sig_ground_att = Column('opp_sig_ground_att', Integer, nullable=True)
    opp_tot_str_made = Column('opp_tot_str_made', Integer, nullable=True)
    opp_tot_str_att = Column('opp_tot_str_att', Integer, nullable=True)
    opp_takedown_made = Column('opp_takedown_made', Integer, nullable=True)
    opp_takedown_att = Column('opp_takedown_att', Integer, nullable=True)
    opp_sub_att = Column('opp_sub_att', Integer, nullable=True)
    opp_reversals = Column('opp_reversals', Integer, nullable=True)
    opp_ctrl = Column('opp_ctrl', Integer, nullable=True)
    create_date = Column('create_date', String, nullable=True)

class FighterTable(DeclarativeBase):
    
    __tablename__ = 'fighters'
    
    id = Column(Integer, primary_key=True)
    fighter_id = Column('fighter_id', String, nullable=True, unique=True)
    first_name = Column('first_name', String, nullable=True)
    last_name = Column('last_name', String, nullable=True)
    nickname = Column('nickname', String, nullable=True)
    dob = Column('dob', String, nullable=True)
    gender = Column('gender', String, nullable=True)
    reach = Column('reach', Integer, nullable=True)
    height = Column('height', Integer, nullable=True)
    weight = Column('weight', Integer, nullable=True)
    stance = Column('stance', String, nullable=True)
    wins = Column('wins', Integer, nullable=True)
    losses = Column('losses', Integer, nullable=True)
    draws = Column('draws', Integer, nullable=True)
    belt = Column('belt', String, nullable=True)
    last_fight_data = Column('last_fight_data', String, nullable=True)
    latest_weightclass = Column('latest_weightclass', String, nullable=True)
    create_date = Column('create_date', String, nullable=True)
