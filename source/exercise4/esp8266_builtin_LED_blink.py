# access internal LED and let it blink
#
from machine import Pin
import time
#2 = internal blue LED esp8266
blueLed = Pin(2, Pin.OUT)

while True:
    blueLed.value(0)
    # or: blueLed.on()
    print('loopy')
    time.sleep(0.5) # no activity for half a second
    blueLed.value(1)
    # or: blueLed.off()
    time.sleep(0.5) # no activity for half a second