from turtle import Turtle, Screen
import random as rand

screen = Screen()
# Setting up screen dimension
screen.setup(width=500, height=400)

colors = ['blue', 'green', 'cyan', 'orange', 'red', 'purple']

is_race_on = False

user_bet = screen.textinput(title="Make your best", prompt="Which turtle will win the race? Enter a color: ")

y = -80
all_turtles = []

for color in colors:
    turtle = Turtle(shape='turtle')
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-230, y=y)
    y += 30
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost.. The {winning_color} turtle is the winner..")
    
        rand_distance = rand.randint(0, 10)
        turtle.forward(rand_distance)

# turtle1 = Turtle(shape='turtle')
# turtle1.penup()
# turtle1.goto(x=-230, y=-100)

screen.exitonclick()