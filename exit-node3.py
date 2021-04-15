#!/usr/bin/python3

import requests
import sys

if len(sys.argv) < 2:
    print("You need to specify a file name")
    sys.exit(0)

f = open(sys.argv[1], "w")

exit_list_url = requests.get('http://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=1.1.1.1&port=80')

exit_list = exit_list_url.text
exit_list = exit_list.split("\n")
exit_list.pop()  # delete that last blank line

i = 0
print("Pulling Tor exit node list...")

for line in exit_list:
        if line[0] != "#":
                f.write(line + ",\n")
                i = i + 1

print("Done, " + str(i) + " exit nodes")
