my_flock = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Minh and these are my sheep sizes")
print(my_flock)
print()

for months in range(1,4):
    print("MONTH {}".format(months))
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
    print("Now my biggest sheep has size {} let's shear it!".format(biggest))
    # after shearing
    grow_flock[spot] = 8
    print("After shearing, here is my flock")
    print(grow_flock)
    
    my_flock = grow_flock
    print()
