# basic, but useful in a pinch

import time

def GetCurrentTime():
    return(time.strftime('%X %x %Z'))
    
    
#returns HH:MM:SS MM:DD:YY TimeZone

#print(GetCurrentTime())



#import datetime

#
# newtime = "2018-09-25T16:49:38.000+0000"
#
# LastScannedTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(newtime))

# print(newtime)
#
# #print(time.strftime('%X %x %Z', newtime))
#
# datetime_object = datetime.strptime(newtime, '%b %d %Y %I:%M%p')


import datetime
lastScannedTime = "2018-09-25T16:49:38.000+0000"
finalTime = datetime.datetime.strptime(lastScannedTime, "%Y-%m-%dT%H:%M:%S.000+0000").strftime('%B %d, %Y %I:%M %p')
print(finalTime)
