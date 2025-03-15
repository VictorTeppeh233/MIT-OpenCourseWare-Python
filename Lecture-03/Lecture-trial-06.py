###########
## EXAMPLE: factorial
###########

#variable for the factorial
x = int(input("factorial of: "))
#loop variable,
i = 1
#factorial
factorial = 1
#while loop
while i <= x:
#function for factorial
    factorial = factorial*i
#increment procedure
    i = i+1
#print function when loop ends
print(f"{x} factorial is {factorial}")

