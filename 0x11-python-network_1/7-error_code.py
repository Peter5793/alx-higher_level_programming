#!/usr/bin/python3
"""
 takes in a URL, sends a request to the URL and displays the body of the
 response
"""

import sys.argv
import requests

if __name__ == "__main__":
    url = argv[1]
    r = requests(url)
    try:
        r.raise_for_status()
        print(r.text)
    except Exceptions as e:
        print("Error code: {}".format(r.status_code))
