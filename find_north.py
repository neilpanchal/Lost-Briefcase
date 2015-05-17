#find_north.py

# Find all buses that are traveling northbound of Dave's office

daves_latitude = 41.98062
daves_longitude = -87.668452

from xml.etree.ElementTree import parse
doc = parse('rt22.xml')

for bus in doc.findall('bus'):

    lat = float(bus.findtext('lat'))
    # Find all buses that are north of the office
    if lat > daves_latitude:
        direction = bus.findtext('d')

        # Only find buses that are actually traveling north
        # Ignore buses that are north of the office but traveling south
        if direction.startswith('North'):
            busid = bus.findtext('d')
            print(busid, lat)
