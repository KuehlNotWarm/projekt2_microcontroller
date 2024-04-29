from wifi import wifiConnect
from bmp180 import BMP180
from mqtt import MQTTClient
from machine import I2C, Pin 
import time, json

# Bus init und aktueller Luftdruck
i2c = I2C(scl=Pin(5), sda=Pin(4))
bmp = BMP180(i2c, 102100.0) #aktueller Luftdruck in Pascal

# Zugangsdaten WLAN
ssid = "iotWifi"
password = "piuserwifi"

# MQTT Broker
server = "broker.hivemq.com"
topic = b'projekt/gruppe1/sensordaten'

#MQTT Client erzeugen
client = MQTTClient(server, keepalive=60)

#Verbindungsaufbau WIFI und MQTT Broker
try:
  wifiConnect(ssid, password)
  client.mqttConnect()
except OSError as e:
  print('Failed to connect to Local Network or MQTT broker.')
  print('Reconnecting...')
  time.sleep(10)
  machine.reset()
  
while True:      
  #Messwerte auslesen und speichern
  messwerte={
    "pressure": bmp.pressure/100.0,
    "temperature": bmp.temperature,
    "height": bmp.altitude
  }
  
  #MQTT versenden 
  print(messwerte)
  client.mqttPublish(topic, json.dumps(messwerte));
 
  time.sleep(5)