from machine import Pin, PWM
import utime,time
#Set the pin for PWM OUTPUT 
led = PWM(Pin(2))
led.freq(10)      # Set the frequency value to 10Hz
led.duty_u16(int(20000))     # Set the duty cycle, between 0-65535
if __name__ == '__main__':
    while True:
        time.sleep(1);
