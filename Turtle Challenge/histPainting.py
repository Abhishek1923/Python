# FOR EXTRACTING THE COLOR FROM THE IMAGE

# import colorgram as cg
# color_list = cg.extract("image.jpg", 30)
# color_palette = []
#
# for color in color_list:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     color_palette.append(new_color)


color_list=[(198, 159, 116), (70, 92, 129), (147, 85, 53), (218, 210, 116), (138, 160, 191), (178, 160, 38), (184, 146, 164), (28, 32, 46), (58, 34, 23), (120, 70, 93), (139, 175, 154), (77, 115, 79), (143, 25, 16), (186, 97, 82), (61, 31, 42), (121, 27, 41), (45, 58, 94), (177, 96, 114), (102, 119, 170), (34, 52, 45), (100, 160, 85), (214, 175, 192), (216, 181, 173), (160, 209, 191), (67, 86, 23), (219, 206, 8)]

from turtle import Screen
import turtle as t
import random
tim=t.Turtle()
t.colormode(255)
tim.speed(10)
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
no_of_dots=100

for dots in range(1,no_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)
    # tim.pendown()

    if dots%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen=Screen()
screen.exitonclick()