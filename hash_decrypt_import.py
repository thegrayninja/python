import crypt
import random
from array import *
import sys

sys.setrecursionlimit(15000)  #may not be necessary..?

oldhash = "hash_from_/etc/shadow/$type$salt$hash" ("Please enter the full hash: ")
password_length = int(raw_input("Please enter the length of password: "))
salt = salt_from_oldhash #raw_input("Please enter the salt: ")

hash_types = """1 = MD5 hashing algorithm.
2 =Blowfish Algorithm is in use.
2a=eksblowfish Algorithm
5 =SHA-256 Algorithm
6 =SHA-512 Algorithm
"""

print(hash_types)
hash_type = hash_type_from_above #int(raw_input("Please Enter the number for the hash type(1-6)"))

updatedFile = open("all_combinations_pw_%s.txt" % (str(password_length)), "r") #reads existing combo file
pwcombos = updatedFile.readlines()
updatedFile.close()

total_guesses = 1
def hack_password():
	for i in pwcombos:
		new_hash = crypt.crypt(i.strip(),'$%d$%s' % (hash_type, salt))
		print (new_hash)
		if new_hash == oldhash:
			print("match! The password is: %s. And it only took %d guesses" % (i.strip(), total_guesses))
			break
		else:
			print("%d)no match :(. password guessed is: %s" %(total_guesses, i.strip()))
			global total_guesses 
			total_guesses +=1
			pass

hack_password()
