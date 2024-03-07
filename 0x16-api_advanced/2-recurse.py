#!/usr/bin/python3
"""Queries the Reddit API and returns all hot posts"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):

    headers = {"User-Agent": "linux:Alxapi:v1.0.0 (by /u/PitchSufficient4470)"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url, params={"count": count, "after": after},
                       headers=headers, allow_redirects=False)
    if res.status_code >= 400:
        return None

    chdren = [child.get("data").get("title")
            for child in res.json().get("data").get("children")]
    hots = hot_list + chdren
    args = res.json()
    if not args.get("data").get("after"):
        return hots

    return recurse(subreddit, hots, args.get("data").get("count"),
                   args.get("data").get("after"))
