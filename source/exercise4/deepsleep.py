from machine import Pin, deepsleep

# GPIO0 als Weckpin konfigurieren
wake_pin = Pin(0, Pin.IN)

# Deep Sleep für 10 Sekunden
deepsleep(10000)

# Wenn der ESP wieder aufwacht, weitermachen
print("woken up!")