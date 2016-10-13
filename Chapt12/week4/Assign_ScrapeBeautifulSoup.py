# Assignment Scraping Numbers from HTML using BeautifulSoup
import urllib
from BeautifulSoup import *

# name of the URL?
url = raw_input('Enter - ')
# string
html = urllib.urlopen(url).read()

# parse the HTML data
soup = BeautifulSoup(html)

# Retrieve the span tag
tags = soup('span')
count = 0
for tag in tags:
    number = int(tag.contents[0])
    #print number
    count = count + number
print count






