import turtle
import math

# Screen setup
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Heart Animation")

# This turns off automatic updates
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.color("hotpink")
t.pensize(2)

text = turtle.Turtle()
text.hideturtle()
text.penup()
text.color("pink")
text.goto(0, -40)

def heart(t_val):
    x = 16 * math.sin(t_val)**3
    y = 13 * math.cos(t_val) - 5 * math.cos(2*t_val) - 2 * math.cos(3*t_val) - math.cos(4*t_val)
    return x*15, y*15

angle = 0

while True:
    t.clear()

    first = True
    for i in range(630):
        x, y = heart(i/100)

        rx = x*math.cos(angle) - y*math.sin(angle)
        ry = x*math.sin(angle) + y*math.cos(angle)

        if first:
            t.penup()
            t.goto(rx, ry)
            t.pendown()
            first = False
        else:
            t.goto(rx, ry)

    text.clear()
    text.write("I love you 💗", align="center", font=("Arial", 26, "bold"))

    angle += 0.05

    # THIS updates the animation
    screen.update()
    