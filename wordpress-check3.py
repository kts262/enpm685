#!/usr/bin/python

import sys
import requests


def check_url(url):
  try:
    r = requests.get(url)
    if r.status_code == 200:
	print url + " - FOUND -- POSSIBLE WORDPRESS SITE"
    else:
        print url + " - NOT found"
  except Exception, e:
    pass

def print_robots(url):
  try:
    r = requests.get(url)
    if r.status_code == 200:
      print "\n" + url + " - FOUND -- robots.txt content:\n"
      print r.content
    else:
      print url + " - NOT found"
  except Exception, e:
    pass

httpsvr = sys.argv[1]

print "Checking " + httpsvr + "..."
check_url(httpsvr + "/readme.html")
check_url(httpsvr + "/wp-admin/admin-ajax.php")
print_robots(httpsvr + "/robots.txt")
