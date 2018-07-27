print("This is a program to calculate factorial of a given number")
n = int(input("Enter a natural number: "))
fact=1
if n < 0:
    print("Can't calculate factorial of negative intergers")
else:
    for i in range(1,n+1,1):
        fact = fact*i
    print("!{} = {}".format(n,fact))