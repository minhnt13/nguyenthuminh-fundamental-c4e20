name = input("Your full name: ").lower()

words = name.split()
string_name = " ".join(words)

print("Updated:",string_name.title())