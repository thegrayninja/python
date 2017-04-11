first_word = raw_input("Please enter word #1: ")
second_word = raw_input("Please enter word #2: ")

def compare_words(first_string, second_string):
	dict1 = {}
	dict2 = {}
  
	count = 0
	for i in first_string:
		if i in dict1:
			count +=1	
			dict1[i] = count
		else:
			count = 1
			dict1[i] = count

	re_count = 0
	for i in second_string:
		if i in dict2:
			re_count +=1	
			dict2[i] = re_count
		else:
			re_count = 1
			dict2[i] = re_count


	if dict1 == dict2:
		print ("%s and %s contain the same letters!" % (first_word,second_word))
	else:
		print ("%s and %s DO NOT contain the same letters :(" % (first_word,second_word))


compare_words(first_word.lower(),second_word.lower())
