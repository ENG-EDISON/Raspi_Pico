from machine import Pin
import utime
#Set trigger Pin to be connected to pin 3 and set the pin as OUTPUT
trigger = Pin(3, Pin.OUT)
#Set echo Pin to be connected to pin 2 and set the pin as INPUT
echo = Pin(2, Pin.IN)
#A function to read measure distance 
def ultra():
    timepassed=0;
    startTime=0;
    stopTime=0;
    #Sending a pulse to the trigger pin begin 0
    #First,set trigger Pin low
    trigger.low()
    #set the trigger pin low for 2 microsecond
    utime.sleep_us(2)
    #set the trigger pin high
    trigger.high()
    #set the trigger pin low for 5 microsecond
    utime.sleep_us(5)
    #set the tirgger pin low
    trigger.low()
    #Sending a pulse to the trigger pin end 0
    #wait for the echo pulse
    while echo.value() == 0:
        startTime = utime.ticks_us()
    while echo.value() == 1:
        stopTime = utime.ticks_us()
    timepassed = stopTime - startTime
    distance = (timepassed * 0.0343) / 2
    print("The distance from object is ",distance,"cm")
   
while True:
   ultra()
   utime.sleep(1)