from machine import ADC
import machine
import time

#create an ADC object
#Set pin connected to ADC signal to 27
adc = ADC(machine.Pin(27))          # create ADC object on ADC pin
while True:
    # read value, 0-65536 across voltage range 0.0v - 3.3v
    print(adc.read_u16())
    #Delay for 1 second
    time.sleep(1)