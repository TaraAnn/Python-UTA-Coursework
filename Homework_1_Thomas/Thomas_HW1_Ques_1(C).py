# Tara Ann Thomas (UTA ID : 1001584535)

# INSY5336 - HOMEWORK1

# Solution To Question 1(C) : Ex 15, CH 2

#My logic involves drawing 2 squares and then connecting the edges.
# So after drawing the squares I would only require 3 more lines
# that connect the edges to form the cuboid.


SIDE_NO = 3 # This is because 1 side is already drawn in the outer for loop
SQUARE_NO = 2
SIDE_LENGTH = 100
VERTEX_ANGLE = 90
LINE_ANGLE = 315 # 315 ([270+360/2]) is the angle at which the lines must be drawn to connect the corners

import turtle

turtle.hideturtle()
turtle.speed(0)

#Drawing the 2 squares
for squares in range (SQUARE_NO):
    turtle.right(VERTEX_ANGLE)
    turtle.forward(SIDE_LENGTH)
    for sides in range(SIDE_NO):
        turtle.left(VERTEX_ANGLE)
        turtle.forward(SIDE_LENGTH)

# Drawing line 1
turtle.penup()
turtle.goto(-SIDE_LENGTH,SIDE_LENGTH)# Since it is a square, it is easy.. 
turtle.setheading(LINE_ANGLE)    #to figure out the coordinates.
turtle.pendown()
turtle.goto(SIDE_LENGTH,-SIDE_LENGTH)

# Drawing line 2
turtle.penup()
turtle.goto(-SIDE_LENGTH,0)
turtle.setheading(LINE_ANGLE) 
turtle.pendown()
turtle.goto(0,-SIDE_LENGTH)

# Drawing line 3
turtle.penup()
turtle.goto(0,SIDE_LENGTH)
turtle.setheading(LINE_ANGLE)
turtle.pendown()
turtle.goto(SIDE_LENGTH,0)  
        
turtle.done()
