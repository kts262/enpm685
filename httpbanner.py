#!/usr/bin/python3

import sys
import requests

httpsvr = sys.argv[1]

response = requests.get(sys.argv[1])

print(sys.argv[1] + ' web server is: ' + response.headers['Server'])
