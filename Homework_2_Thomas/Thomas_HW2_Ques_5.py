# Tara Ann Thomas (UTA ID : 1001584535)

# INSY5336 - HOMEWORK2

# Solution To Question 5 : Ex 26, CH 5 - Turtle : City Skyline

import random
import turtle

turtle.speed(0)
turtle.hideturtle()
def main() :
    draw_building()
    draw_stars()
    turtle.goto(-30,30)
    draw_windows()
    turtle.goto(-130,110)
    draw_windows()
    turtle.goto(-210,-90)
    draw_windows()
    turtle.goto(90,50)
    draw_windows()
    turtle.goto(-50,-110)
    draw_windows()
    turtle.goto(-130,50)
    draw_windows()
    
    

def draw_building():
    turtle.fillcolor('grey')
    turtle.begin_fill()
    turtle.setup(600,700)
    turtle.penup()
    turtle.goto(-300,-200)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(120)
    turtle.right(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(220)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(170)
    turtle.right(90)
    turtle.forward(110)
    turtle.right(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(70)
    
    turtle.penup()
    turtle.right(90)
    turtle.goto(300,-350)
    turtle.right(90)
    turtle.goto(-300,-350)
    turtle.right(90)
    turtle.goto(-300,-200)
    turtle.end_fill()
    if turtle.bgcolor()=='white':
        turtle.bgcolor('midnightblue')

def draw_stars():
    turtle.goto (-240,180)
    turtle.dot(5,'white')
    turtle.goto (-250,40)
    turtle.dot(5,'white')
    turtle.goto (-130,280)
    turtle.dot(5,'white')
    turtle.goto (280,180)
    turtle.dot(5,'white')
    turtle.goto (20,120)
    turtle.dot(5,'white')
    turtle.goto (80,270)
    turtle.dot(5,'white')
    turtle.goto (150,69)
    turtle.dot(5,'white')
    turtle.goto (-289,310)
    turtle.dot(5,'white')

def draw_windows():
    turtle.pendown()
    turtle.pencolor('white')
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.end_fill()
    turtle.penup()
   


    
main()
