# import colorgram
# colors = colorgram.extract('image.jpeg', 10)
# colors_list = []
# for color in colors:
#     colors_list.append(color)
#
# print(colors_list)
# color_rgb = []
#
# for each in colors_list:
#     r = each.rgb.r
#     g = each.rgb.g
#     b = each.rgb.b
#     new_color = r,g,b
#     color_rgb.append(new_color)
#
# print(color_rgb)

import turtle as t
from turtle import Turtle, Screen
import random

timmy = t.Turtle()
t.colormode(255)

color_list = [(192, 163, 119), (126, 185, 156), (213, 213, 132),
              (187, 222, 201), (155, 212, 186), (137, 168, 182),
              (220, 217, 177), (181, 141, 159), (91, 155, 110),
              (145, 149, 76)]

a = 1
b = 500


# changing speed of turtle
timmy.speed("fastest")

# making patten
while b:
    # makes the turtle to move forward
    timmy.forward(a)

    # makes the turtle to move left
    timmy.left(121)
    timmy.left(1)
    a += 1
    b -= 1

# a = 20
# timmy.speed("fastest")
# for each in range(1, 100):
#     timmy.left(5)
#     timmy.circle(each, 360, 3)
#
# timmy.left(120)
# for each in range(1, 100):
#     timmy.left(5)
#     timmy.circle(each, 360, 3)

# for each in range(1, 100):
#     timmy.left(5)
#     for _ in range(1, 4):
#         timmy.forward(a)
#         timmy.left(120)
#         a = a + 1

# Different graphics
# timmy.width(1)
# timmy.speed("fastest")
# for each in range(20, 70):
#     timmy.pencolor("black")
#     timmy.circle(each, 360, 3)
#     timmy.left(5)
#
# timmy.setx(0)
# timmy.sety(0)
# timmy.left(60)
# for each in range(20, 70):
#     timmy.pencolor("black")
#     timmy.circle(each, 360, 3)
#     timmy.left(5)
#
# timmy.setx(0)
# timmy.sety(0)
# timmy.left(60)
# for each in range(20, 70):
#     timmy.pencolor("black")
#     timmy.circle(each, 360, 3)
#     timmy.left(5)


# Hirst Painting code

# timmy.penup()
# timmy.hideturtle()
# timmy.sety(300)
#
# for _ in range(1, 11):
#     timmy.setx(-300)
#     y = timmy.ycor()
#     timmy.sety(y - 50)
#     for _ in range(1, 11):
#         timmy.forward(50)
#         timmy.dot(20, random.choice(color_list))

screen = Screen()
screen.exitonclick()
