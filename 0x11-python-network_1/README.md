# Python - Network

## General
* How to fetch internet resources with the Python package urllib
* How to decode urllib body response
* How to use the Python package requests #requestsiswaysimplerthanurllib
* How to make HTTP GET request
* How to make HTTP POST/PUT/etc. request
* How to fetch JSON resources
* How to manipulate data from an external service

----------------------------------------------------------------------------------

### Tasks
Script that fetches ```https://intranet.hbtn.io/status```

```
hp@Peter-Lugalia MINGW64: ~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
```

Send request to URL and dispaly the valie of the ```X-request-Id```

```
hp@Peter-Lugalia MINGW64 ~/0x11$ /1-hbtn_header.py https://intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
hp@Peter-Lugalia MINGW64
hp@Peter-Lugalia MINGW64 ~/0x11$ /1-hbtn_header.py https://intranet.hbtn.io
6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
```
Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)

Script is tested on the port provided using the web server running on port 5000

```
hp@Peter-Lugalia MINGW64 ~/0x11$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
````