"""
NAME: Nithilasaravanan Kuppan
ID: 260905444

COMP 598 HOMEWORK 6
To get the hottest 5 posts over three consecutive days from the given subreddit (r/politics) and store it in data/ filename
"""

import requests
import requests.auth
import json
import time
import argparse
import os.path as osp
import sys
from hw6.GetReddit import SubDataGetWrite


this_dir = osp.dirname(__file__)

def main():
    """
    Getting params from CLI
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', help = 'Relative path / name of the outfile file', default = 'nope')
    parser.add_argument('sr', help = 'Name of the subreddit in the form \" /r/SUBREDDIT\"')
    try:
       args = parser.parse_args()
    except:
        print('\n No subreddit provided. Please try again \n')
        parser.print_help()
        sys.exit()

    subreddit = args.sr
    output_path = args.o

    if output_path == 'nope':
        print('\n No file path provided. Please try again \n')
        parser.print_help()
        sys.exit()

    """
    Reddit Authorization and Data collection
    """

    #Getting the OAuth authorization leveraging Reddit app. SOURCE: Reddit API Documentation
    
    client_auth = requests.auth.HTTPBasicAuth('_kEte7lCEAg6SQ', '0-FgqXE7WBDWB0NcmsMIiErjrxQ')
    post_data = {"grant_type": "password", "username": "APIDataColUser", "password": "weakpassword"}
    headers = {"User-Agent": "MacOS:requests (by /u/APIDataColUser)"}

    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    letmein = response.json()

    print("Successful Authorization! \n")

    headers = {"Authorization":letmein['access_token'] , "User-Agent": "Ubuntu:requests (by /u/APIDataColUser)"}

    print(f'Getting 500 of the hottest posts from {subreddit} \n')
    SubDataGetWrite(subreddit, headers, output_path)

if __name__ == '__main__':
    main()


