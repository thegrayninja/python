#thegrayninja
#source: https://gist.github.com/nmcv/3997853

import itertools

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(),./<>?;':[]{}-=_+` \|\""
pwlength = int(raw_input("Please enter the password length: "))
count = 0
x=""
total = 0
for combination in itertools.product(alphabet, repeat=pwlength):
    x += ''.join(map(str, combination))+'\n'


updatedFile = open("all_combinations_pw_%s.txt" % (str(pwlength)), "w") #creates new file
updatedFile.write(x)		#then writes to file
updatedFile.close()
