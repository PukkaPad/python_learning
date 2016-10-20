# 7.11 Exercises
# Exercise 7.1

"""Write a program to read through a file and print the contents of the
file (line by line) all in upper case. Executing the program will look as follows:
python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
SAT, 05 JAN 2008 09:14:16 -0500
You can download the file from www.py4inf.com/code/mbox-short.txt
"""
import sys

def ex7p1():
    while True:
        
        try:
            fname = raw_input ('Enter file name: ')
            fhand = open(fname)
            break
            #print fname
            
   
        except IOError:
            print '%s does not exit!' % fname
            continue
         
        # CTRL+C with raw_input was not working. So I had to add this other except function so I can force quit if necessary
        except KeyboardInterrupt :
            print 'CTRL+C!!! \nBye'
            sys.exit() # this atops the program
    
    for line in fhand:
        line = line.strip(' \n\t').upper() # strip line of whitespaces, newlines and tabs
        print line
        
    
    
if __name__ == '__main__':
    ex7p1()            