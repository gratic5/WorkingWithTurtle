from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.color("red")
timmy.shape("turtle")
Screen().colormode(255)
timmy.speed("fastest")
timmy.pensize(1.15)

def draw_spirograph(size_of_gap):
    for i in range(360 // size_of_gap):
        r,g,b = random.randint(0,255),random.randint(0,255),random.randint(0,255)
        timmy.pencolor(r,g,b)
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()
