# 2.1 my flock
my_flock = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Minh and these are my sheep sizes")
print(my_flock)
print()

# 2.2 find biggest sheep
biggest = 0
spot = 0
for pos, sheep_size in enumerate(my_flock):
    if sheep_size > biggest:
         biggest = sheep_size
         spot = pos
print("Now my biggest sheep has size {} let's shear it!".format(biggest))
print()

# 2.3 shearing the biggest
my_flock[spot] = 8
print("After shearing, here is my flock")
print(my_flock)
print()

# 2.4 one month growth
grow_flock = [sheep+50 for sheep in my_flock]
print("One month hass passed, now here is my flock")
print(grow_flock)
print()
