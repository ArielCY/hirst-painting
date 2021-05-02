# import colorgram
#
# colors = colorgram.extract('image.jpg', 50)
# #print(colors)
# rgb_color = []
# # for color in colors:
# #     rgb_color.append(color.rgb)
# # print(rgb_color)
#
# for color in colors:
#     new_r = color.rgb.r
#     new_g = color.rgb.g
#     new_b = color.rgb.b
#     new_color = [new_r, new_g, new_b]
#     rgb_color.append(new_color)
#
# print(rgb_color)
color_list = [(21, 114, 174), (142, 163, 184), (204, 137, 167), (192, 174, 15), (148, 16, 31), (68, 23, 31), (16, 139, 58), (237, 212, 66), (216, 160, 93), (50, 28, 26), (122, 71, 101), (198, 66, 28), (6, 107, 64), (228, 168, 197), (243, 216, 3), (25, 179, 89), (241, 74, 29), (20, 172, 189), (111, 191, 142), (183, 94, 116), (188, 181, 214), (35, 37, 46), (157, 206, 216), (138, 26, 21), (238, 168, 156), (9, 101, 105), (148, 214, 173), (7, 76, 29), (113, 122, 160), (46, 59, 104), (104, 113, 0)]

import turtle as turtle_module
import random

tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup() # no line
tim.hideturtle() # hide turtle: no arrow
turtle_module.colormode(255)
tim.setheading((180+270)/2) # turn to left bottom corner
tim.forward(300) # walk to left bottom corner
tim.setheading(0) # facing east and walk to straight
num_dot = 100

for dot_count in range(1, num_dot + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90) # turn right
        tim.forward(50)
        tim.setheading(180) # turn left
        tim.forward(50*10)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()