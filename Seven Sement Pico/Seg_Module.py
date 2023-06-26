import machine

D=[
    [1,1,1,1,1,1,0],#Digit 0
    [0,1,1,0,0,0,0],#Digit 1
    [1,1,0,1,1,0,1],#Digit 2
    [1,1,1,1,0,0,1],#Digit 3
    [0,1,1,0,0,1,1],#Digit 4
    [1,0,1,1,0,1,1],#Digit 5
    [1,0,1,1,1,1,1],#Digit 6
    [1,1,1,0,0,0,0],#Digit 7
    [1,1,1,1,1,1,1],#Digit 8
    [1,1,1,1,0,1,1],#Digit 9
   ]


class Seven_Segment:
    def __init__ (self,a,b,c,d,e,f,g):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
        self.g=g
        self.Pin1=machine.Pin(self.a,machine.Pin.OUT)
        self.Pin2=machine.Pin(self.b,machine.Pin.OUT)
        self.Pin3=machine.Pin(self.c,machine.Pin.OUT)
        self.Pin4=machine.Pin(self.d,machine.Pin.OUT)
        self.Pin5=machine.Pin(self.e,machine.Pin.OUT)
        self.Pin6=machine.Pin(self.f,machine.Pin.OUT)
        self.Pin7=machine.Pin(self.g,machine.Pin.OUT)
    def Display(self,num):
            self.Pin1.value(D[num-1][0])
            self.Pin2.value(D[num-1][1])
            self.Pin3.value(D[num-1][2])
            self.Pin4.value(D[num-1][3])
            self.Pin5.value(D[num-1][4])
            self.Pin6.value(D[num-1][5])
            self.Pin7.value(D[num-1][6])