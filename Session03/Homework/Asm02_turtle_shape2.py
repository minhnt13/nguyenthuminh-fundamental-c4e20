from turtle import *

colors = ['red', 'blue','brown','yellow','grey']

for shapecolor in colors:
    color(shapecolor)
    begin_fill()
    for side in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    forward(50)
    end_fill()  

mainloop()


