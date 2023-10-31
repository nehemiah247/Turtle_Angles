from turtle import Turtle, Screen
import random

timmy_turtle = Turtle()

penny = Turtle()
penny.pensize(5)
colours = ['pale green', 'blue', 'dark green', 'red', 'pink', 'brown', 'Black']


def draw_shape(num_side):
    angle = 360 / num_side
    for i in range(num_side):
        penny.forward(100)
        penny.right(angle)


for shape_side_n in range(3, 11):
    penny.color(random.choice(colours))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()