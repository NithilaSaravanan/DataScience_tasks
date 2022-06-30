#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 04:08:16 2020

@author: nithila
"""

import pandas as pd
import numpy as np
import datetime

#Load Data
df = pd.read_csv('testdata.csv', names = ['id','creation','closed','zip'], parse_dates = True) #Remember to chqnge this!
df['creation']=pd.to_datetime(df['creation'])
df['closed']=pd.to_datetime(df['closed'])


#Filter out 
df['year'] = df['creation'].dt.year
df['month'] =df['creation'].dt.month
df = df [df['year'] ==2018] # Remember to change this!
df = df[df['closed'].isnull() == False]
df = df[df.zip.apply(lambda x: str(x).isnumeric())]

#Create necessary columns
df['hours'] = round(((df['closed'] - df['creation']).dt.total_seconds())/3600)

df1 = df.groupby(['zip','month'], as_index = False)['hours'].mean()
df2 = df.groupby('month', as_index = False) ['hours'].mean()

final_df = pd.merge(df1,df2,how='left', on='month')
final_df.columns = ['zip','month','zip_hours','over_hours']

final_df.to_csv(r'output.csv', index = False)