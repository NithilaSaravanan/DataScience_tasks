#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:56:25 2020

@author: nithila
"""

from bs4 import BeautifulSoup as bs
import pandas as pd
import sys
import requests as r
import hashlib
import os.path as osp
import time

def getCache(url, cache_dir):
    hash_name = hashlib.sha1(url.encode('utf-8')).hexdigest()
    filename = osp.join(cache_dir, hash_name)
    contents = None
    if osp.exists(filename):
        return filename
    else:
        time.sleep(1) #Make sure to not hit the server too often too soon
        data = r.get(url)
        contents = data.text
        try:
            with open(filename, 'w') as f:
                f.write(contents)
        finally:
            f.close()
        return filename


def getCoursesAndPrint(filename):
    file = open(filename, 'r')
    soup = bs(file, 'html.parser')
    course_data = []
    course_id = []
    course_name = []
    course_credits = []
    total_len = len(soup.find_all('h4','field-content'))
    
    a = soup.find_all('h4','field-content')
    
    for i in range(total_len):
        course_data.append(a[i].string)
    
    for i in range(len(course_data)):
        number = course_data[i].split()[-2]
        number = number.replace('(','')
        if number.replace('.','',1).isdigit() :
            if len(course_data[i].split()[0]) ==4:
                if ")" in course_data[i].split()[-1]:
                    course_credits.append(number)
                    course_id.append(course_data[i].split()[0] + ' ' + course_data[i].split()[1])
                    name = course_data[i].split()[2:-2]
                    course_name.append(' '.join(word for word in name))
        
    df = pd.DataFrame(list(zip(course_id, course_name, course_credits)), columns = ['CourseID','Course Name','# of credits'])
    df.to_csv(sys.stdout, index = False)
    
    
def main():
    cache_dir = 'data2/mcgill'
    pg_no = 76
    url = "https://www.mcgill.ca/study/2020-2021/courses/search?page=" + str(pg_no)
    file_name = getCache(url, cache_dir)
    getCoursesAndPrint(file_name)
    
    
    
if __name__=='__main__':
    main()



































"""

file = open('mycourses_test2', 'r')
soup = bs(file, 'html.parser')
course_data = []
course_id = []
course_name = []
course_credits = []
total_len = len(soup.find_all('h4','field-content'))

a = soup.find_all('h4','field-content')

for i in range(total_len):
    course_data.append(a[i].string)

for i in range(len(course_data)):
    number = course_data[i].split()[-2]
    number = number.replace('(','')
    if number.replace('.','',1).isdigit() :
        if len(course_data[i].split()[0]) ==4:
            if ")" in course_data[i].split()[-1]:
                course_credits.append(number)
                course_id.append(course_data[i].split()[0] + ' ' + course_data[i].split()[1])
                name = course_data[i].split()[2:-2]
                course_name.append(' '.join(word for word in name))
    
df = pd.DataFrame(list(zip(course_id, course_name, course_credits)), columns = ['CourseID','Course Name','# of credits'])
df.to_csv(sys.stdout, index = False)


"""
