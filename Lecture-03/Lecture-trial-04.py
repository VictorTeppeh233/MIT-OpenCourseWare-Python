############### YOU TRY IT ################
# Expand this code to show a sad face when the user entered 
# the while loop more than 2 times. Hint: use a counter
###################

#start with declaring a variable outsite the loop function and assigning it a value of 0
n = 0
#create a variable to take input
where = input("Go left or right? ")
#start the while loop 
while where == "right":
    n = n + 1
    if n > 2:
        print(":(")
    where = input("Still Go left or right? ")
#this is executed when you exit the while loop
print("You got out!")
