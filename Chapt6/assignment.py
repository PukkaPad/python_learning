# Assignement 6.5 - Chapter 6
""" Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out
"""

text = "X-DSPAM-Confidence:    0.8475";

getspace = text.find(' ')
#print getspace

getnumber = text[getspace+1:]

float_number = float(getnumber)

print float_number