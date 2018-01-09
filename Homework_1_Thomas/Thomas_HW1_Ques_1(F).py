# Tara Ann Thomas (UTA ID : 1001584535)

# INSY5336 - HOMEWORK1

# Solution To Question 1(F) : Ex 15, CH 2

SIDE_NO = 3 # This is because 1 side is already drawn in the outer for loop
SQUARE_NO = 2
SIDE_LENGTH = 100
VERTEX_ANGLE = 90
LINE_ANGLE_1 = 315 # 315 ([270+360/2]) is the angle of one of the diagonals
LINE_ANGLE_2 = 225 # ([180+270)/2] is the angle of the other diagonal
DASH = 100/9 # Because I want to make 9 divisions in the line
import turtle

#turtle.hideturtle()
turtle.speed(3)

turtle.dot()
turtle.left(VERTEX_ANGLE)
turtle.forward(SIDE_LENGTH)
for cycles in range(3):
    #print(cycles)
    turtle.dot()
    turtle.right(VERTEX_ANGLE)
    #turtle.forward(SIDE_LENGTH)
    if cycles %2==0:# So that the dashed lines occur only for alternate sides
        turtle.forward(DASH)
        turtle.penup()
        turtle.forward(DASH)
        turtle.pendown()
        turtle.forward(DASH*2)
        turtle.penup()
        turtle.forward(DASH)
        turtle.pendown()
        turtle.forward(DASH*2)
        turtle.penup()
        turtle.forward(DASH)
        turtle.pendown()
        turtle.forward(DASH)
        
    else :
        turtle.forward(SIDE_LENGTH)

# Draw diagonal 1
turtle.penup()
turtle.goto(0,SIDE_LENGTH)# Since it is a square, it is easy.. 
turtle.setheading(LINE_ANGLE_1)    #to figure out the coordinates.
turtle.pendown()
turtle.goto(SIDE_LENGTH,0)

# Draw diagonal 2
turtle.penup()
turtle.goto(SIDE_LENGTH,SIDE_LENGTH)
turtle.setheading(LINE_ANGLE_2)    
turtle.pendown()
turtle.goto(SIDE_LENGTH/2,SIDE_LENGTH/2)
turtle.dot()
turtle.goto(0,0)
        
turtle.done()
