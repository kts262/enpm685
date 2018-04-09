#!/usr/bin/python

import urllib2
import sys

attempts = 0

while attempts < 3:
    try:
        response = urllib2.urlopen(sys.argv[1], timeout = 5)
        content = response.read()
        f = open(sys.argv[2], 'w' )
        f.write(content)
        f.close()
        break
    except urllib2.URLError as e:
        attempts += 1
        print type(e)
