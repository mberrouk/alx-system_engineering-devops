#!/usr/bin/python3
"""Queries the Reddit API and returns the top 10 hot posts"""
import requests


def top_ten(subreddit):
"""Print the top 10 hot posts or print None"""

    headers= {"User-Agent": "My-User-Agent"}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    res = requests.get(url, headers, allow_redirects=False)
    if res.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in res.json().get("data").get("children")]
