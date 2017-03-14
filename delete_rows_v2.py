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
	delimfile = csv.DictReader(csvfile)
	for row in delimfile:


		if 'None' in row['Risk']:
			print ('None')
		else:
			x = x + '%s,%s' %(row['Host'], row['Risk'])
csvfile.close()


#to save the good stuff to a new file
with open(argv[2], 'a') as csvnew:
	csvnew.write(x)

csvnew.close()
