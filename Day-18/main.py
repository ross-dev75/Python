import turtle as t
import random
rgb_colors = [(230, 227, 223), (164, 153, 138), (238, 232, 234), (229, 236, 232), (226, 232, 238), (148, 91, 59), (56, 33, 20), (173, 148, 53), (42, 103, 153), (31, 40, 57), (127, 170, 191), (221, 207, 121)]
t.colormode(255)
timmy = t.Turtle()
timmy.pensize(10)

def uturn_left():
    timmy.left(90)
    timmy.penup()
    timmy.forward(40)
    timmy.left(90)
    timmy.pendown()

def uturn_right():
    timmy.right(90)
    timmy.penup()
    timmy.forward(40)
    timmy.right(90)
    timmy.pendown()

def paint_dots():
    for i in range(10):
        timmy.dot(20, random.choice(rgb_colors))
        timmy.penup()
        timmy.forward(40)
        timmy.pendown()
        timmy.dot(20, random.choice(rgb_colors))


for _ in range(3):
    for i in range(10):
        paint_dots()
        uturn_left()
        paint_dots()
        uturn_right()
