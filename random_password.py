#github.com/thegreyninja
#not quite random as you can see..but it's a start

import random
from array import *


def random_password():
	alphabet_lower = "abcdefghijklmnopqrstuvwxyz!"
	alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	alphabet_special = "@#$%^&*(),./<>?;':[]{}-=_"
	alphabet_number = "1234567890"

	random_pw = []
	count = 0
	while count < 16:
		value = random.randrange(len(alphabet_lower))
		random_pw.insert(count,alphabet_lower[value])
		count += 1
		value = random.randrange(len(alphabet_upper))
		random_pw.insert(count,alphabet_upper[value])
		count += 1
		value = random.randrange(len(alphabet_special))
		random_pw.insert(count,alphabet_special[value])
		count += 1
		value = random.randrange(len(alphabet_number))
		random_pw.insert(count,alphabet_number[value])
		count += 1
	
	
	random.shuffle(random_pw)
	print (''.join(random_pw))

random_password()
