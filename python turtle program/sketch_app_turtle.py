
from turtle import Turtle, Screen


tut = Turtle(shape="turtle")
screen = Screen()
tut.color("red")

screen.bgcolor("black")

screen.listen()

def move():
    tut.forward(20)
def backward():
    tut.backward(20)
def left():
    tut.left(20)
def right():
    tut.right(20)
def screenClear():
    tut.reset()

screen.onkey(key="w", fun=move)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=screenClear)























#screen.exitonclick()
