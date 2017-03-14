import csv
from sys import argv

#####
#####
#####
#usage: test_csv.py <original_file_name> <new_file_name>
#yes, old file name must exist
#both old and new file names are required
#####
#####
#####


#opens your csv file and saves the good stuff to x
x = ""
with open(argv[1], 'rb') as csvfile:
		
	delimfile = csv.DictReader(csvfile)
	for row in delimfile:


		if 'None' in row['Risk']:
			print ('None')
		else:
			x = x + '%s,%s,%s,%s,%s,%s,%s\n' %(row['Host'], row['Risk'], row['CVSS'], row['CVE'], row['Port'], row['Protocol'], row['Name'])
csvfile.close()


#to save the good stuff to a new file
with open(argv[2], 'a') as csvnew:
	csvnew.write('Host, Risk, CVSS, CVE, Port, Protocol, Name\n')
	csvnew.write(x)

csvnew.close()
