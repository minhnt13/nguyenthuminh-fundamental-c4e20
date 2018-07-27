from turtle import *
color("red")
speed(10)

for j in range (4):
    left(120)
    for i in range (2):
        forward(100)
        right(60)
        forward(100)
        right(120)      
    right(210)
mainloop ()

# another
# left(30)
# for i in range (4):
#     for sides in range (0,4,1):
#         if sides % 2 == 0:
#             forward(100)
#             right(60)
#         else:
#             forward(100)
#             right(120)
#     right(90)        
mainloop()