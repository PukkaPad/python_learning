# Assignement Chapter 10
# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# Read file
#fhand = open ('mbox-short.txt')
fhand = open(raw_input('Enter file, please:'))
counts = dict()
hour_lst = list()

# Find 'From'
for line in fhand:
	line = line.rstrip()
	#print line

	# Find hour 
	if line.startswith('From'):
		line = line.split()
		#print len(line)
		if len(line) < 7:
			continue
		#print line
		HHMMSS = line [5]
		#print HHMMSS
		hours = HHMMSS[:2]
		#print hour 
		# Append hours to a list
		hour_lst.append(hours) 

# Create dictionary (key and value)
for hour in hour_lst:
	counts[hour]=counts.get(hour,0) + 1
#print counts

#print sorted ([(k,v) for k,v in counts.items()])

for k,v in sorted(counts.items()):
	print k,v

	





		

