# search through a string.
s = "demo loops - fruit loops"
# for loop to print when letters "i" or "u" are found
for index in range(len(s)):
    if s[index] == "i" or s[index] == "u":
        print("There is an i our u")