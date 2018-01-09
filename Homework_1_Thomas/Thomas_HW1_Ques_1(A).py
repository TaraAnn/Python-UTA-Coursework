# Tara Ann Thomas (UTA ID : 1001584535)

# INSY5336 - HOMEWORK1

# Solution To Question 1(A) : Ex 15, CH 2

#Named Constants
SIDE_NO = 3 # This is because 1 side is already drawn in the outer for loop
SQUARE_NO = 2
SIDE_LENGTH = 100
RHOMBUS_ANGLE = 45 # To get the shape of the rhombus
VERTEX_ANGLE=90

import turtle

turtle.hideturtle()
turtle.speed(0)

#Drawing the 2 squares
for squares in range (SQUARE_NO):
    turtle.right(RHOMBUS_ANGLE)
    turtle.forward(SIDE_LENGTH)
    for sides in range(SIDE_NO):
        turtle.left(VERTEX_ANGLE)
        turtle.forward(SIDE_LENGTH)

    turtle.setheading(180)

turtle.done()
