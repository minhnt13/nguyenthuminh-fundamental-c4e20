# i. 20 number starting from 0
for i in range (0,20,1):
    print(i," ",end="")

print()

# Ask users to enter a number, then print n positive numbers from 0 to n-1:     
n = abs(int(input("Enter a number: ")))
for j in range (0,n,1):
    print(j," ",end="")