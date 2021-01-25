from turtle import Turtle
import turtle
import random


tut = Turtle()
#tut.speed(100)
#turtle.screensize(1000, 1000)
tut.speed("fastest")
#tut.pensize(12)

def color():
    R = random.random()
    G = random.random()
    B = random.random()

    return (R, G, B)

def donut():
    for _ in range(1000):
        tut.color(color())
        tut.circle(100)
        tut.penup()
        tut.forward(2)
        tut.right(3)
        tut.pendown()
        
donut()
