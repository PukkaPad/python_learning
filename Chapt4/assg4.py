# Chapter 4
""" Write a program to prompt the user for hours and rate per hour usingraw_input to compute gross pay. Award time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use raw_input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.
"""

def computepay(hours,rate):
    
    if hours > normal_hours:
        pay  = normal_hours * rate + (hours - normal_hours) * 1.5 * rate
        #print "Computing hours bigger than 40h"
        
    else:
        pay = hours * rate
        
    return pay
    	
normal_hours = 40
hours = float(raw_input("Please enter Hours:"))
rate = float(raw_input("Please enter rate:"))

results = computepay(hours,rate)
print results