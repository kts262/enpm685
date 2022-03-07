#!/usr/bin/python3

import csv

# read in CSV of all users
# compare to list of completed users
# if user is not in completed output their information

# completed format
# 0 = name
# 1 = email

# all users format
# 0 = username
# 1 = first, 2 = last
# 3 = title, 4 = phone, 5 = dept 

completedusers = []

completed_file = open("completed.csv","r")
completed_reader = csv.reader(completed_file)
completed_count = 0

for row in completed_reader:
	# Skip the header "Email"
	if row[1] != "Email":
		# build the list but let's strip "@enpm685.com"
		# this will return only the user name part of the email
		username = row[1].split("@")[0]
		completedusers.append(username)
		completed_count = completed_count + 1

remaining_count = 0

allusers_file = open("allusers.csv","r")
allusers_reader = csv.reader(allusers_file)

print("\nRemaining users:")
print("----------------")

# skipping the CSV "header" 
next(allusers_reader)

for row in allusers_reader:
	if row[0] not in completedusers:
		# output user, email, name
		print(row[0] + "," + row[0] + "@enpm685.com," + row[1] + " " + row[2])
		remaining_count = remaining_count + 1

# str() to change our int to a string
print("\nUsers completed training: " + str(completed_count))
print("Users still need to complete training: " + str(remaining_count))
