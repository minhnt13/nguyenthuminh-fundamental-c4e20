my_flock = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Minh and these are my sheep sizes")
print(my_flock)
print()
# find biggest sheep
biggest = 0
spot = 0
for pos, sheep_size in enumerate(my_flock):
    if sheep_size > biggest:
         biggest = sheep_size
         spot = pos
print("Now my biggest sheep has size {} let's shear it!".format(biggest))
# 2.3 shearing the biggest
my_flock[spot] = 8
print("After shearing, here is my flock")
print(my_flock)
print()

for months in range(1,4):
    print("MONTH {}:".format(months))
    grow_flock = [sheep+50 for sheep in my_flock]
    print("One month hass passed, now here is my flock")
    print(grow_flock)
    # find biggest sheep
    biggest = 0
    spot = 0
    for pos, sheep_size in enumerate(grow_flock):
        if sheep_size > biggest:
            biggest = sheep_size
            spot = pos
    # shear the biggest
    if months < 3:
        print("Now my biggest sheep has size {} let's shear it!".format(biggest))
        grow_flock[spot] = 8
        print("After shearing, here is my flock")
        print(grow_flock)
    else:
        print()
        total = 0
        for sheep_size in grow_flock:
            total = total + sheep_size
        print("My flock's size in total: {}".format(total))
        print("I would get {} * 2$ = {}".format(total,total*2))
    my_flock = grow_flock
    print()
# total size
