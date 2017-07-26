#github.com/thegrayninja

#a "simple" way to determine if the student figures out the area of a circle
#doing so without using x amount of decimal points, but still requiring the user 
#to enter decimal values

#needs to be cleaned up a bit...


import math
import re


a = 2
b = math.pi

area = b*(a*a)

print(area)
user_guess = "12.5"
result = re.match('^\d*[.]\d?', user_guess)
if result:
    print("yes, there is enough data")
else:
    print("no, try again")
    

    
user_guess_list = []
for i in user_guess:
    user_guess_list.append(i)

    
#print (user_guess_list)
user_guess_len = (len(user_guess_list))

area_answer = []
for i in str(area):
    area_answer.append(i)
    
true_area = area_answer[:user_guess_len]
print(true_area)

truest_area = ""
for i in true_area:
    truest_area += i
    
print (truest_area)

if user_guess == truest_area:
    print ("yaya!")
else:
    print ("nah, homie")
    
