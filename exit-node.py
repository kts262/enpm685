#!/usr/bin/python

import urllib2

response = urllib2.urlopen('https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=1.1.1.1&port=80')
exit_list = response.read()
exit_list = exit_list.split("\n")
exit_list.pop()  # delete that last blank line

for line in exit_list:
        if line[0] != "#":
                print line + ","

