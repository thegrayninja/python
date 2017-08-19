##github.com/thegrayninja

## 4! = 4*3*2*1


no_of_char = raw_input("Please enter number of characters: ")
no_of_slots = raw_input("Please enter the number of spaces: ")

i = 1
no_char = int(no_of_char)
total = int(no_of_char)
while i < int(no_of_slots):
	if no_char != 1:
		total *= (no_char -1)
		no_char -= 1
		i += 1
	else:
		i += 1
print(total)


