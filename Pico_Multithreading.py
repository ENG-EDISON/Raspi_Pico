import _thread
import machine
import time

#Function to blink LED 1
def Led1():
    global lock
    while True:
        lock.acquire()
        #Turn led_1 ON
        Led_1.on()
        #Delay for 1 second
        time.sleep(1)
        #Turn led_1 OFF        
        Led_1.off()
        #Delay for 1 second
        time.sleep(1)
        lock.release()

def Led2():
    global lock
    while True:
        #Turn led_2 ON
        lock.acquire()
        Led_2.on()
        #Delay for 1 second
        time.sleep(1)
        #Turn led_2 OFF
        Led_2.off()
        #Delay for 1 second
        time.sleep(1)
        lock.release()

#Create a lock for suncronizing Tasks
lock=_thread.allocate_lock()
#Create two led objects
Led_1=machine.Pin(1,machine.Pin.OUT)
Led_2 =machine.Pin(2,machine.Pin.OUT)
#create a thread that will run on core 0
Thread1=_thread.start_new_thread(Led1,())
#The below code runs on core 1
Led2()