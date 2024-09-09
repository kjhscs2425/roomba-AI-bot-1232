# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward
import room

# THIS PARAMETER CAN CHANGE!!!
# Make sure your code works for n_alcoves = 0, 1, 2, 3, and 4
# (You are allowed to use this parameter in your code)
n_alcoves = 3
# THIS PARAMETER CAN CHANGE!!!
# Make sure your code works for any positive integer value of cirlce_room_radius
# (You are allowed to use this parameter in your code)
circle_room_radius = 2

# Draw the Level 5 version of the room
window = room.draw_room(level = 8,
                        n_alcoves = n_alcoves,
                        radius = circle_room_radius)

###
# Start your code here
forward(40)
right(90)
forward(40)
right(180)
forward(80)
right(180)
forward(40)
left(90)
forward(200)
right(180)
forward(80)
left(90)
forward(160)
right(180)
forward(320)
right(180)
forward(40)
right(90)
forward(40)
right(180)
forward(80)
right(180)
forward(40)
left(90)
forward(240)
right(90)
forward(40)
right(180)
forward(80)
right(180) 
forward(40)
right(90)
forward(80)
right(90)
forward(40)
left(90)
forward(80)
left(90)
forward(80)
left(90)
forward(80)
left(90)
forward(40)

 
# End your code here
###
 
window .exitonclick()
