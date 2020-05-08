#!/usr/bin/python3
"""
"""
import requests

def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    header = {'user-agent': 'X-Modhash'}
    r = requests.get('https://www.reddit.com/r/{}/about.json'.
                     format(subreddit), headers=header)
    data_sub = r.json()
    try:
        dataSu = data_sub['data']['subscribers']
    except:
        return 0
    return(dataSu)
