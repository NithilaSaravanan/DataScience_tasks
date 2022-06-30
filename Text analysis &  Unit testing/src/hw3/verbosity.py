"""

Function to calculate the verbosity metric. Takes a dataframe as an input and returns the values in a dict variable.

AUTHOR: Nithilasaravanan Kuppan
MCGILL ID: 260905444
EMAIL: nithilasaravana.kuppan@mail.mcgill.ca

COMP 598
Homework Assignment 3

"""

import pandas as pd
import numpy as np
import os.path
import argparse
import re
import json
from collections import Counter

def calc_verbosity(df):
   
    verbosity_data = df[df['clean_speaker'] != 'other']
    tot_act = verbosity_data['speech_act'].sum()
    twilight_v = round((verbosity_data[verbosity_data['clean_speaker']=='twilight']['speech_act'].sum())/tot_act, 2)
    applejack_v = round((verbosity_data[verbosity_data['clean_speaker']=='applejack']['speech_act'].sum())/tot_act, 2)
    rarity_v = round((verbosity_data[verbosity_data['clean_speaker']=='rarity']['speech_act'].sum())/tot_act, 2)
    pinkie_v = round((verbosity_data[verbosity_data['clean_speaker']=='pinkie']['speech_act'].sum())/tot_act, 2)
    rainbow_v = round((verbosity_data[verbosity_data['clean_speaker']=='rainbow']['speech_act'].sum())/tot_act, 2)
    fluttershy_v = round((verbosity_data[verbosity_data['clean_speaker']=='fluttershy']['speech_act'].sum())/tot_act, 2)

    js_verbosity ={"twilight":twilight_v, "applejack":applejack_v, "rarity":rarity_v, "pinkie":pinkie_v, "rainbow":rainbow_v,"fluttershy":fluttershy_v}
    return(js_verbosity)

