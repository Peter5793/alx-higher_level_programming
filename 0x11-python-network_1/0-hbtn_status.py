#!/usr/bin/python3
import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()


