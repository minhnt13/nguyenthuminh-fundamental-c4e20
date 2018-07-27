# 1’s and 0’s, consecutively
for i in range(1,12,1):
    print(i % 2," ",end="")

print()

# Ask users to enter a number n, then print n 1’s and 0’s in total consecutively:
n = abs(int(input("Enter the total number of 1's and 0's: ")))
for j in range (1,n+1,1):
    print(j % 2," ", end="")