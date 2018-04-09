#!/usr/bin/python

import sys
import requests


def check_url(url):
  try:
    r = requests.get(url + "/readme.html")
    if r.status_code == 200:
	print url + " - FOUND -- POSSIBLE WORDPRESS SITE"
    else:
        print url + " - NOT found"
  except Exception, e:
    pass

httpsvr = sys.argv[1]

print "Checking " + httpsvr + "..."
check_url(httpsvr)
