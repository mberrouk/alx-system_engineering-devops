#!/usr/bin/python3
""" Function that queries the Reddit API and returns the number of subscribers. """

import requests

def number_of_subscribers(subreddit):
    """ return the number of subscribers or 0. """
    headers = {"User-Agent": "Alxapi"}
    response = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit),
                            headers=headers, allow_redirects=False)
    if response.status_code > 299:
        return 0
    return response.json().get("data").get("subscribers")
