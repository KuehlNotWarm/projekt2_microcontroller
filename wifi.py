# Stellt die Verbindung zum WLAN her
import network, time
def wifiConnect(ssid, password):
   
    sta_if = network.WLAN(network.STA_IF)
    print('Wait for connection')
    sta_if.active(True)
    sta_if.connect(ssid, password)
    while not sta_if.isconnected():
        print(".", end="")
        time.sleep_ms(500)
            
    print()
    print("Connected to ", ssid)
    print('IP address:', sta_if.ifconfig()[0])
