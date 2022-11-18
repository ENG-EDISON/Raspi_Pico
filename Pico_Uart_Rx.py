import time
from machine import UART
#Create UART object 
# set the  UART port connected ->UART1
#set baudrate to 9600
uart = UART(1, 9600)
while(True):
    #Check if there is any data to be received
    if (uart.any()):
        #print what has been received
        uart.write(uart.read())
    #Delay for 1s    