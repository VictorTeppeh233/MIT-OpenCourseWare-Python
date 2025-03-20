###Word problem
#Alyssa, Ben, and Cindy are selling tickets to a fundraiser
# Ben sells 2 fewer than Alyssa
# Cindy sells twice as many as Alyssa
# 10 total tickets were sold by the three people
# How many did Alyssa sell?

#solution
for alyssa in range(11):
    for ben in range(11):
        for cindy in range(11):
            total = (alyssa + ben + cindy == 10)
            two_less = (ben == alyssa-2)
            twice = (cindy == 2*alyssa)
            if total and two_less and twice:
                print(f"Alyssa sold {alyssa} tickets")
                print(f"Ben sold {ben} tickets")
                print(f"Cindy sold {cindy} tickets") 