#thegrayninja
#source: https://gist.github.com/nmcv/3997853

import itertools

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(),./<>?;':[]{}-=_+` \|\""
#alphabet = "test"
pwlength = int(raw_input("Please enter the password length: "))


updatedFile = open("all_combinations_pw_%s.txt" % (str(pwlength)), "a") #creates new file
for combination in itertools.product(alphabet, repeat=pwlength):
    updatedFile.write(''.join(map(str, combination))+'\n')		#then writes to file
	
updatedFile.close()
