clothes_item = ["T-Shirt","Sweater"]
key = ["c","r","u","d"]
ask = True
while ask:
    com = input("Welcome to our shop, what do you want (C, R, U, D)? ")
# read
    if com.lower() == key[1]:
        print("Our items: ", end="")
        print(*clothes_item, sep=", ")

# creat
    if com.lower() == key[0]:
        new_item = input("Enter new item: ")
        clothes_item.append(new_item)
        print("Our items: ", end="")
        print(*clothes_item, sep=", ")

# update
    if com.lower() == key[2]:
        update_pos = int(input("Update position? "))
        if update_pos > len(clothes_item):
            print("Invalid position.")
        else:
            update_item = input("Enter new item: ")
            clothes_item[update_pos-1] = update_item
            print("Our items: ", end="")
            print(*clothes_item, sep=", ")

# delete
    if com.lower() == key[3]:
        delete_pos = int(input("Delete position? "))
        if delete_pos > len(clothes_item):
            print("Invalid postion.")
        else:
            del clothes_item[delete_pos-1]
            print("Our items: ", end="")
            print(*clothes_item, sep=", ")

    if com.lower() not in key:
        print("Invalid request.")
        
    print()