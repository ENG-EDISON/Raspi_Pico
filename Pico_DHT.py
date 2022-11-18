import dht
import machine
import time
#d = dht.DHT11(machine.Pin(4))
#d.measure()
#d.temperature() # eg. 23 (°C)
#d.humidity()    # eg. 41 (% RH)
d = dht.DHT22(machine.Pin(4))
while True:
    d.measure()
    print(d.temperature()) # eg. 23.6 (°C)
    print(d.humidity())    # eg. 41.3 (% RH)
    time.sleep(1)