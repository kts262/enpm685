#!/usr/bin/python3
"""
Consult TOR exit node list and produce a formatted file
"""
import sys
from argparse import ArgumentParser
import requests

def csv_format(ip_address):
    """
    return ip address with a comma
    """
    return f"{ip_address},"

def cidr_format(ip_address):
    """
    return ip address in cidr notation
    """
    return f"{ip_address}/32"

def iptables_format(ip_address):
    """
    return ip address for firewall configuration drops
    """
    return f"sudo iptables -A INPUT -s {ip_address} -j DROP"

def default_format(ip_address):
    """
    just return the ip address
    """
    return ip_address


parser = ArgumentParser(description="Usage %prog [-f format] file")
parser.add_argument("-f", dest="format", help="output format to use [csv ,palo, iptables]")

args, rest_of_args = parser.parse_known_args()

if args.format == "csv":
    format_func = csv_format
elif args.format in ['cidr', 'palo']:
    format_func = cidr_format
elif args.format == "iptables":
    format_func = iptables_format
else:
    format_func = default_format

print("Pulling Tor exit node list...")

exit_list = requests.get('http://check.torproject.org/cgi-bin/' +
                         'TorBulkExitList.py?ip=1.1.1.1&port=80').text.split("\n")

if args.format:
    print(f"Output option selected: {args.format}")
if len(rest_of_args) > 0:
    exit_filename = rest_of_args[0]
else:
    print("No filename specified")
    sys.exit()

formatted_exit_list = [ format_func(line) for line in exit_list if line and line[0] != "#" ]

with open(exit_filename, 'w+', encoding="utf-8") as exit_out:
    print("\n".join(formatted_exit_list), file = exit_out)

exit_list_count = len(formatted_exit_list)

print(f"Done, {exit_list_count} exit nodes written to {exit_filename}")
