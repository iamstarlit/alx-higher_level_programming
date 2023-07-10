#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8) using urllib and sys.
"""

from sys import argv
from urllib import request
from urllib import parse


if __name__ == '__main__':

    url = argv[1]
    email = {'email': argv[2]}
    data = parse.urlencode(email).encode('utf-8')

    with request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
