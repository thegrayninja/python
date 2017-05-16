#github.com/thegrayninja
#yes..it's ugly. but it works

import csv
import os
import subprocess

with open("list_of_fqdn_sample.txt", "r") as temp_cidr_list:
	cidr_list=temp_cidr_list.readlines()
temp_cidr_list.close()



fdig = ""
for i in cidr_list:
	hostname = i.strip()
	formatdig = 'dig %s \@8.8.8.8 | grep %s' % (hostname, hostname)
	digresults = subprocess.check_output(formatdig, shell=True)
	print (digresults)
	fdig += digresults
	
temp_dig = open("temp_dig.txt", "a")
temp_dig.write(fdig)
temp_dig.close()

grepformat = 'grep -o "A.*" temp_dig.txt'
grepresults = subprocess.check_output(grepformat, shell=True)

xgrep = grepresults.replace("A\t", "")
xgrep = xgrep.replace("A","")
xgrep = xgrep.replace("\n\n","\n")
xgrep = xgrep.replace("\n\n","\n")
print(xgrep)

temp_dig = open("temp_ip.txt", "a")
temp_dig.write(xgrep)
temp_dig.close()


with open("temp_ip.txt", "r") as temp_ip_list:
	ip_list=temp_ip_list.readlines()
temp_ip_list.close()

whodat = ""
for i in ip_list:
	whois_format = 'whois %s | grep -E "NetRange|CIDR|Customer|Organization"' % (i.strip())
	whois_data = os.popen(whois_format).read()
	whodat += whois_data

temp_whois = open("cidr.txt", "a")
temp_whois.write(whodat)
temp_whois.close()

