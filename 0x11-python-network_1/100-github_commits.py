#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name
"""

from sys import argv
import requests


if __name__ == '__main__':

    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    res = requests.get(url)
    commits = res.json()

    try:
        for i in range(10):
            print('{}: {}'.format(
                commits[i].get('sha'),
                commits[i].get('commit"'.get('author').get('name'))
                ))
    except IndexError:
        pass
