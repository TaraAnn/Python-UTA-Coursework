# Tara Ann Thomas (UTA ID : 1001584535)

# INSY5336 - HOMEWORK1

# Solution To Question 1(D) : Ex 15, CH 2

# Named Constants
RADIUS = 50 # length of each side of the outer triangle
DIAMETER = RADIUS * 2
OFFSET_X = 20 # Distance between the circles
SIDE_NO = 3 # Triangle has 3 sides
CIRCLES_NO = 5
import turtle

turtle.hideturtle()
turtle.speed(0)

# Drawing the first row of circles

for cycles in range(CIRCLES_NO-2):
    turtle.circle(RADIUS)
    turtle.penup()
    turtle.forward(DIAMETER + OFFSET_X)
    turtle.pendown()

turtle.penup()
turtle.goto(OFFSET_X*3,-RADIUS)
turtle.pendown()

for cycles in range(CIRCLES_NO-3):
    turtle.circle(RADIUS)
    turtle.penup()
    turtle.forward(DIAMETER + OFFSET_X)
    turtle.pendown()
        
turtle.done()
