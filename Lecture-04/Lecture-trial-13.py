#################### YOU TRY IT ###################
# Hardcode a number as a secret number. Write a program that 
# checks through all the numbers between 1 to 10 and prints the 
# secret value. If it's not found, prints that it didn't find it. 
# solution

secret = 4
found = False
for i in range(1,11):
    if i == secret:
        print("yes, it's", i)
        found = True
if not found:
    print("not found")