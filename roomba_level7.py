# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, tracer, update
import room

tracer(0, 0)

# THIS PARAMETER CAN CHANGE!!!
# Make sure your code works for n_alcoves = 0, 1, 2, 3, and 4
# (You are allowed to use this parameter in your code)
n_alcoves = 3

# Draw the Level 7 version of the room
window = room.draw_room(level = 7, n_alcoves = n_alcoves)

###
# Start your code here
forward(40)
left(90)
forward(120)
right(180)
forward(240)
left(90)
forward(40)
right(90)
forward(40)
right(180)
for _ in range (3):
    forward(320)
    right(90)
    forward(40)
    right(90)
    forward(320)
    left(90)
    forward(40)
    left(90)
forward(320)
left(90)
forward(120)
right(90)
forward(40)
right(180)
forward(400)
right(180)
forward(200)
right(90)
forward(240)
left(90)
forward(160)
right(180)
forward(320)
left(90)
forward(40)
right(90)
forward(80)
right(180)
forward(480)
right(90)
forward(40)
left(90)
forward(40)
right(180)
forward(560)
left(90)
forward(40)
right(90)
forward(40)
right(180)
forward(640)
right(90)





 
 
# End your code here
###
update()
window.exitonclick()