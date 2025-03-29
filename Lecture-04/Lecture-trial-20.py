###Convert to binary
###Only Positive numbers 
num = int(input("enter an integer: "))
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2
print (result)