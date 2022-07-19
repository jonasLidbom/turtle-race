from turtle import Turtle, Screen
import random

is_race_on = False
x = -230
y = -100

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

# Creating turtles.
for color in colors:
    new_turtle = Turtle(shape="turtle", )
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=x, y=y)
    all_turtles.append(new_turtle)
    y += 40
# Starts the race.
if user_bet:
    is_race_on = True

# Conditions for the race to stop and to pick the winner.
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
