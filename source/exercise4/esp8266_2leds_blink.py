# needs breadboard with 2 leds -> long one!
print('Hello, MicroPython!')

from machine import Pin
import time

orange = Pin(2, Pin.OUT)
ledD1=Pin(5,Pin.OUT)#D1
ledD2=Pin(4,Pin.OUT)#D2

eigeneLED=Pin(5,Pin.OUT)#D1
#eigeneLED=Pin(4,Pin.OUT)#D2

for ix in range(10):
    orange.value(0)
    ledD1.value(1)
    ledD2.on()
    print('loopy')
    time.sleep(0.5)
    ledD1.off()
    ledD2.off()
    orange.value(1)
    time.sleep(0.3)