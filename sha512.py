#with help from the following:
#http://www.slashroot.in/how-are-passwords-stored-linux-understanding-hashing-shadow-utils
#https://stackoverflow.com/questions/329956/python-crypt-module-whats-the-correct-use-of-salts
#http://jasonwyatt.co/post/40138193838/generate-hashed-passwords-and-salts-with-python


##notes:
#$1 = MD5 hashing algorithm.
#$2 =Blowfish Algorithm is in use.
#$2a=eksblowfish Algorithm
#$5 =SHA-256 Algorithm
#$6 =SHA-512 Algorithm

import crypt
x = crypt.crypt('mypassword','$6$sAlTSAlt')
print(x)
