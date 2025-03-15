###########
## EXAMPLE: factorial using for loop
###########

##With for loops
factorial = 1
x = int(input("number :"))
for i in range(1, x+1, 1):
    factorial *= i
print(f'{x} factorial is {factorial}')