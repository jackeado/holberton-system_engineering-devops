#!/usr/bin/python3
"""
"""
import requests


def number_of_subscribers(subreddit):
    """ """
    sub = requests.get('https://www.reddit.com/r/{}/about.json'.
                       format(subreddit), headers={'user-agent': 'X-Modhash'})
    data_sub = sub.json()
    if dataSu is None or dataSu is not str:
        return 0
    dataSu = data_sub['data']['subscribers']
    return(dataSu)
