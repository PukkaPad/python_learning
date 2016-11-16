# Chapter 13 - Week 6 - Assignment
# Using the GeoJSON API

# -*- coding: utf-8 -*-

import json
import urllib
import string

# URL to be used
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

# looping
while True:
    location = raw_input ('Enter location: ')
    # I dont want to type each word capitalized...
    #location = string.capwords(location)
    # exit loop if nothing typed
    if len(location) < 1:
        break
    # calling the API
    url = serviceurl + urllib.urlencode({'sensor':'false', 'address':location})

    #print url

    print 'Retrieving ', url

    # accessing URL parameters

    data = urllib.urlopen(url).read()

    print 'Retrieved', len(data), 'characteres'

    try:
        js = json.loads(str(data))
    except:
        js = None

    # printing nicely to look for what I need to find
    print json.dumps(js, indent=4)

    get_placeID = js["results"][0]["place_id"]

    print 'Place id ', get_placeID    


''' Welcome Mariana de Souza e Silva from Using Python to Access Web Data

Calling a JSON API

In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

http://python-data.dr-chuck.net/geojson
This API uses the same parameters (sensor and address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get a list of all of the address values which can be used with this API.
To call the API, you need to provide a sensor=false parameter and the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.urlencode() fuction as shown in http://www.pythonlearn.com/code/geojson.py

Test Data / Sample Execution

You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJJ8oO7_B_bIcR2AlhC8nKlok".

$ python solution.py
Enter location: South Federal University 
Retrieving http://...
Retrieved 2101 characters
Place id ChIJJ8oO7_B_bIcR2AlhC8nKlok 
Turn In

Please run your program to find the place_id for this location:

University of Twente
Make sure to enter the name and case exactly as above and enter the place_id and your Python code below. Hint: The first seven characters of the place_id are "ChIJPZ9 ..."
Make sure to retreive the data from the URL specified above and not the normal Google API. Your program should work with the Google API - but the place_id may not match for this assignment.'''