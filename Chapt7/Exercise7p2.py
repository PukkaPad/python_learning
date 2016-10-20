# 7.11
# Exercise 7.2

"""
Write a program to prompt for a file name, and then read through
the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with 'X-DSPAM-Confidence:' pull apart
the line to extract the floating-point number on the line. Count these lines and
then compute the total of the spam confidence values from these lines. When you
reach the end of the file, print out the average spam confidence.
Enter the file name: mbox.txt
Average spam confidence: 0.894128046745
Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519
Test your file on the mbox.txt and mbox-short.txt files.
"""

import sys, re, math
#I will try do use regex

line_list =[]

while True:
    try:
        fname = raw_input ('Enter file name: ')
        fhand = open(fname)
        break
    except IOError:
        print '%s does not exist.' % fname
        continue
    except KeyboardInterrupt:
        print 'CTRL+C! \nBye'
        sys.exit()

for line in fhand:
    line = line.rstrip() 
    #print line
    # I am looking for lines that start with (^) X-, followed by one character(.) or more(+) characteres, followed by the string Confidence
    #if re.search('^X.+Confidence', line):
        #print line
        #line_list.append(line)
#print line_list

    #or I can use findall to extract the string
    # I am looking for lines that start with (^) X- followed zero or more characters (.*), folowed by semicolon (:) and whitespace. I will extract ([]) one or more characteres that are a digit or a period [0-9.]+
    line = re.findall('^X-.*Confidence: ([0-9.]+)', line)
    if len(line) > 0: # whithout this if we print empty ones
        #line_list.append(line)
        # each output looks like [['number], ['number], etc]. I dont want square brackets
        #solution:
        line_list.append(line[0]) # index; I only get the string
        line_result = [float(i) for i in line_list]
sum_line = sum(line_result)
index_num = len(line_result) 
#print line_result
#print index_num
average = sum_line/index_num
print 'Average spam confidence: ', average



    

