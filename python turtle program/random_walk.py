from turtle import Turtle
import turtle
import random


tut = Turtle()
#tut.speed(100)
#turtle.screensize(1000, 1000)
tut.speed("fastest")
tut.pensize(12)

def color():
    R = random.random()
    G = random.random()
    B = random.random()

    return (R, G, B)


directions = [0, 90, 180, 270]

for _ in range(1000):
    tut.color(color())
    tut.forward(30)
    tut.setheading(random.choice(directions))
