import random
import turtle
from turtle import Turtle, Screen
import random
new_turtle = Turtle()
screen = Screen()
is_race_on=False

screen.setup(width=500, height=400)

user_bet = screen.textinput(title="make your bet", prompt="which a turtle will win the race ? enter the color:")

colors = ["red", "orange", "blue", "green", "gray", "brown", "yellow", "pink", "purple"]

# y_place=-100

y_position=[-70,-40,-10,20,50,80]
all_turtle=[]


for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    # new_turtle.color(random.choice(colors))
    new_turtle.goto(x=-230,y=y_position[turtle_index])
    all_turtle.append(new_turtle)

   # new_turtle.goto(x=-230, y=y_place)
    # y_place+=40


if user_bet:
    is_race_on =True

while is_race_on:

  for turtle in all_turtle:
      if turtle.xcor()>230:
          is_race_on=False
          winning_color=turtle.pencolor()
          if winning_color==user_bet:
              print(f"YOU WON!, and the {winning_color}turtle is the winner!")
          else:
              print(f"YOU lost!, and the {winning_color}turtle is the winner!")

      rand_distance=random.randint(0,20)
      turtle.forward(rand_distance)




# new_turtle=Turtle(shape="turtle")
# new_turtle.penup()
# new_turtle.color("pink")
# new_turtle.goto(x=-230,y=-60)

# new_turtle=Turtle(shape="turtle")
# new_turtle.penup()
# new_turtle.color("yellow")
# new_turtle.goto(x=-230,y=-20)


# new_turtle=Turtle(shape="turtle")
# new_turtle.penup()
# new_turtle.color("green")
# new_turtle.goto(x=-230,y=20)
#
# new_turtle=Turtle(shape="turtle")
# new_turtle.penup()
# new_turtle.color("blue")
# new_turtle.goto(x=-230,y=60)
#
# new_turtle=Turtle(shape="turtle")
# new_turtle.penup()
# new_turtle.color("red")
# new_turtle.goto(x=-230,y=100)

screen.exitonclick()
