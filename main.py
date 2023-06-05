from turtle import Turtle, Screen

screen = Screen()

turtle1 = Turtle()

# Setting up screen dimension
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your best", prompt="Which turtle will win the race? Enter a color: ")

screen.exitonclick()