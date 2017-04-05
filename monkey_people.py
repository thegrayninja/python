import random
from array import *
import time

def monkey():
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(),./<>?;':[]{}-=_+` \|\""
	sentence = raw_input("Please enter something: ")	
	current_time = lambda: int(round(time.time() * 1000))
	print("start time: %s" % (current_time()))
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
		print("completed at: %s" % (current_time()))
		tries += 1

monkey()
