"""
NAME: Nithilasaravanan Kuppan
ID: 260905444

COMP 598 HOMEWORK 5
To find the average length of the titles in Reddit posts
Input: JSON file containing data from Reddit API (['children'] field)
"""
import json
import argparse
import sys
import os.path as osp
from hw5.AverageLength import AvgPostLength

this_dir = osp.dirname(__file__)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help = 'Please enter a filename, technically either sample1.json or sample2.json (which is the output of the Reddit API data collection script)')
    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(0)

    filename = args.input_file
    redditData = osp.join(this_dir,'..','data',filename)

    #Reading the file and storing it as a list
    data =[]

    for line in open(redditData, 'r'):
        try:
            data.append(json.loads(line))
        except ValueError:
            pass

    #Calling AverageLength.py to calcualte the metric
    print(AvgPostLength(data))


if __name__=='__main__':
    main()
