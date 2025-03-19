# EXAMPLE:  cube root

# finding a perfect cube root of positive numbers
cube = int(input("Enter an integer: "))

for guess in range(cube+1):
    if guess**3 == cube:
        print("cube root of", cube, "is", guess)
