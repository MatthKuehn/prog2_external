from machine import Pin
import time

builtinLed = Pin(2, Pin.OUT)
ledD1=Pin(5,Pin.OUT)#D1

for ix in range(10):
    builtinLed.value(0)
    ledD1.on()
    print('loopy luiii')
    time.sleep(0.5)
    ledD1.off()
    builtinLed.value(1)
    time.sleep(0.3)