from machine import WDT
import machine
import time
# enable the WDT with a timeout of 5s (1s is the minimum)
led=machine.Pin(25,machine.Pin.OUT);
#create a watchdog object and set timeout to 5s
wdt = WDT(timeout=5000)
#Turn led on
led.on()
time.sleep(2)
while True:
    #Refresh the counter
    wdt.feed()
    #Turn Led off
    led.off()
    #Delay 2 seconds
    time.sleep(2)
