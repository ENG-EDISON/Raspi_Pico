import machine
import time
LED=2;
led = machine.Pin(LED, machine.Pin.OUT)
while True:
    led.off()
    time.sleep(1)
    led.on()
    time.sleep(1)