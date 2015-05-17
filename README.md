# Lost Briefcase
Chicago Transit System Experiment

Version: Python 3.4.3 (Anaconda Package)

###Task 1
Travis doesn't know the number of the bus he was riding. Find likely candidates by parsing the data just downloaded and identifying vehicles traveling northbound of Dave's office.

Dave's office is located at:
Latitude: 41.980262
Longitude: -87.668452

### Task 2
Write a program that periodically mnonitors the identified buses and reports their current distance from Dave's office.

When the bus gets closer than 0.5 miles, have the program issue an alert by popping up a web-page showing the bus location on a map.

Travis will meet the bus and get his briefcase.

######To display a map: Google Static Maps
https://developers.google.com/maps/documentation/staticmaps/

######To show a page in a browser
```python
import webbrowser
webbrowser.open('http://...')
```


