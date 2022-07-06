"""
NAME: Nithilasaravanan Kuppan
ID: 260905444

COMP 598 HOMEWORK 6
Source code (function) for fetching 500 hottest posts from a subreddit and writing them to a location

"""

import requests
import json
import time
import os.path as osp

this_dir = osp.dirname(__file__)

def SubDataGetWrite(subreddits, headers,output):
    output_path = osp.join(this_dir, '..', '..', 'data', output)
    content = []
    
    #To get posts AFTER the last post in the list (obeying the max limit of the API)
    after_post = ""

    #To figure out how many extra posts crept in because of the stickied posts
    post_count = 0

    
    #Getting reddit subreddit data using API call
    for i in range(5):
        
        time.sleep(2)

        url = f'http://api.reddit.com{subreddits}/hot?limit=100&after='+ after_post
        data = requests.get(url, headers=headers)
        content.append(data.json()['data']['children'])

        #Getting the *name* of the last post for the after parameter
        after_post = content[-1][-1]['data']['name']

        #Getting the total number of posts coming through
        post_count = post_count + len(content[i])

    tooManyPosts = post_count - 500

    #Reducing the number of posts to 500
    if(tooManyPosts > 0):
        content[-1] = content[-1][:(len(content[-1]) - tooManyPosts)]

    #Write this data to the data/output
    with open(output_path, 'w') as HotPosts:
        for i in range(len(content)):
            for x in content[i]:
                json.dump(x, HotPosts)
                HotPosts.write('\n')


    print(f'Wrote 500 lines to {output} successfully!\n')

    



