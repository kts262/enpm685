#!/usr/bin/python3

import requests
from optparse import OptionParser

parser = OptionParser(usage="Usage %prog [-f format] file")
parser.add_option("-f", dest="format", help="output format to use [csv ,palo, iptables]")

options, args = parser.parse_args()

if len(args) < 1:
    parser.error("You need to specify a format and a file name")
    sys.exit(0)

f = open(args[0], "w")

exit_list_url = requests.get('http://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=1.1.1.1&port=80')

exit_list = exit_list_url.text
exit_list = exit_list.split("\n")
exit_list.pop()  # delete that last blank line

i = 0
print("Pulling Tor exit node list...")
print("Output option selected: " + options.format)

for line in exit_list:
        if line[0] != "#":
                if options.format == "csv":
                    line_output = line + ",\n"
                elif (options.format == "palo") or (options.format == "cidr"):
                    line_output = line + "/32\n"
                elif options.format == "iptables":
                    line_output = "sudo iptables -A INPUT -s " + line + " -j DROP\n"
                f.write(line_output)
                i = i + 1

print("Done, " + str(i) + " exit nodes")
