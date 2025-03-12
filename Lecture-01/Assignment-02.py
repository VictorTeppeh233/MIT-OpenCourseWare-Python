#Swap values of x and y without binding the numbers directly.
#Debut this code.

x = 1
y = 2

# Code
# x = y
# y = x

# Solution
# create a third variable called z then assign it to either x or y.
z = x
# z = 1

# x gets y's value which is 2
x = y

# y gets x value which is one, but from z
y = z

print("x = : ", x)
print("y = : ", y)