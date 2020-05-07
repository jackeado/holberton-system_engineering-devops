#!/usr/bin/python3
"""
"""
import requests


def number_of_subscribers(subreddit):
    """ """
    sub = requests.get('https://www.reddit.com/r/{}/about.json'.
                       format(subreddit), headers={'user-agent': 'X-Modhash'})
    data_sub = sub.json()
    dataSu = data_sub['data']['subscribers']
    if dataSu is None:
        return 0
    return(dataSu)
