numbers = [1, 6, 8, 1, 2, 1, 5, 6]
numb = int(input("Enter a number? "))
counter = 0
for item in numbers:
    if numb == item:
        counter +=1   

print("{} appears {} times in my list".format(numb, counter))