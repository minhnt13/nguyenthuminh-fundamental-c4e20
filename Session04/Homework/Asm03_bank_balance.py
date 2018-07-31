loop = True
while loop:
    balance = input("Enter your balance: ")
    
    if balance.isdigit():
        balance = int(balance)
        print("Your updated balance: ${: ,}".format(balance))
        loop = False
    
    else:
        print("Invalid input. Please re-enter your balance.")

