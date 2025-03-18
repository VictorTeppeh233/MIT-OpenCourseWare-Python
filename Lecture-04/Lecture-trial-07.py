# EXAMPLE: guessing perfect square roots
# Given an int, call it x, want to see if there is another int which is its square root
# Start with a guess and check if it is the right answer.
# To be systematic, start with guess = 0, then 1, then 2, etc.

# Solution
guess = 0
x = int(input("Enter an integer: "))
while guess**2 < x:
    guess = guess + 1
if guess**2 == x:
    print("Square root of" , x, "is", guess)
else:
    print(x, "is not a perfect square")