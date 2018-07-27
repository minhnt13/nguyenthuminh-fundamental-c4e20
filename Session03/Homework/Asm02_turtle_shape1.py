from turtle import *
colors = [
    ('red', 3), 
    ('blue', 4),
    ('brown', 5),
    ('yellow', 6),
    ('grey', 7)
]
speed(10)
for color,sides in colors:
    pencolor(color)
    for i in range(sides):
        forward(100)
        left(360/sides)
mainloop()
