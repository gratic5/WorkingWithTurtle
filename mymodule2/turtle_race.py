from turtle import Turtle, Screen
import random

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()
t6 = Turtle()

screen = Screen()
screen.setup(width=800,height=600)
screen.title("Turtle Race")
choice = screen.textinput("Make your bet","Who will win the next race? Enter a colour: ")

colors = ["purple", "blue", "green", "yellow", "orange", "red"]

turtles = [t1,t2,t3,t4,t5,t6]
for i,j in enumerate(turtles):
    j.shape("turtle")
    turtles[i].penup()
    turtles[i].setpos(-380,150-(i*60))
    j.color(colors[i])

race_on = True
winner = None

screen.listen()
while race_on:
    random.shuffle(turtles)  # Randomize order each loop
    for t in turtles:
        t.forward(random.randint(0, 10))
        if t.xcor() >= 390:
            race_on = False
            winner = t.pencolor()
            break
        

screen.bye()

if winner == choice.lower():
    print(f"You win! The {winner.title()} turtle won the race!")
else:
    print(f"You lose. The {winner.title()} turtle won the race.")