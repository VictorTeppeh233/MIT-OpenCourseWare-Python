# Practice 1: 
# Declare a variable x that stores an int > 0. Print all ints, one on each
# line, between 1 (inclusive) and x (inclusive) that are divisible by 5.
# For ex. if x = 15, it prints 5, 10, and 15. 
# For ex. if x = 14, it prints 5 and 10.

#Solution using while loop
#prompt user for number
x = int(input("Enter the number: "))
#use while loop to ensure that the value is greater than 0
while x <= 0:
    x = int(input("Enter a valid number: "))
#implementing while loop
multiple = 1
while multiple <= x:
    if multiple % 5 == 0:
        print(multiple)
    multiple = multiple+1
print('the end')