import os
import subprocess

#have a text file that contains ips, listed in a column
with open("temp_ip.txt", "r") as temp_ip_list:
	ip_list=temp_ip_list.readlines()
temp_ip_list.close()

whodat = ""
for i in ip_list:
	whois_format = 'whois %s | grep -E "Customer|Organization|NetRange|CIDR"' % (i.strip())
	whois_data = os.popen(whois_format).read()
	whodat += whois_data

temp_whois = open("cidr_whois.txt", "a")
temp_whois.write(whodat)
temp_whois.close()
