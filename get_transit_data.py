# get_transit_data.py

# Fetch Route 22 data from the CTA Transit API and save the raw data as rt22.xml

import urllib.request
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()
f = open('rt22.xml', 'wb')
f.write(data)
f.close()


