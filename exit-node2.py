#!/usr/bin/python

import urllib2

f = open("tor_exit_nodes.txt", 'wb')

response = urllib2.urlopen('https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=1.1.1.1&port=80')
exit_list = response.read()
exit_list = exit_list.split("\n")
exit_list.pop()  # delete that last blank line
i = 0
print "Pulling Tor exit node list..."

for line in exit_list:
        if line[0] != "#":
                f.write(line + ",\n")
                i = i+1

print "Done. " + str(i) + " exit nodes"

