#!/usr/bin/python

import sys
import httplib

def getHTTPHeaders(hostname):
  try:
    http = httplib.HTTPConnection(hostname)
    http.request("HEAD", "/")
    resp = http.getresponse()
    server = resp.getheader('Server')
    return server
  except Exception, e:
    return False

httpsvr = sys.argv[1]

header = getHTTPHeaders(httpsvr)
if header is not False:
  print httpsvr + " HTTP server is: \'" + str(header) + "\'"
else:
  print  httpsvr + " Could not get HTTP Server info"
