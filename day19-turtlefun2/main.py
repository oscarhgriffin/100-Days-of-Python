from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def move_counter_clock():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def move_clock():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def shake():
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clock)
screen.onkey(key="d", fun=move_clock)
screen.onkey(key="space", fun=shake)
screen.exitonclick()

