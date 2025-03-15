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
#using while loop
while i <= N:
    print("hello world")
    number = number+i
    i = i+1
print("the end")