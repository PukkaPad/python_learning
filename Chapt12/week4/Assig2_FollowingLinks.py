# assignment: Following Links in Python

import urllib
from BeautifulSoup import *


# URL imput from user only happens once

url = raw_input('Enter - ')


# Ask for number of times process will be repeated
repetitions = range(int(raw_input('Enter count:' )))
# Ask for position
position_url = int (raw_input ('Enter position:' ))


# loop as many times as repetitions
for repetition in repetitions:
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	# define what tag I want
	tags = soup('a')


# create a list so I can get the url by position
# i repopulate it every time
	url_list = list()
	for tag in tags:
		# get the href attribute
		url = tag.get('href', None)
		#print url
		# append all the links
		url_list.append(url)
		#url = url_new
#print url_list
	url_new = url_list[position_url-1]
	print 'Retrieving:', url_new
	url = url_new

