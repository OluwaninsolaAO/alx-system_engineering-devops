#!/usr/bin/python3
""" returns a list containing the titles of all hot
articles for a given subreddit"""
from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """ returns a list containing the titles of all hot
    articles for a given subreddit"""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Python Scripts (by: /u/oluwaninsolaao)'}
    params = {'after': after}
    resp = get(url, headers=headers, params=params)

    if resp.ok:
        data = resp.json().get('data')
        if len(data.get('children')) != 0:
            for post in data.get('children'):
                hot_list.append(post.get('data'))
            after = data.get('after')

            if after is None:
                return hot_list
            return recurse(subreddit, hot_list=hot_list, after=after)

    return None
