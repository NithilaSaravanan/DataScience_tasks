"""
NAME: Nithilasaravanan Kuppan
ID: 260905444

COMP 598 HOMEWORK 5
To get the 100 latests posts each from the given subreddits and store the ['children'] field for every post in data/ folders. The output files are data/sample1.json and data/sample2.json

"""
import requests 
import requests.auth
import json
import time
from hw5.GetReddit import SubDataGetWrite

def main():

    #Getting all the OAuth authorization working here using the Reddit app. SOURCE: Reddit API Documentation
    #PLEASE MAKE SURE TO USE YOUR OWN CREDENTIALS WHILE RUNNING THIS PART. THIS CODE HAS MY ACCOUNT CREDENTIALS IN IT

    client_auth = requests.auth.HTTPBasicAuth('_kEte7lCEAg6SQ', '0-FgqXE7WBDWB0NcmsMIiErjrxQ')
    post_data = {"grant_type": "password", "username": "APIDataColUser", "password": "weakpassword"}
    headers = {"User-Agent": "MacOS:requests (by /u/APIDataColUser)"}

    #Getting tokens
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    letmein = response.json()
    
    print("Successful Authorization! \n")


    headers = {"Authorization":letmein['access_token'] , "User-Agent": "MacOS:requests (by /u/APIDataColUser)"}

    #Listing all subreddits to pull from (as per the assignment)
    SubPopSubreddits = ['funny','AskReddit','gaming','aww','pics','Music','science','worldnews','videos','todayilearned']
    PostsPopSubreddits = ['AskReddit','memes','politics','nfl','nba','wallstreetbets','teenagers','PublicFreakout','leagueoflegends','unpopularopinion']

    #Calling function to get the data and output it to the data/ folder
    print("Getting the newest 1000 posts from the most popular subreddits (by subscribers)\n")
    SubDataGetWrite(subreddits=SubPopSubreddits, headers=headers, output='sample1.json')
    print("Getting the newest 1000 posts from the most popular subreddits (by daily posts)\n")
    SubDataGetWrite(subreddits=PostsPopSubreddits, headers=headers, output='sample2.json')

if __name__=='__main__':
    main()





