# Tara Ann Thomas 

# INSY5336 - HOMEWORK2

# Solution To Question 2 : Ex 16, CH 4 - Turtle : Repeating Squares

import turtle

# Named Constants
NO_OF_SQUARES = 100
NO_OF_SIDES = 4
VERTEX_ANGLE = 90
LOOPS = 3

side_length = 2 # Length of the smallest square
step = 3 # To draw the next square


turtle.speed(0)
turtle.hideturtle()

#Draw 1st 2 squares
side_length = side_length + step
for count2 in range(LOOPS):
    turtle.left(VERTEX_ANGLE)
    turtle.forward(side_length)
turtle.right(VERTEX_ANGLE)
turtle.forward(step)
side_length = side_length + step
for count3 in range(LOOPS-1):
    turtle.right(VERTEX_ANGLE)
    turtle.forward(side_length)
turtle.left(VERTEX_ANGLE)
turtle.forward(step)

#Draw 96 squares
for count1 in range(NO_OF_SQUARES//2 - 4):
    side_length = side_length + step
    for count2 in range(LOOPS-1):
        turtle.left(VERTEX_ANGLE)
        turtle.forward(side_length)
    turtle.right(VERTEX_ANGLE)
    turtle.forward(step)
    side_length = side_length + step
    for count3 in range(LOOPS-1):
        turtle.right(VERTEX_ANGLE)
        turtle.forward(side_length)
    turtle.left(VERTEX_ANGLE)
    turtle.forward(step)

#Draw last 2 squares
side_length = side_length + step
for count2 in range(LOOPS-1):
    turtle.left(VERTEX_ANGLE)
    turtle.forward(side_length)
turtle.right(VERTEX_ANGLE)
turtle.forward(step)
side_length = side_length + step
for count3 in range(LOOPS-1):
    turtle.right(VERTEX_ANGLE)
    turtle.forward(side_length)
   
#Draws missing borders of squares
turtle.goto(0,0)
turtle.goto(-290,0)
