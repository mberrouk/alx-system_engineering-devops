#!/usr/bin/python3

"""
Python script that using a REST API for a given employee ID,
returns information about a TODO list progress.
"""

from sys import argv
from requests import get


if __name__ == "__main__":
    finished = 0
    alls = 0
    tasks = []
    resp = get('https://jsonplaceholder.typicode.com/todos/')
    data = resp.json()
    response = get('https://jsonplaceholder.typicode.com/users')
    data2 = response.json()

    for i in data2:
        if i.get('id') == int(argv[1]):
            employee = i.get('name')

    for i in data:
        if i.get('userId') == int(argv[1]):
            alls += 1
            if i.get('finished') is True:
                finished += 1
                tasks.append(i.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee, finished,
                                                          alls))

    for i in tasks:
        print("\t {}".format(i))
