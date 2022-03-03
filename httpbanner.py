#!/usr/bin/python3

import sys
import requests

# Fetch from the command line argument
httpsvr = sys.argv[1]

# Get the response from http server
response = requests.get(httpsvr)

if 'Server' in response.headers:
    print(httpsvr + ' web server is: ' + response.headers['Server'])
else:
    print(httpsvr + ' web server has following headers: ' + response.headers)
