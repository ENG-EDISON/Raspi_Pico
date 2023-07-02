import serial
from serial.tools import list_ports
import time

def print_ports_info():
    for port in list_ports.comports():
        print("Device :",port.device)
        try:
            print("Vid:",hex(port.vid),"pid:",hex(port.pid))
        except:
          print("Vid:",port.vid,"pid:",port.pid)
        print("Serial Number:",port.serial_number)
        print("Name: ",port.name)
        print("hiw: ",port.hwid)
        print("Description: ",port.description)
        print("Interface:",port.interface)
        print("Location:",port.location)
        print("Manufacturer: ",port.manufacturer)
        print("Product Id: ",port.product)

def scan_for_picos(verbose=False):
    picos=[]
    for port in list_ports.comports():
        if verbose:
            print("Checking",port.device)
        if port.manufacturer !=None:
            if "Silicon Labs" in port.manufacturer:
                picos.append(port.device)
            return picos
picos=scan_for_picos()
pico1=print_ports_info()
print("Picos Found:")
for pico in picos:
    print(pico)
s=serial.Serial(pico,baudrate=115200)
Query=[b't',b's']
while True:
    try:
        s.open()
    except:
        for i in Query:
            Res=[]
            s.write(i)
            k=s.read_until(b'-')
            k=k.decode('utf-8')
            if "t" in  k:
                print(k[:-2])
            if "s" in k:
                print(k[:-2])
        time.sleep(1)
