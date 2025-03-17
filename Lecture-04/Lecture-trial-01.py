# program to count the number of even integers in a range in a for loop

x = int(input("input range: "))
counter = 0
for i in range(x):
    # i is 0,1,2,3,4
    if i%2 == 0:
        counter += 1
print(counter)