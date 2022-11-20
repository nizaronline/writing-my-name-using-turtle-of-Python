# this program is intended to draw my name usin Python and the module turtle

# importing the module turtle and all its methods
from turtle import *

# defining the screen
screen=Screen()
screen.bgcolor("white")
screen.title("writing my name")

# defining the turtle as the object which makes the drawing
color("black")
speed(1)
penup()

mode("logo")

# drawing the letter N, first part

# moving the turtle to a start point, located at the left edge of the screen
goto (300,0)

pendown() # order the turtle to trace
begin_fill() # filling the future drawing after closing lines
forward (300) # tracing a straight vertical line from the botton to to top
circle(5,180) #  drawing half a circle to the left
forward(300) #tracing back a straight vertical line from the top  to to bottom
circle(5,180) # drawing the half of circle in order to close the drawing
end_fill() #filling the drawing after the lines have been closed
penup() # ordering the turtle to not to draw







