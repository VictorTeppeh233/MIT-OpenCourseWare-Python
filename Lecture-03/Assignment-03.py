# Practice 1: 
# Declare a variable x that stores an int > 0. Print all ints, one on each
# line, between 1 (inclusive) and x (inclusive) that are divisible by 5.
# For ex. if x = 15, it prints 5, 10, and 15. 
# For ex. if x = 14, it prints 5 and 10.

#Solution using for loop
#prompt user for number
x = int(input("Enter the number: "))
#use while loop to ensure that the value is greater than 0
while x <= 0:
    x = int(input("Enter a valid number: "))
#implementing for loop
multiple = 1
for multiple in range(1, x+1):
    if multiple%5 == 0:
        print(multiple)
print('the end')