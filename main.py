from machine import Pin,PWM,UART
import utime

uart = UART(1,9600)

led = Pin(25,Pin.OUT)


in1 = Pin(10,Pin.OUT)
in2 = Pin(11,Pin.OUT)
enA = Pin(15,Pin.OUT)


in3 = Pin(12,Pin.OUT)
in4 = Pin(13,Pin.OUT)
enB = Pin(14,Pin.OUT)


enA.high()
enB.high()


def right():
    in1.high()
    in2.low()
    in3.high()
    in4.low()
def left():
    in1.low()
    in2.high()
    in3.low()
    in4.high()
def stop():
    in1.low()
    in2.low()
    in3.low()
    in4.low()
def forward():
    in1.high()
    in2.low()
    in3.low()
    in4.high()
def backward():
    in1.low()
    in2.high()
    in3.high()
    in4.low()

    
while True:
   led.value(1)
   if uart.any(): #Checking if data available
        data=uart.read() #Getting data
        data=str(data) #Converting bytes to str type
        print(data)
        
        if('Forward_ON' in data):
            forward()
        else if('Backward_ON' in data):
            backward()
        else if('Left_ON' in data):
            left()
        else if('Right_ON' in data):
            right()
        else if('Stop' in data):
            stop()
        else:
            stop()
            
        