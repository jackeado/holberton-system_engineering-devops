#!/usr/bin/python3
"""
Numbers of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    headers = {'user-agent': 'X-Modhash'}
    r = requests.get('https://www.reddit.com/r/{}/about.json'.
                     format(subreddit), headers=headers).json()
    try:
        dataSu = r['data']['subscribers']
        return (dataSu)
    except:
        return 0
