# Week 5 - Chapter 13

import urllib
import xml.etree.ElementTree as ET

# request data:

serviceurl = raw_input ('Enter xml data, please: ')

print 'Retrieving ', serviceurl

# reads the data using urllib 
read_data = urllib.urlopen(serviceurl).read()
print 'Retrieved', len(read_data), 'characters'

# parsing the string to get the tree
tree = ET.fromstring(read_data)
# print tree


# find the tag comment. I am using a XPath selector string which will look through the entire tree of XML for any tag named comment.
# findall retrieves a list of subtrees
find_comment = tree.findall('.//comment')
# find the tag count. and get how many of it we have
find_count = tree.findall('.//count')
print 'Count: ', len(find_count) # here I know the number of times the tag count appears


# loop through all the count and sum the values
# findall retrieves a list of subtrees
count = 0
number_list = []

for item in find_comment:
    #print 'Count', item.find("count").text
    
    number_list.append(item.find('count').text)
    
    #print number_list

    # using a list of comprehension to convert str to int:
    number_list = [int(i) for i in number_list]
print 'Sum: ', sum(number_list)


# # or :)

# for i in number_list:
#     count = count + i
# print 'Count other way', count


