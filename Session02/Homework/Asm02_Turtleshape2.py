from turtle import *
speed(10)
for sides in range(3,7,1):
    if sides % 2 == 0:
        color("red")
    else:
        color("blue")
    for i in range(sides):
        forward(100)
        left(360/sides)
mainloop()
