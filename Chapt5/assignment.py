# Assignment  - Chapter 5  
"""Write a program that repeatedly prompts a user for
integer numbers until the user enters 'done'. Once 'done' is entered, print
out the largest and smallest of the numbers. If the user enters anything
other than a valid number catch it with a try/except and put out an
appropriate message and ignore the number. Enter the numbers from the book
for problem 5.1 and Match the desired output as shown.''
"""
largest = None
smallest = None

while True:
	

	try:
		enter_input = raw_input('Enter a number. When you are done, enter "done": ')
		
		if enter_input == 'done':
 			break
 		
 		else: 
 		# it sees everything I type as an integer
			values_input = int(enter_input)

			if values_input > largest:
				largest = values_input

		
			if smallest is None:
				smallest = values_input

			elif values_input < smallest:
				smallest = values_input

 	except (ValueError):
 			print 'Invalid input'
	

print 'Maximum', largest 
print'Minumum', smallest


	
