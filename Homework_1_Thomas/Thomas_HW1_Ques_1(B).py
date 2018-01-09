# Tara Ann Thomas 

# INSY5336 - HOMEWORK1

# Solution To Question 1(B) : Ex 15, CH 2

# Named Constants
LENGTH_SIDE = 100 # length of each side of the outer triangle
ANGLE = 120 # Each angle is 60 deg which in terms of turtle coordinates is 120 deg
SIDE_NO = 3 # Triangle has 3 sides

import turtle

turtle.hideturtle()
turtle.speed(0)

#Drawing outer triangle
for sides in range(SIDE_NO):
    turtle.forward(LENGTH_SIDE)
    turtle.left(ANGLE)

# Determining coordinates of the inner triangle.
x_cor_1 = LENGTH_SIDE/2
y_cor_1 = (((LENGTH_SIDE**2)-\
            ((LENGTH_SIDE/2)**2))**(1/2))/2\
            # Height of the outer triangle(Pythagoras theorem)/2
x_cor_2 = LENGTH_SIDE
y_cor_2 = 0

# Drawing inner triangle & filling it with color red
turtle.fillcolor('red')
turtle.begin_fill()
turtle.goto(x_cor_1,y_cor_1)
turtle.goto(x_cor_2,y_cor_2)
turtle.end_fill()
        
turtle.done()
