#Assume you are given a variable named number (has a numerical value). 
# Write a piece of Python code that
# prints out one of the following strings:
# positive if the variable number is positive
# negative if the variable number is negative
# zero if the variable number is equal to zero

#Solution
number = int(input("number = : "))

#conditional statements to determine if it's positive, negative or equal to zero.
if (number > 0):
    print("positive")
elif (number == 0):
    print("zero")
else :
    print("negative")