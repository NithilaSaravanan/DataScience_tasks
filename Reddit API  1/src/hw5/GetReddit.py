"""
NAME: Nithilasaravanan Kuppan
ID: 260905444

COMP 598 HOMEWORK 5
Source code associatd with collect.py script

"""



import requests
import json
import time
import os.path as osp

this_dir = osp.dirname(__file__)

def SubDataGetWrite(subreddits, headers,output):
    content = []
    
    #Getting reddit subreddit data using API call
    for i in range(len(subreddits)):
        time.sleep(2)
        data = requests.get(f'http://api.reddit.com/r/{subreddits[i]}/new?limit=100', headers=headers)
        content.append(data.json()['data']['children'])

    output_path = osp.join(this_dir,'..','..','data',output)

    #Write this data to the data/output
    with open(output_path, 'w') as PopPosts:
        for i in range(len(content)):
            for x in content[i]:
                json.dump(x, PopPosts)
                PopPosts.write('\n')


    print(f'Wrote 1000 lines to {output_path} successfully!\n')





