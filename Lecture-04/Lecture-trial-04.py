# search through a string.
s = "demo loops - fruit loops"
# for loop to print when letters "i" or "u" are found
for char in s:
    if char in "iu":
        print("There is an i or u")