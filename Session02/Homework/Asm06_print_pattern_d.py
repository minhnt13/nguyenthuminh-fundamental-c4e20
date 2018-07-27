# 10 x 10 1’s and 0’s, consecutively
# for j in range (0,10,1):
#     if j % 2 == 0:
#         for i in range(1,11,1):
#             print(i % 2," ",end="")
#     else:
#         for i in range(2,12,1):
#             print(i % 2," ",end="")
#     print()
for j in range (2,12,1):
    for i in range(1,11,1):
        print(abs(((j - i) % 2))," ",end="")
    print()
print ()
<<<<<<< HEAD
#Ask users to enter a number n, then print n x n 1’s and 0’s, consecutivelyn = int(input("Enter a number: "))
=======
# Ask users to enter a number n, then print n x n 1’s and 0’s, consecutively
>>>>>>> 696ff48b06d3ba2ae8b4efb33930d939bfed994b
n = int(input("Enter a number: "))
for y in range (2,n+2):
    for k in range (1,n+1):
        print(abs((y - k) % 2)," ",end="")
    print()
