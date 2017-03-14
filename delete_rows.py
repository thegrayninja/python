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
		#for reference, the test.csv file contains 1 word on each line: Spamming, Spam, spammerson, spamdude
	
	for line in csvfile:
		if 'pamm' in line:
			print ('pamm')
			#line = ''
		else:
			x = x + '%s' %(line)
csvfile.close()


#to save the good stuff to a new file
with open(argv[2], 'a') as csvnew:
	csvnew.write(x)

csvnew.close()
