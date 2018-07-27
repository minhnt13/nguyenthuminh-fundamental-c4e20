# 9 x 9 numbers (multiplication table)
for i in range (1,10,1):
    print(i," ",end="")
    for j in range (2,10,1):
       print("{:3d}".format(i * j),end="")
    print()

print()


# Ask user to enter a number n, then print n x n numbers, following multiplication table pattern:
n = int(input("Enter a number: "))
for y in range (1,n+1):
    print(y," ", end="")
    for k in range (2,n+1):
        print("{:4d}".format(y*k),end="")
    print()
