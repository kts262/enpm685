#!/usr/bin/python3

import requests

exit_list_url = requests.get('http://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=1.1.1.1&port=80')
exit_list = exit_list_url.text
exit_list = exit_list.split("\n")
exit_list.pop()  # delete that last blank line

for line in exit_list:
        if line[0] != "#":
                print(line + ",")
