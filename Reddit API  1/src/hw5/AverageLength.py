"""
NAME: Nithilasaravanan Kuppan
ID: 260905444

COMP 598 HOMEWORK 5
Source code for compute_title_lengths.py in scripts

"""

import json

def AvgPostLength(post_list):
    totalChars = 0
    for x in post_list:
        totalChars = totalChars + len(x['data']['title'])
    return (round(totalChars / len(post_list),2))
