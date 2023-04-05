import turtle
tim = turtle.Turtle()
def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def move_counter_clockwise():
    tim.setheading(tim.heading()+10)
def move_clockwise():
    tim.setheading(tim.heading()-10)
def clear_scr():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen = turtle.Screen()

screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(move_counter_clockwise,"a")
screen.onkey(move_clockwise,"d")
screen.onkey(clear_scr,"c")

screen.exitonclick()