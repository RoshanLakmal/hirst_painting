# This is a sample Python script.
# import colorgram
#
# number_of_colors = 20
# colors = colorgram.extract('painting.jpg', number_of_colors)
#
# color_list = []
#
# def generate_color_tuple(rgb_obj):
#     genereated_tuple = (rgb_obj.r,rgb_obj.g,rgb_obj.b)
#     return genereated_tuple
#
# for color_item in colors:
#     rgb_obj = color_item.rgb
#     tuple_color =generate_color_tuple(rgb_obj)
#     color_list.append(tuple_color)
#
# print(color_list)

import turtle as t
import random

t.colormode(255)
turtle_start = t.Turtle()
turtle_start.shape("turtle")
# turtle_start.speed("fastest")

color_list = [(235, 234, 231), (235, 229, 232), (236, 34, 108), (221, 232, 237), (146, 27, 66), (230, 238, 233), (239, 75, 35), (7, 147, 92), (222, 170, 43), (183, 158, 47), (44, 191, 232), (27, 126, 193), (253, 223, 0), (125, 193, 77), (84, 26, 88), (178, 39, 100), (244, 219, 48), (29, 169, 119), (203, 60, 32), (208, 131, 165)]

for x in range(10):
    for y in range(10):
        turtle_start.dot(20, random.choice(color_list))
        turtle_start.penup()
        turtle_start.forward(50)
        # print(turtle_start.pos())
    turtle_start.setx(0)
    turtle_start.sety(50 * (x+1))
    # turtle_start.goto(1,1)
# for row in range(2):
#     for column in range(2):
#         print(column)
        # turtle_start.dot(20, random.choice(color_list))
        # turtle_start.penup()
        # turtle_start.forward(50)
    # turtle_start.home(0,row)
    # turtle_start.left(90)
    # turtle_start.dot(20, random.choice(color_list))
    # turtle_start.penup()
    # turtle_start.forward(50)
    # turtle_start.right(90)

    # turtle_start.forward(50)
    # turtle_start.dot(20, random.choice(color_list))
    # turtle_start.left(90)


t.Screen().exitonclick()