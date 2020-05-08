#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """ Top ten post """
    sub = requests.get('https://www.reddit.com/r/{}/.json'.
                       format(subreddit),
                       headers={'user-agent': 'X-Modhash'}).json()
    try:
        for i in range(10):
            print(sub['data']['children'][i]['data']['title'])
    except:
        print(None)
