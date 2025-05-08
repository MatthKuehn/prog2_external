# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 17:44:48 2025

@author: kuehnbam
"""
import paho.mqtt.client as mqtt
import json
from datetime import datetime
import pandas as pd
import time
import matplotlib.pyplot as plt
import sqlalchemy 
# MQTT Broker Details
mqtt_server = '172.20.10.13'  # IP des Brokers
mqtt_port = 1883  # Standardport für MQTT
topic = 'temperatur_vong_esp'

conn=sqlalchemy.create_engine("mysql+pymysql://root:^)FL|!k.!;t]prB2@localhost:3306/prog2")
dtAll=pd.DataFrame(columns=['zeit','temp','ort'])
stop_flag = False
counter=0

# Callback-Funktion für den Empfang von Nachrichten
def on_message(client, userdata, msg):
    global dtAll # greift auf die oben generierte Variable zu
    global stop_flag
    global conn
    global counter

    print(f'Nachricht bzgl. {msg.topic} kam rein')
    counter=counter+1
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        # Versuch, die empfangene Nachricht als JSON zu parsen
        data = json.loads(msg.payload)
        #print('Daten als Python Dictionary:', data)
        
        # Weiterverarbeitung der Daten
        
        if 'temperature' in data:
            temperature = data['temp']
            ort=data['ort']
            tempDict={'zeit':timestamp,'temp':temperature,'ort':ort}
            tempDF=pd.DataFrame([tempDict])
            #print(tempDF)
            
            tempDF.to_sql('temperatur_kempten', con=conn, if_exists='append', index=False)
            print(counter,' - sent to sql db at ',tempDict['zeit'])
            
            #print(f'Temperatur: {temperature}°C')
		# in dtALL würden die Daten für das Plotten weiter unten gespeichert
		# auskommentiert, da sonst RAM volllaufen würde. kann getestet werden, plot sollte funktionieren
            #dtAll=pd.concat([dtAll,tempDF],ignore_index=True)
            #print(dtAll)
            
        if data.get('stop', False):  # Angenommen, das JSON enthält ein 'stop'-Feld und dieses ist False, wird die Kommunikation gestoppt und es wird weiter unten geplottet
            stop_flag = True
            
    except json.JSONDecodeError:
        print('Error parsing from JSON')
    return

# MQTT Client erstellen
client = mqtt.Client()
# Callback-Funktionen setzen
client.on_connect = lambda client, userdata, flags, rc: client.subscribe(topic)
client.on_message = on_message
# Verbinde mit dem MQTT Broker
client.connect(mqtt_server, mqtt_port, 60)
# Endlosschleife starten, um Nachrichten zu empfangen
client.loop_start()
while not stop_flag:
    time.sleep(1)
client.loop_stop()  # Stoppe den Client-Loop, um das Abonnieren zu beenden
print("Empfangenes 'stop'-Signal vom esp. Stoppe das Abonnieren...")
    

# Sobald das Stoppsignal empfangen wird, wird der Subscriber gestoppt
print("Abo gestoppt. skript weiter ausführen")
print(dtAll.head())
dtAll.plot(y='temp',x='zeit',kind='bar')
plt.ylim(21,26)
plt.show()

#engine=sqlalchemy.create_engine("mysql+pymysql://root:^)FL|!k.!;t]prB2@localhost:3306/prog2")
#dtAll.to_sql('temperatur_kempten', con=engine, if_exists='replace', index=False)
