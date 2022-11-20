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
mode("logo")
penup()


# drawing the letter N, first part
goto (-300,0) # moving the turtle to a start point, located at the left edge of the screen
pendown() # order the turtle to trace
begin_fill() # filling the future drawing after closing lines
forward (300) # tracing a straight vertical line from the botton to to top
circle(10,180) #  drawing half a circle to the left
forward(300) #tracing back a straight vertical line from the top  to to bottom
circle(10,180) # drawing the half of circle in order to close the drawing
end_fill() #filling the drawing after the lines have been closed
penup() # ordering the turtle to not to draw

# drawing the letter N, second part
goto (-305,300) # moving the turtle to th top part so it starts drawing from there

begin_fill()
right(155)  # in this case, i need to change the dircection of the turtle's head,
#setting the angle at -45° on the x axis
# so it can draw the diagonal from top left corner to botton right corner.
pendown()
forward(325)
circle(10,180)
forward(275)
circle(10,180)
end_fill()
penup()







