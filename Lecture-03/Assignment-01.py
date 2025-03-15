#Assume you are given a positive integer variable named N . 
# Write a piece of Python code that prints hello world on separate lines, N times.
#  You can use either a while loop or a for loop.

# Write your code here

###################
###Solution
###Using for loop
#define variables
N = int(input("Input number: "))
i = 1
number = 1
#using for loop
for number in range (1, N+1):
    print("hello world")

