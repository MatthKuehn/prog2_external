# read temperature sensors
# take care, the sensors need a 4.7 kOhm resistor!
# although the drawing suggests 5V, 3.3V also works
from machine import Pin
import time
from onewire import OneWire
#OneWire is a serial communication protocol that allows data exchange between a master (=ESP32 or 8266) and one or more slave 
#devices using just one data wire (plus ground) --> concatenate multiple sensors
from ds18x20 import DS18X20 # the package for this specific temperature sensor
import onewire, ds18x20

# The temp sensor is connected at Pin17 (D8)
tempSensorPin = Pin(17)

# calling the sensor without the import of DS18X20 (only ds18x20 as generic package)
# these 3 lines of code are not necessary for the loop below and only show an alternative way of calling the sensor
ds_sensor = ds18x20.DS18X20(onewire.OneWire(tempSensorPin))
roms = ds_sensor.scan()
print('Found DS devices: ', roms)

# Create OneWire instance -> wiring now knows which pin to connect to
dq_ow = OneWire(tempSensorPin)

# Create DS18x20 instance -> now the esp knows, that behind the wiring we have an instance of DS18X20, e.g. a temp sensor
ds = DS18X20(dq_ow)
# this script was designed for esp32, not esp8266, adapt pin!
internalLed = Pin(48, Pin.OUT)  # GPIO2
led2=Pin(1, Pin.OUT) 

# Scan the ds18b20 devices on the single bus and return a list of device addresses (--> if there are multiple connected)
ds_addresses = ds.scan() 

for idx in range(5):
    #Obtain temperature sampling for convert temperature unit conversion.
    ds.convert_temp()
    internalLed.on()
    led2.on()# Turn LED on  
    time.sleep(1)
    
    print('in loop: ',idx)
    for ds_address in ds_addresses:
        # Print temperature of all devices
        print('Die Temperatur am Sensor '+str(bytes(ds_address)) + ' beträgt: ' + str(ds.read_temp(ds_address))+' °C')
    internalLed.off()
    led2.off()# Turn LED off
    time.sleep(1)

led2.on()
internalLed.off()
print('end of file')