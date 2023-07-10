#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

from sys import argv
import requests


if __name__ == '__main__':

    letter = '' if len(argv) == 1 else argv[1]
    res = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})

    try:
        res = res.json()
        if res == {}:
            print('No result')
        else:
            print('[{}] {}'.format(res.get('id'), res.get('name')))
    except ValueError:
        print('Not a valid JSON')
