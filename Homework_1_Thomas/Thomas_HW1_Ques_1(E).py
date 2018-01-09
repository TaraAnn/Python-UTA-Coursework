# Tara Ann Thomas 

# INSY5336 - HOMEWORK1

# Solution To Question 1(E) : Ex 15, CH 2

# Named Constants
LINE_LENGTH = 100
RADIUS_CIRCLE = 30
WEST_COORDINATE = -130 # To avoid west appearing on top of the line
#WEST_COORDINATE_Y = -20
import turtle

turtle.hideturtle()
turtle.speed(0)


# Drawing line 1
turtle.penup()
turtle.goto(WEST_COORDINATE,0)
turtle.write('West')
turtle.forward(30)
turtle.pendown()
turtle.goto(LINE_LENGTH,0)
turtle.write('East') 

# Drawing line 2
turtle.penup()
turtle.goto(0,LINE_LENGTH)
turtle.setheading(270)
turtle.write('North')    
turtle.pendown()
turtle.goto(0,-LINE_LENGTH)
turtle.penup()
turtle.goto(0,-LINE_LENGTH-20)
turtle.write('South')

# Drawing Circle
turtle.penup()
turtle.goto(-RADIUS_CIRCLE,0)
turtle.pendown()
turtle.circle(30)

        
turtle.done()
