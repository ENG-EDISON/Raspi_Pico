from machine import Pin
import time

#create a pin object and select the GPIO number
pin = Pin(5,Pin.IN,Pin.PULL_UP)
#Create a pin object where the LED is connected(use 25 for onboard led)
#Configure the pin as OUTPUT
led = Pin (25,Pin.OUT);

#Define a callback function to be called when the 'pin' is pressed
def callback(pin):
    #If led is ON,turn the led OFF
    if led.value()==1:
        led.off()
    #If led is OFF,turn the led ON
    else:
        led.on()
#set up the 'pin' as interrupt and attach the callback function to be called
#when the pin is pressed
#The interrupt has been set to trigger on falling edge detection
pin.irq(trigger=Pin.IRQ_FALLING, handler=callback)

while True:
    #if led is on,print "Led ON"
    if led.value()==1:
        print("Led ON")
    #if led is OFF,print "Led OFF"
    else:
        print("Led OFF")
    #Delay for 1 second
    time.sleep(1)