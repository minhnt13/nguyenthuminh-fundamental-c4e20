sentence = input("Enter your words/sentences: ").lower()
string = sentence.replace(" ", "")
character = dict((letter,string.count(letter)) for letter in set(string))
for key, value in character.items():
    print(key," ", value)