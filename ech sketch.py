from  turtle import  Turtle, Screen

tim=Turtle()
screen=Screen()



def tim_forward():
    tim.forward(10)


def tim_backward():
    tim.backward(10)


def turn_right():
   new_heading=tim.heading()-10
   tim.setheading(new_heading)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(tim_forward,"w")
screen.onkey(tim_backward,"s")
screen.onkey(turn_right,"d")
screen.onkey(turn_left,"a")
screen.onkey(clear,"c")

screen.exitonclick()