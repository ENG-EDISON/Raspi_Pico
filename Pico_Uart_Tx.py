import time
from machine import UART

#create a Uart object.
# Use uart1 and set baudrate to 9600.
uart = UART(1, 9600)
#Forever running loop
while(True):
    #Write the bits to the uart port
    uart.write("Hello World!\n")
    #Delay for 1 second
    time.sleep(1);