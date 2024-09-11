# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(7)

# Draw the Level 3 version of the room
window = room.draw_room(level = 3)

###
# Start your code here
forward(40)
for _ in range(30):
    forward(40)
    right(90)
    forward(40)
    
 
# End your code here
###
 
window.exitonclick()