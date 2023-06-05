from turtle import Turtle, Screen

screen = Screen()

colors = ['blue', 'green', 'cyan', 'orange', 'red', 'purple']

# Setting up screen dimension
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your best", prompt="Which turtle will win the race? Enter a color: ")

turtles = []

y = -80

for color in colors:
    turtle = Turtle(shape='turtle')
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-230, y=y)
    y += 30

# turtle1 = Turtle(shape='turtle')
# turtle1.penup()
# turtle1.goto(x=-230, y=-100)

screen.exitonclick()