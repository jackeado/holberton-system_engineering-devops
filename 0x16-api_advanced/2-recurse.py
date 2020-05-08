#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""
from requests import get


def recurse(subreddit, hot_list=[], next=None):
    """ Top ten post """
    query_params = {'limit': 100}
    if next:
        query_params['after'] = next
    sub = get('https://www.reddit.com/r/{}/hot.json'.
              format(subreddit),
              headers={'user-agent': 'X-Modhash'},
              allow_redirects=False,
              params=query_params)
    if sub.status_code != 200:
        return(None)
    else:
        data_json = sub.json()
        parsed_data = data_json.get('data')
        posts = parsed_data.get('children')
        hot_list += posts
        next_list = parsed_data.get('after')
        if next_list:
            return(recurse(subreddit, hot_list, next_list))
        else:
            return(hot_list)
