from turtle import Turtle, Screen
import turtle
import random




tu = Turtle()
screen  = Screen()

#screen.bgcolor("black")
tu.pensize(18)
tu.speed(10)

tu.penup()
tu.setheading(90)
tu.forward(200)
tu.pendown()
tu.right(90)


def color():
    R = random.random()
    G = random.random()
    B = random.random()
    color_color = tu.color(R, G, B)
    return color_color


color_list = ["white", "black"]


def f():
    color()
    tu.right(-90)
    tu.forward(100)
    tu.right(90)
    tu.forward(60)
    color()
    tu.right(90)
    tu.forward(15)
    tu.right(90)
    tu.forward(60)
    color()
    tu.right(-90)
    tu.forward(30)
    tu.right(-90)
    tu.forward(60)
    tu.right(90)
    color()
    tu.forward(15)
    tu.right(90)
    tu.forward(60)
    tu.right(-90)
    color()
    tu.forward(40)
    tu.right(-90)


def u():
    color()
    tu.right(-90)
    tu.forward(100)
    tu.backward(100)
    color()
    tu.right(90)
    tu.forward(60)
    color()
    tu.right(-90)
    tu.forward(100)
    color()
    tu.backward(100)
    tu.right(90)

def c():
    color()
    tu.forward(70)
    tu.backward(70)
    color()
    tu.right(-90)
    tu.forward(100)
    color()
    tu.right(90)
    color()
    tu.forward(70)


def k():
    color()
    tu.right(-90)
    tu.forward(100)
    color()
    tu.backward(50)
    tu.right(60)
    color()
    tu.forward(70)
    tu.backward(70)
    tu.right(90)
    color()
    tu.right(-10)
    tu.forward(200)
    color()
    tu.right(135)
    tu.forward(900)
    tu.right(180)

##def circle():
##    tu.circle(100)
##    tu.forward(3)
##    tu.right(3)


def circle(size):
    for _ in range(int(360 / size)):
        screen.bgcolor(random.choice(color_list))
        color()
        tu.circle(100)
        tu.setheading(tu.heading() + size)




screen.bgcolor("black")



f()
tu.penup()
tu.forward(120)
tu.pendown()

screen.bgcolor("white")


u()
tu.penup()
tu.forward(60)
tu.pendown()

screen.bgcolor("black")





c()
tu.penup()
tu.right(90)
tu.forward(100)
tu.right(-90)
tu.forward(60)
tu.pendown()

screen.bgcolor("white")


k()
tu.speed(9)

screen.bgcolor("black")

tu.pensize(8)

#circle(10)






def mid_finger_2():
    for i in range(2):
        color()
        tu.right(-90)
        tu.forward(60)
        tu.right(90)
        tu.forward(30)
        tu.right(90)
        tu.forward(60)
        tu.right(90)
        tu.forward(30)
        tu.backward(30)
        tu.right(180)
        tu.forward(10)

def mid_single():
    color()
    tu.right(-90)
    tu.forward(110)
    tu.right(90)
    tu.forward(30)
    tu.right(90)
    tu.forward(25)
    tu.right(90)
    tu.forward(30)
    tu.backward(30)
    tu.right(-90)
    tu.forward(85)
    tu.right(90)
    tu.forward(30)
    tu.backward(30)
    tu.right(180)
    tu.forward(10)



def mid_finger_3():
    for i in range(2):
        color()
        tu.right(-90)
        tu.forward(60)
        tu.right(90)
        tu.forward(30)
        tu.right(90)
        tu.forward(60)
        tu.right(90)
        tu.forward(30)
        tu.backward(30)
        tu.right(180)
        tu.forward(10)
        

tu.pensize(10)

screen.bgcolor("white")
mid_finger_2()
screen.bgcolor("black")
mid_single()
screen.bgcolor("white")
mid_finger_3()




screen.bgcolor("black")
screen.exitonclick()












