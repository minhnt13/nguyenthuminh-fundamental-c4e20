inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# adđ a key and set value
inventory["pocket"]= ["seashell", "strange berry", "lint"]
# remove
del inventory["backpack"][1]
# add 50 to gold
inventory["gold"] += 50

