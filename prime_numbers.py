#github.com/thegrayninja
##prime number

x_input = raw_input("Please enter a number: ")
x = int(x_input)
primeno = 0
divide_by = x
divisible_numbers = ""

i = 1
while i < ((x/2)+1):
	if i != 1:
		print(i)
		if x % i == 0:
			divisible_numbers += "%d is divisible by %d.\n" % (x, i)
			primeno = 1
	i +=1
			

if primeno == 1:
	print("%d is not a prime number!\n****\n%s" % (x, divisible_numbers))
else:
	print("%d is a prime number!" %(x))
		
