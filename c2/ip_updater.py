#!/usr/bin/env python3

# Server IP Updater for NoSerpent Cyberattack
# Made By Narek K. and Adel B.

'''
Update given IP in these files:

- client.py
- static/js/app.95c21043.js
- static/js/app.95c21043.js.map
'''

files = ['client.py', 'static/js/app.95c21043.js', 'static/js/app.95c21043.js.map']

# get argument ip


for filepath in files:
	with open(filename, 'r') as file :
		filedata = file.read()

	filedata = filedata.replace('<SERVER_IP>', '')

with open('example.txt', 'w') as file:
file.write(filedata)

f = open("example.txt", "r")
print("after change")
print(f.read())