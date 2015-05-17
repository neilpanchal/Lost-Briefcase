# monitor.py

import urllib.request
import time


from xml.etree.ElementTree import parse
candidates = ['4389', '4379']
daves_latitude = 41.980262

def distance(lat1, lat2):
    return 69*abs(lat1-lat2)

def monitor():
    u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
    doc = parse(u)
    for bus in doc.findall('bus'):
        busid = bus.findtext('id')
        if busid in candidates:
            lat = float(bus.findtext('lat'))
            dist = distance(lat, daves_latitude)
            print(busid, dist, 'miles')
    print('-'*30)


while True:
    monitor()
    time.sleep(5)
