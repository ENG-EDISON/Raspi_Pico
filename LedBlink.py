import machine
import time
#Use GPIO naming Convention.
LED=2;
#Create a Led object
#set the Led as either INPUT or OUTPUT
led = machine.Pin(LED, machine.Pin.OUT)
#Forever running loop
while True:
    #Turn the led on
    led.off()
    #Delay for 1 second
    time.sleep(1)
    #Turn led off
    led.on()
    #Delay for 1 second
    time.sleep(1)