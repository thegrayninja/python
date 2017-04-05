import random

def monkey():
	alphabet = "abcdefghijklmnopqrstuvwxyz "
	sentence= "methinks it is like a weasel"
	random_sentence = ""
	tries = 1
	while sentence != random_sentence:
		random_sentence = ""
		count = 0
		while count < len(sentence):
			value = random.randrange(len(alphabet))
			random_sentence = random_sentence + alphabet[value]
			count += 1
			
		print("%d. %s \n" % (tries, random_sentence))
		tries += 1

monkey()
