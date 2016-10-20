# Assignement 7.2
""" Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
"""

fname = raw_input ('Enter file name, please: ')

try:
	fhand = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()
search_string = 'X-DSPAM-Confidence: '
count = 0
adding = 0

for line in fhand:
	line = line.rstrip()
	if not search_string in line:
		continue
	count =count + 1
	# print line
	# print count
	get_space = line.find (' ')
	get_num = line[get_space+1:]
	float_num = float(get_num)
	adding = adding + float_num
	# print adding
	# print count

avg = adding / count
print "Average spam confidence:", avg
