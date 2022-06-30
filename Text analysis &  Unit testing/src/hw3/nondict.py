"""

Function to calculate the non dictionary words metric. Takes a dataframe as an input and returns the values in a dict variable.

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

def calc_nondict(df):
    #For twilight
    list_twilight = []
    for el1 in df[df['clean_speaker']=='twilight']['non_dict_words']:
         list_twilight += el1

    twilight_counter1 = pd.DataFrame(Counter(list_twilight).most_common(5), columns =['0', '1'])
    twilight_counter = twilight_counter1['0']
    twilight_non_dict_words = [twilight_counter[0], twilight_counter[1], twilight_counter[2], twilight_counter[3], twilight_counter[4]]

     #For applejack
    list_applejack = []
    for el1 in df[df['clean_speaker']=='applejack']['non_dict_words']:
        list_applejack += el1

    applejack_counter1 = pd.DataFrame(Counter(list_applejack).most_common(5), columns =['0', '1'])
    applejack_counter = applejack_counter1['0']
    applejack_non_dict_words = [applejack_counter[0], applejack_counter[1], applejack_counter[2], applejack_counter[3], applejack_counter[4]]

    #For rarity
    list_rarity = []
    for el1 in df[df['clean_speaker']=='rarity']['non_dict_words']:
        list_rarity += el1

    rarity_counter1 = pd.DataFrame(Counter(list_rarity).most_common(5), columns =['0', '1'])
    rarity_counter = rarity_counter1['0']
    rarity_non_dict_words = [rarity_counter[0], rarity_counter[1], rarity_counter[2], rarity_counter[3], rarity_counter[4]]

    #For pinkie
    list_pinkie = []
    for el1 in df[df['clean_speaker']=='pinkie']['non_dict_words']:
        list_pinkie += el1

    pinkie_counter1 = pd.DataFrame(Counter(list_pinkie).most_common(5), columns =['0', '1'])
    pinkie_counter = pinkie_counter1['0']
    pinkie_non_dict_words = [pinkie_counter[0], pinkie_counter[1], pinkie_counter[2], pinkie_counter[3], pinkie_counter[4]]

    #For rainbow
    list_rainbow = []
    for el1 in df[df['clean_speaker']=='rainbow']['non_dict_words']:
        list_rainbow += el1

    rainbow_counter1 = pd.DataFrame(Counter(list_rainbow).most_common(5), columns =['0', '1'])
    rainbow_counter = rainbow_counter1['0']
    rainbow_non_dict_words = [rainbow_counter[0], rainbow_counter[1], rainbow_counter[2], rainbow_counter[3], rainbow_counter[4]]

    #For fluttershy
    list_fluttershy = []
    for el1 in df[df['clean_speaker']=='fluttershy']['non_dict_words']:
        list_fluttershy += el1

    fluttershy_counter1 = pd.DataFrame(Counter(list_fluttershy).most_common(5), columns =['0', '1'])
    fluttershy_counter = fluttershy_counter1['0']
    fluttershy_non_dict_words = [fluttershy_counter[0], fluttershy_counter[1], fluttershy_counter[2], fluttershy_counter[3], fluttershy_counter[4]]

    js_non_dict = {"twilight": twilight_non_dict_words, "applejack": applejack_non_dict_words, "rarity":rarity_non_dict_words,"pinkie":pinkie_non_dict_words,"rainbow":rainbow_non_dict_words,"fluttershy":fluttershy_non_dict_words}

    return(js_non_dict)
