import machine
import sdcard
import uos
import time

cs = machine.Pin(1, machine.Pin.OUT)
led=machine.Pin(25,machine .Pin.OUT)

def Blink():
    #turn Led off
    led.off()
    #Delay for 1 second
    time.sleep(1)
    #Turn led off
    led.on()
    #Delay for 1 second
    time.sleep(1)
    #turn Led off
    led.off()
    
#get the sdcard.py from https://github.com/micropython/micropython-lib/blob/master/micropython/drivers/storage/sdcard/sdcard.py
# Assign chip select (CS) pin (and start it high)

# Intialize SPI peripheral (start with 1 MHz)
spi = machine.SPI(0,
                  baudrate=1000000,
                  polarity=0,
                  phase=0,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(2),
                  mosi=machine.Pin(3),
                  miso=machine.Pin(4))

# Initialize SD card
sd = sdcard.SDCard(spi, cs)

# Mount filesystem
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")

# Create a file and write something to it
with open("/sd/test01.csv", "w") as file:
    file.write("Hello, SD World!\t")
    file.write("This is a test\r\n")

# Open the file we just created and read from it
with open("/sd/test01.txt", "r") as file:
    data = file.read()
    print(data)
    Blink()
