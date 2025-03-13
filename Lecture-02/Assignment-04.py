############## YOU TRY IT ###############
# Write a program that:
# * Saves a secret number. 
# * Asks the user for a number guess.
# * Prints whether the guess is too low, too high, or the same as the secret. 

# your code here


secret_number = 50
guess = int(input("Please type your number guess: "))
if (guess > secret_number):
    print("too high")
elif (guess < secret_number):
    print("too low")
else:
    print("same")