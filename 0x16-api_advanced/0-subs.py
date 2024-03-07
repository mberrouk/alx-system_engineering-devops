#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests


def number_of_subscribers(subreddit):
    """ return the number of subscribers or 0. """

    headers = {"User-Agent": "Alxapi"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 299:
        return res.json().get("data").get("subscribers")
    return 0
