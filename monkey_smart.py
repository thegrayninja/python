import random
from array import *


def monkey():
	alphabet = "abcdefghijklmnopqrstuvwxyz "
	sentence= "methinks it is like a weasel"
	random_sentence = []
	tries = 1
	while sentence != ''.join(random_sentence):
		random_sentence = []
		
		count = 0
		while count < len(sentence):
			value = random.randrange(len(alphabet))
			if alphabet[value] == sentence[count]:
				random_sentence.insert(count,alphabet[value])	
				count += 1	
			else:
				pass
			
		print("%d. %s \n" % (tries, ''.join(random_sentence)))
		tries += 1

monkey()
