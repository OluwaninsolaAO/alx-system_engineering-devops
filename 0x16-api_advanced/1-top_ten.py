#!/usr/bin/python3
"""prints the titles of the first 10 hot posts
listed for a given subreddit"""
from requests import get


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts
    listed for a given subreddit"""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Python Scripts (by: /u/oluwaninsolaao)'}
    resp = get(url, headers=headers)

    if resp.ok:
        data = resp.json().get('data')
        if len(data.get('children')) != 0:
            for post in data.get('children')[:10]:
                print(post.get('data').get('title'))
            return
    print(None)
