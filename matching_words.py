#github.com/thegreyinja
first_word = raw_input("Please enter word #1: ")
second_word = raw_input("Please enter word #2: ")

def compare_words(first_string, second_string):
	dict1 = {}
	dict2 = {}
	dict3 = []

	for i in first_string:
		if i in dict1:	
			dict1[i] += 1
		else:
			dict1[i] = 1

	for i in second_string:
		if i in dict2:	
			dict2[i] += 1
		else:
			dict2[i] = 1


	if dict1 == dict2:
		print ("%s and %s contain the same letters!" % (first_word,second_word))
	else:
		print ("%s and %s DO NOT contain the same letters :(" % (first_word,second_word))

	for i in reversed(second_string):
		dict3.append(i)
	third_string = ''.join(dict3)
	
	if first_string == third_string:
		print ("%s is %s spelled backwards :P" % (second_word, first_word))
	#remove next comment for debugging! :)	
	#print ("%s and %s" % (dict1, dict2))

compare_words(first_word.lower(),second_word.lower())
