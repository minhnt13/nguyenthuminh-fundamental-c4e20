from turtle import *

color("purple")
speed(10)
pensize(2)

square_side = 1

for k in range (50):   
    for i in range(4):
        forward(square_side)
        left(90)
    square_side += 3
    left(10)

mainloop()