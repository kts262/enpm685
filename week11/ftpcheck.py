#!/usr/bin/python

import sys
import ftplib

def anonFTP(hostname):
  try:
    ftp = ftplib.FTP(hostname)
    ftp.login('anonymous', 'test@test.com')
    ftp.quit()
    return True 
  except Exception, e:
    return False

ftpsvr = sys.argv[1]

print ftpsvr + ": Checking anonymous FTP server status"
ftp_result = anonFTP(ftpsvr)
if ftp_result is not False:
  print "[+] " + ftpsvr + " is an anonymous FTP server"
else:
  print "[-] " + ftpsvr + " is either offline or not an FTP server"
