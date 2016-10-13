# Chapter 11

import re

# load file:
fhand = open ('regex_sum_285376.txt')

no_space = fhand.read()

# creat empty list
list_num = list()

# get the numbers
find_num = re.findall('([0-9]+)', no_space)

#print find_num[0]
#y = find_num[0] + find_num[1]
#print y

# convert number to integer
for charact in find_num:
	list_num.append(int(charact))
print list_num

summ = 0
count = 0

for value in list_num:
	count = count + 1
	summ = summ + value
#print count
print summ