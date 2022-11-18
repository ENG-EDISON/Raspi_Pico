import time
from machine import UART

# UART 3, and baudrate.
uart = UART(1, 9600)

while(True):
    uart.write("Hello World!\n")
    time.sleep(1);