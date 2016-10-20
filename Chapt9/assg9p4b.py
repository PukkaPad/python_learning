# Chapter 9 - Dictionaries
# Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

counts = dict()
name_lst = list()
bigcount = None
bigname = None


fname = raw_input('Enter file name, please:')
fhand = open (fname)
for line in fhand:
	line = line.rstrip()

	if line.startswith('From:'):
		line = line.split() # it gives me a list of words
		find_email = line [1] # I get all the emails
		getname = find_email.split() # list of names
		name_email = getname[0] 
		name_lst.append(name_email)
#print name_lst
for name in name_lst:
	counts[name] = counts.get(name,0) + 1
#print counts
for name, count in counts.items():
	if bigcount is None or count > bigcount:
		bigname = name
		bigcount = count
print bigname, bigcount