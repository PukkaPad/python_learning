# Chapter 13 - Week 6 - Assignment
# Extracting Data from JSON

# -*- coding: utf-8 -*-

import json
import urllib

while True:
    # Ask for URL
    #url = 'http://python-data.dr-chuck.net/comments_42.json'
    #url = 'http://python-data.dr-chuck.net/comments_285382.json'

    url = raw_input('Enter URL, please: ')
    if len(url) < 1:
        break
    print 'Retrieving', url

    # Read Data
    html = urllib.urlopen(url).read()

    print 'Retrieving ', len (html), 'characteres'

    js = json.loads(str(html))

    #print len(js)

    #print json.dumps(js, indent=4)
    #print js['comments'][0]['count']
    #print js['comments'][1]['count']

    js_loop = js['comments']

    #print js_loop

    sum_count = []
    count = 0

    # Looping
    for i in js_loop:
        count += 1
        #print count
        #print js_loop[count-1]['count']
        sum_count.append(js_loop[count-1]['count'])
    print 'Count: ', count
    print 'Sum: ', sum(sum_count)


'''Welcome Mariana de Souza e Silva from Using Python to Access Web Data

Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://python-data.dr-chuck.net/comments_285382.json (Sum ends with 26)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
Data Format
The data consists of a number of names and comment counts in JSON as follows:

{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}
The closest sample code that shows how to parse JSON and extract a list is json2.py. You might also want to look at geoxml.py to see how to prompt for a URL and retrieve data from a URL.

Sample Execution

$ python solution.py 
Enter location: http://python-data.dr-chuck.net/comments_42.json
Retrieving http://python-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2... '''