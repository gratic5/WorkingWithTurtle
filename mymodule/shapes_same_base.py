from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
Screen().colormode(255)

for i in range(11):
    if i >= 3:
        r,g,b = random.randint(0,255),random.randint(0,255),random.randint(0,255)
        for j in range(i):
            timmy.forward(100)
            timmy.right(180 - (((i - 2)*180)/i))
        timmy.pencolor(r,g,b)
    


screen = Screen()
screen.exitonclick()