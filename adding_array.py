#github.com/thegrayninja
#a+b=c...2 items in array to equal the second value in the list

list1 = ([7,10,13,55,68,8,3,2,4],17)
list_len = (len(list1[0]))

c = list1[1]

a = 0
b = 1
for i in list1[0]:
	while b < (list_len):
		if (list1[0][a]+list1[0][b]) == c:
			print ("%d+%d=%d" % (list1[0][a],list1[0][b],c))
			break
		
		b += 1
	a +=1
	b = (a+1)	
		
print ("loop is over")
