#!/usr/bin/python

import urllib2
from optparse import OptionParser

parser = OptionParser(usage="Usage: %prog [-f format] file")
parser.add_option("-f", dest="format", help="output format to use [csv, palo, iptables]")

options, args = parser.parse_args()

if len(args) < 1:
	parser.error("Wrong number of arguments")

f = open(args[0], 'wb')

response = urllib2.urlopen('https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=1.1.1.1&port=80')
exit_list = response.read()
exit_list = exit_list.split("\n")
exit_list.pop()  # delete that last blank line
i = 0
print "Pulling Tor exit node list..."
print "Output option selected: " + options.format

for line in exit_list:
        if line[0] != "#":
		if options.format == "csv":
                	line_output = line + ",\n"
		elif (options.format == "palo") or (options.format == "cidr"):
			line_output = line + "/32\n"
		f.write(line_output)
                i = i+1

print "Done. " + str(i) + " exit nodes"

