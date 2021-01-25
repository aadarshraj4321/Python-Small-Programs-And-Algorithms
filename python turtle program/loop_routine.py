from turtle import Turtle, Screen
import random

tut = Turtle(shape="turtle")
screen = Screen()




tut.penup()
tut.setheading(90)
tut.forward(300)
tut.right(90)
tut.forward(45)
tut.right(90)
tut.pendown()
#tut.setheading(0)





def write(text):
    tut.write(text, align="left")


def write1(text):
    tut.write(text, align="right")


def forward(val):
    tut.forward(val)

def right(val):
    tut.right(val)

def color():
    R = random.random()
    G = random.random()
    B = random.random()
    colors = tut.color(R, G, B)
    return colors



tut.speed(2)
tut.pensize(6)

color()
forward(50)
write("   7 AM")

forward(50)
write("   9 AM")

screen.delay(100)

forward (50)
write("   11 AM")

forward(50)
write("   Wake Up")
color()


forward(50)
write("   Listen Music | Refresh")
color()

forward(50)
write("   Started Online Classes")
color()

forward(50)
write("   On Going Classes")

forward(50)
write("   Same Fucki** Online Classes")

forward(50)
write("   6 PM | Now Real Work Start")
color()

forward(50)
write("   Working On Computer Vision")

forward(50)
write("   Working On Machine Leanring And AI Projects And Learning ALSO")

color()


right(90)
forward(60)
right(90)

screen.bgcolor("black")

forward(50)
write1("Working On Android App Development   ")

forward(25)
write1("10 PM   ")

forward(50)
write1("Doing Hacking With My Linux Girlfriend   ")
tut.color("white")
forward(50)
write1("Finally Dinner<^~^> With Silicon Valley S2 Loop 23 time   ")
tut.color("white")
forward(50)
write1("Doing Some Competition On Kaggle For Data Science   ")

forward(50)
write1("Solve Problem From DS ALGO   ")

forward(50)
write1("Bhtakana On Youtube And Internet Surfing for 20 Min   ")


forward(50)
write1("2 AM | Doing Exercise It's Like Mad   ")
tut.color("white")
forward(50)
write1("Doing Some Code Again   ")
tut.color("white")
forward(50)
write1("Searching About Elon Musk   ")


forward(40)
write1("5 Am | Good Night | Bed Bula Raha Hai   ")


