#!/usr/bin/python3

import sys
import requests


def check_url(url):
  r = requests.get(url)
  if r.status_code == 200:
    print(url + " - FOUND -- POSSIBLE WORDPRESS SITE")
  else:
    print(url + " - NOT found")

def print_robots(url):
  r = requests.get(url)
  if r.status_code == 200:
    print ("\n" + url + " - FOUND -- robots.txt content:\n")
    print(r.text)
  else:
    print(url + " - NOT found")

httpsvr = sys.argv[1]

print("Checking " + httpsvr + "...")
check_url(httpsvr + "/readme.html")
check_url(httpsvr + "/wp-admin/admin-ajax.php")
print_robots(httpsvr + "/robots.txt")
