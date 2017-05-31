#thegrayninja

import crypt
import random
from array import *


oldhash = "$6$SALTsalt$hashedvalue"
#alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(),./<>?;':[]{}-=_+` \|\""
alphabet = "test"
new_password="test"
password_length = int(raw_input("Please enter the length of password: "))
salt = raw_input("Please enter the salt: ")
hash_types = """1 = MD5 hashing algorithm.
2 =Blowfish Algorithm is in use.
2a=eksblowfish Algorithm
5 =SHA-256 Algorithm
6 =SHA-512 Algorithm
"""

print(hash_types)
hash_type = int(raw_input("Please Enter the number for the hash type(1-6)"))

total_guesses = 1
def hack_password():
	
	newnew_password=[]
	count=0
	while count < password_length:	
		value = random.randrange(len(alphabet))
		newnew_password.insert(count,alphabet[value])
		count +=1
		the_password = ''.join(newnew_password)		
	print (the_password)
	new_hash = crypt.crypt(the_password,'$%d$%s' % (hash_type, salt))
	print (new_hash)
	if new_hash == oldhash:
		print("match! The password is: %s. And it only took %d guesses" % (the_password, total_guesses))
	else:
		print("%d)no match :(. password guessed is: %s" %(total_guesses, the_password))
		global total_guesses
		total_guesses +=1
		hack_password()


hack_password()
