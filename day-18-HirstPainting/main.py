
import turtle as t
from turtle import Turtle, Screen
import random
import colorgram

# rgb_colors = []
# colors = colorgram.extract('hirstimage.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(214, 153, 73), (174, 47, 78), (139, 30, 54), (36, 43, 72), (237, 217, 95), (160, 182, 26), (34, 108, 151), (212, 67, 99), (109, 187, 203), (22, 144, 80), (41, 49, 113), (238, 72, 55), (72, 185, 108), (142, 86, 61), (199, 123, 166), (76, 26, 47), (60, 41, 39), (237, 200, 1), (236, 165, 192), (4, 187, 195), (28, 49, 46), (78, 127, 192), (91, 187, 145), (1, 87, 119), (162, 216, 184), (77, 70, 43)]

tim = Turtle()
tim.shape("turtle")
tim.color("purple")
t.colormode(255)
# motion

def draw(space, x):
    for i in range(x):
        for j in range(x):
            dot_color = random.choice(color_list)
            tim.dot(20, dot_color)
            tim.forward(space)
            tim.color(dot_color)
        tim.backward(space*x)
        tim.right(90)
        tim.forward(space)
        tim.left(90)

tim.penup()
draw(30,10)

# dot with
# 60 diameter
# yellow color

screen = Screen()
screen.exitonclick()
