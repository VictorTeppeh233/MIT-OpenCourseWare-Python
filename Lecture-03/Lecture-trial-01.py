#where is used as a variable to store the answer for direction
where = input("You are in the Lost Forest. Go left or right? ")
#while loop checkes for the direction and if yes repeats the code block.
while where == "right":
    where = input("You are still in the Lost Forest. Go left or right? ")	
print("You got out of the Lost Forest!") 