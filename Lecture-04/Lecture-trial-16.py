# EXAMPLE:  cube root
#Guess and check cube root
#Optimised to be a little faster

#solution

cube = int(input("Enter an integer: "))
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube) :
        break
if guess**3 != abs(cube):
    print(cube, "is not a perfect cube")
else:
    if cube < 0:
        guess = -guess
    print("Cube root of "+str(cube)+" is "+str(guess))