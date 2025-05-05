import random,turtle

timmy = turtle.Turtle()
timmy.pensize(5)
turtle.Screen().colormode(255)
timmy.color("red")
timmy.shape("turtle")

 
for i in range(100):
    choice = random.randint(1,4)
    if choice == 1:
        timmy.back(20)
    if choice == 2:
        timmy.left(90)
        timmy.forward(20)
    if choice == 3:
        timmy.forward(20)
    if choice == 4:
        timmy.right(90)
        timmy.forward(20)

    r,g,b = random.randint(0,255),random.randint(0,255),random.randint(0,255)
    timmy.pencolor(r,g,b)


screen = turtle.Screen()
screen.exitonclick()