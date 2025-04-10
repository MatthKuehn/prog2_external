from machine import Pin
from time import sleep

ledD1=Pin(5,Pin.OUT)#D1
buttonIntResistance = Pin(12, Pin.IN,Pin.PULL_UP)#D6 12
while True:
    if buttonIntResistance.value() == 0:     # if button pressed
      print('button1 gedrückt')
      ledD1.value(1)             # led will turn ON
    if buttonIntResistance.value() == 1:                        # if push_button not pressed
      print('button1 nicht gedrückt')
      ledD1.value(0)             # led will turn OFF
    print('---')
    sleep(2)
    