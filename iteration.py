
#from itertools import product
#from itertools import combinations


##same, but without duplicates:
#word = list(combinations(alphabet, 2))
#print(word)

#for i in word:
#	print(''.join(i))

import itertools

alphabet = "abcd "
count = 0
x=""
total = 0
for combination in itertools.product(alphabet, repeat=4):
    x += ''.join(map(str, combination))+'\n'


print(x)
for i in x:
	total += 1

print (total)
