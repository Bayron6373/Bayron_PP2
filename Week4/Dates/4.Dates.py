#Try it yourself
import datetime

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A")) #Weekday
print(x.strftime("%B")) #Month

import datetime
x = datetime.datetime(2021 , 11 , 20, 21,15,56) #The datetime() class also takes parameters for time and timezone
print(x)

import datetime

x = datetime.datetime(2004,12,6)
print(x.strftime("%B"))
