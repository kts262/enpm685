#!/usr/bin/python3

# updated for Python 3

# Sample usage:
# $ python3 wget.py https://umd.edu response.txt

import urllib.request
import sys

# sys.argv[1] = url
# sys.argv[2] = file name

url = sys.argv[1]
file_name = sys.argv[2]

# Execute the request
response = urllib.request.urlopen(url)

# Store the response to a local file in the current directory
with open(file_name, mode="wb") as response_file:
    response_file.write(response.read())
