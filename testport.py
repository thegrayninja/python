#simple script to identify if a port is open on a host
#syntax: .\testport.py website.com 443
#synatx: .\testport.py 10.0.0.1 22

from sys import argv
import socket

self, url, port = argv 									#need 'self' to satisfy argv values

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 	#socket stuff
s.settimeout(0.75)										#obvious

iport = int(port) 										#convert string to int
result = s.connect_ex((url, iport)) 					#result will be an integer

if result == 0: 										#0 means the port is open
	print("%d is open :)" % (iport))
else:
	print("%d is closed :(" % (iport))
