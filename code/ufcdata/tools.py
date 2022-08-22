#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   tools.py
@Time    :   2022/08/18 11:50:57
@Author  :   Neel Gokhale
@Contact :   neelg14@gmail.com
@License :   (C)Copyright 2020-2021, Neel Gokhale
'''

import pandas as pd

def strip_remove_blanks(string_list) -> list:
    """Returns a list of strings without any blanks

    Args:
        `string_list` (`list`): list of strings

    Returns:
        `list`: list without blanks
    """
    
    string_list = [x.strip() for x in string_list]
    string_list = [x for x in string_list if x]
    
    return string_list

def time_to_sec(time) -> int:
    """Converts string time in format "mm:ss" into int seconds

    Args:
        `time` (`str`): string time

    Returns:
        `int`: total number of seconds
    """
    
    try:
        min_sec = time.split(':')
        sec = int(min_sec[1])
        min_in_sec = int(min_sec[0])
    except (IndexError, TypeError) as e:
        return e
    
    return sec + min_in_sec

def judge_round_scores(round_scores, f1_list, f2_list, j, correct_position):
    """Correctly indexes the rounds scores by index j

    Args:
        `round_scores` (`any`): round scores
        `f1_list` (`list`): fighter 1 score list
        `f2_list` (`list`): fighter 2 score list
        `j` (`int`): index
        `correct_position` (`bool`): check if in correct position
    """
    
    if correct_position:
        f1_list.append(round_scores[j+1])
        f2_list.append(round_scores[j+2])
    else:
        f2_list.append(round_scores[j+1])
        f1_list.append(round_scores[j+2])

def query_to_df(query) -> pd.DataFrame:
    """Transforms query object (dict-like) into a pandas DataFrame

    Args:
        `query` (`any`): query object. Recommended usage is by returning it as an object through a specified function in query.py

    Returns:
        `pd.DataFrame`: _description_
    """
    
    df = pd.DataFrame(query.fetchall())
    df.columns = query.keys()
    
    return df
