from machine import RTC
import time
#Create RTC object
rtc = machine.RTC()
while True:
    #@hi variable stores the current datetime in a list
    hi=rtc.datetime()
    #Use list indexing to get the datetime 
    print("Year=",hi[0],"Month=",hi[1],"date=",hi[2],"Hour=",hi[4],"Min=",hi[5],"Sec=",hi[6])
    #Delay for 1 second
    time.sleep(1)