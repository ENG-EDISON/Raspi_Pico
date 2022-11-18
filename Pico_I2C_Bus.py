from machine import Pin, SoftI2C
import time
#create an I2C object
#set SCL_PIN->GPIO5
#set SDA_PIN->GPIO4
#set frequency to 100kHz
i2c = SoftI2C(scl=Pin(5), sda=Pin(4), freq=100_000)
# scan for devices
i2c.scan()
while True:
    # read 4 bytes from device with address 0x3a
    i2c.readfrom(0x3a, 4)
    # write '12' to device with address 0x3a
    # create a buffer with 10 bytes
    i2c.writeto(0x3a, '12')
    buf = bytearray(10)
    # write the given buffer to the peripheral
    i2c.writeto(0x3a, buf)
    time.sleep(1)