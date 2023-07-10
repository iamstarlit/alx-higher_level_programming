#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
using requests module
"""

import requests

if __name__ == '__main__':

    res = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(res.text.__class__))
    print('\t- content: {}'.format(res.text))
