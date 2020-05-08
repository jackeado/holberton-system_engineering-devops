#!/usr/bin/python3
"""
"""
import requests


def top_ten(subreddit):
    """ """
    sub = requests.get('https://www.reddit.com/r/{}/.json'.
                       format(subreddit),
                       headers={'user-agent': 'X-Modhash'}).json()
    try:
        for i in range(10):
            print(sub['data']['children'][i]['data']['title'])
    except:
        print(None)
