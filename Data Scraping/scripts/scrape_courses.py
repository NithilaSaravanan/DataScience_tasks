"""
NAME: Nithilasaravanan Kuppan
ID: 260905444
EMAIL: nithilasaravana.kuppan@mail.mcgill.ca

COMP 598 - HOMEWORK 7 - Task 2
"""

from bs4 import BeautifulSoup as bs
import pandas as pd
import sys
import requests as r
import hashlib
import os.path as osp
import time
import argparse
import os

#Check if directory exists, else creating it in the script
def checkDir(cache_dir):
    try:
        os.makedirs(cache_dir)
        print(f'\n Created {cache_dir}')
    except FileExistsError:
        pass

#Function to ensure file is cached and if present, script leverages it
def getCache(url, cache_dir):
    hash_name = hashlib.sha1(url.encode('utf-8')).hexdigest()
    filename = osp.join(cache_dir, hash_name)
    contents = None

    if osp.exists(filename):
        return filename
    else:
        time.sleep(1) #Prevents overburden on server
        data = r.get(url)
        contents = data.text
        with open(filename, 'w') as f:
            f.write(contents)
        return filename


#Function to get the course info from the URL and print the proper ones it in a CSV format
def getCoursesAndPrint(filename):
    file_n = open(filename, 'r')
    soup = bs(file_n, 'html.parser')
    course_data = []
    course_id = []
    course_name = []
    course_credits = []
    total_len = len(soup.find_all('h4','field-content'))

    a = soup.find_all('h4','field-content')

    for i in range(total_len): #Finding the total number of courses on the page
        course_data.append(a[i].string)

    for i in range(len(course_data)):
        number = course_data[i].split()[-2]
        number = number.replace('(','')
        if number.replace('.','',1).isdigit(): #checking structure rule 1
            if len(course_data[i].split()[0]) ==4: #checking structure rule 2
                if ")" in course_data[i].split()[-1]: #checking structure rule 3
                    course_credits.append(number)
                    course_id.append(course_data[i].split()[0] + ' ' + course_data[i].split()[1])
                    name = course_data[i].split()[2:-2]
                    course_name.append(' '.join(word for word in name))

    df = pd.DataFrame(list(zip(course_id, course_name, course_credits)), columns = ['CourseID','Course Name','# of credits'])
    df.to_csv(sys.stdout, index = False)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', help = 'Path to the cache directory to store all the pages', default = 'nope')
    parser.add_argument('pg', help = 'Page number (McGill\'s website) to download courses from')

    try:
        args = parser.parse_args()
    except:
        print('\n Missing parameter. Please try again \n')
        parser.print_help()
        sys.exit()

    cache_dir = args.c
    pg_no = args.pg

    if (cache_dir == 'nope'):
        print('\n Missing parameters. Please try again \n')
        parser.print_help()
        sys.exit()

    checkDir(cache_dir)
    url = 'https://www.mcgill.ca/study/2020-2021/courses/search?page='+str(pg_no)

    file_name = getCache(url, cache_dir)

    getCoursesAndPrint(file_name)


if __name__ == '__main__':
    main()

