#github.com/thegrayninja
##prime number
##warning - 7+ digits puts a stress on your memory

x_input = raw_input("Please enter a number: ")
x = int(x_input)
primeno = 0
divide_by = x
divisible_numbers = ""

for i in range(x):
	i2 = i+1
	if i2 != 1:
		if i2 != x:
			if x % i2 == 0:
				divisible_numbers += "%d is divisible by %d.\n" % (x, i2)
				primeno = 1
			

if primeno == 1:
	print("%d is not a prime number!\n****\n%s" % (x, divisible_numbers))
else:
	print("%d is a prime number!" %(x))
		
