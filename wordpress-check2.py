#!/usr/bin/python

import sys
import requests


def check_url(url):
  r = requests.get(url)
  if r.status_code == 200:
    print(url + " - FOUND -- POSSIBLE WORDPRESS SITE")
  else:
    print(url + " - NOT found")

httpsvr = sys.argv[1]

print("Checking " + httpsvr + "...")
check_url(httpsvr + "/readme.html")
check_url(httpsvr + "/wp-admin/admin-ajax.php")
