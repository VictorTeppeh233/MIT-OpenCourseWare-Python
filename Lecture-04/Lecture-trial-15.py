# EXAMPLE:  cube root
# finding perfect cube with negative numbers
cube = int(input("Enter an integer: "))

for guess in range (abs(cube)+1):
    if guess**3 == abs(cube):
        if cube < 0:
            guess = -guess
        print("Cube root of "+str(cube)+" is "+str(guess))