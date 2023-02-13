import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which tutle will win the race? Enter a color: ")
colors = ["red", 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []
y = -100
for color in colors:
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    tim.goto(-230, y)
    turtles.append(tim)
    y += 40

if user_bet in colors:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is winner!")
            else:
                print(f"You've lose! The {winning_turtle} turtle is winner!")
        turtle.speed("slow")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
