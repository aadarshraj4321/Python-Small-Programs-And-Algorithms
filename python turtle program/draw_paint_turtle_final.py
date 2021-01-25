import turtle
from turtle import Turtle, Screen
import random
#import colorgram


tut = Turtle()
screen = Screen()
tut.speed("fastest")
turtle.colormode(255)
tut.hideturtle()

##rgb_colors = []
##colors = colorgram.extract("dot.jpg", 20)
##for color in colors:
##    r = color.rgb.r
##    g = color.rgb.g
##    b = color.rgb.b
##    new_color = (r, g, b)
##    rgb_colors.append(new_color)
##    
##print(rgb_colors)


color_list = [(131, 166, 205), (222, 148, 106),
              (31, 42, 61), (199, 134, 147), (165, 59, 48), (140, 184, 162),
              (39, 105, 157), (238, 212, 89), (152, 58, 66), (217, 81, 70),
              (169, 29, 33), (236, 165, 156), (50, 112, 90), (35, 61, 55),
              (17, 97, 71), (156, 33, 30)]

tut.setheading(225)
tut.penup()
tut.forward(300)
tut.pendown()
tut.setheading(0)

num_of_dots = 10

for i in range(1, num_of_dots + 1):
    for _ in range(10):        
        tut.dot(20, random.choice(color_list))
        tut.penup()
        tut.forward(50)
        tut.pendown()
    tut.penup()
    tut.setheading(90)
    tut.forward(50)
    tut.setheading(180)
    tut.forward(500)
    tut.setheading(0)
    tut.pendown()


screen.exitonclick()
