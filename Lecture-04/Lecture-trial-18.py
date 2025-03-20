###Word problem
#Alyssa, Ben, and Cindy are selling tickets to a fundraiser
# Ben sells 2 fewer than Alyssa
# Cindy sells twice as many as Alyssa
# 10 total tickets were sold by the three people
# How many did Alyssa sell?

#solution

for alyssa in range(1001):
    ben = max(alyssa-20,0)
    cindy = alyssa*2
    if ben + cindy + alyssa == 1000:
        print(f'Alyssa sold {alyssa} tickets')
        print(f'Ben sold {ben} tickets')
        print(f'Cindy sold {cindy} tickets')