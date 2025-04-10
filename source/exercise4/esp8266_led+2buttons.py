# 2 leds activated by 2 buttons
from machine import Pin
from time import sleep

ledD1=Pin(5,Pin.OUT)#D1
ledD2=Pin(4,Pin.OUT)#D2

#push_buttonExtResistance = Pin(12, Pin.IN)  # 23 number pin is input
buttonIntResistance = Pin(12, Pin.IN,Pin.PULL_UP)#D6 12
buttonExtResistance= Pin(14, Pin.IN)#D5 14 # Pull_down
while True:
    if buttonIntResistance.value() == 0:     # if button pressed
      print('button1 gedrückt')
      ledD1.value(1)             # led will turn ON
    if buttonIntResistance.value() == 1:                        # if push_button not pressed
      print('button1 nicht gedrückt')
      ledD1.value(0)             # led will turn OFF
    if buttonExtResistance.value() == 1:                        # if push_button not pressed
      print('button2 nicht gedrückt')
      ledD2.value(0)             # led OFF
    if buttonExtResistance.value() == 0:                        # if push_button not pressed
      print('button2 gedrückt')
      ledD2.value(1)             # led will turn OFF

    print('---')
    sleep(2)