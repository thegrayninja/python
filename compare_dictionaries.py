#github.com/thegrayninja
#for use with the scrabble helper/english treasure mapper tool
#if random word has a higher count of the same letter when compared to xuser,
#the word is invalid. 
#ideal for scrabble, you can't make pool if you only have one o


xuser = "people"
yrandom = "pool"

x = {}
y = {}

for i in xuser:
    if i not in x:
        x[i] = 1
    else:
        x[i] += 1

for i in yrandom:
    if i not in y:
        y[i] = 1
    else:
        y[i] += 1


#x = {"p":2,"e":2,"o":1,"l":1}
#z = "pool"
#y = {"p":1,"o":2,"l":1}


#ycount = len(y)

count = 0
#while count < len(y)

print(x.get("p"))
for i in yrandom:
    xtotal = x.get(i)
    ytotal = y.get(i)
    if ytotal > xtotal:
        print("People has %d '%s'" % (xtotal, i))
        print("Pool has %d '%s'" % (ytotal, i))
        print ("Pool has more '%s' than People. Not a valid option." % (i))
        break
    else:
        print("People has %d '%s'" % (xtotal, i))
        print("Pool has %d '%s'" % (ytotal, i))


