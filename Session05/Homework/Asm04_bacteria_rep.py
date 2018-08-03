initial_numb = int(input("How many B bacterias are there? "))
time = int(input("How much time in minutes will we wait? "))
exponent = time // 2
total_numb = initial_numb*2**exponent
print("After {} minutes, we would have {} bacterias".format(time, total_numb))
