from machine import UART,Pin
import time

Uart_Dev=UART(0,baudrate=115200,tx=Pin(0),rx=Pin(1))
rxdata=bytes()
counter=0;
counter2=0
while True:
    if Uart_Dev.any()>0:
        rxdata=Uart_Dev.read()
        command= rxdata.decode('utf-8')
        if "t" in command: #send temperature back
            n=str(counter)+'t-'
            counter+=10
            Uart_Dev.write(n)
        if "s" in command: # send Speed back
            k=str(counter2)+'s-'
            counter2+=2
            Uart_Dev.write(k)
