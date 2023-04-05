import time
from turtle import Turtle, Screen
import random

timmy=Turtle()
timmy.shape('turtle')
timmy.color('red')

# making a square with turtle
# for _ in range(4):
#     timmy.fd(100)
#     timmy.right(90)

# drawing a dashed line
# for _ in range(15):
#     timmy.fd(10)
#     timmy.penup()
#     timmy.fd(10)
#     timmy.pendown()

# drawing different shapes with different color

# col=["blue","dark red","dark green","coral","powder blue","olive","tomato","indigo"]
# def draw_shape(num_sides):
#     angle=360/num_sides
#     for _ in range(num_sides):
#         timmy.fd(100)
#         timmy.right(angle)
# import random
# for shape in range(3,11):
#     draw_shape(shape)
#     timmy.color(random.choice(col))

# random walk
# col=["blue","dark red","dark green","coral","powder blue","olive","tomato","indigo"]
# direction=[0,90,180,270]
# timmy.speed(10)
# for _ in range(200):
#     timmy.pen(fillcolor="black", pencolor=random.choice(col), pensize=10)
#     timmy.fd(100)
#     timmy.setheading(random.choice(direction))

# random color

import turtle as t
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

# direction=[0,90,180,270]
# timmy.pensize(15)
# timmy.speed(10)
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.fd(30)
#     timmy.setheading(random.choice(direction))


# Spirograph
timmy.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+size_of_gap)
draw_spirograph(5)


screen=Screen()
screen.exitonclick()