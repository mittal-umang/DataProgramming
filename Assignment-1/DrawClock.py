# Chapter 1 Question 21
# Write a program that displays a clock to show the time
# 9:15:00

import turtle


def __clock__():
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.circle(100)
    turtle.penup()
    turtle.goto(0, 90)
    turtle.pendown()
    turtle.write("12", move=False, align="left")
    turtle.penup()
    turtle.goto(90, 0)
    turtle.pendown()
    turtle.write("3", move=False, align="left")
    turtle.penup()
    turtle.goto(0, -90)
    turtle.pendown()
    turtle.write("6", move=False, align="left")
    turtle.penup()
    turtle.goto(-90, 0)
    turtle.pendown()
    turtle.write("9", move=False, align="left")
    turtle.penup()
    turtle.goto(0, 0)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(80)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(70)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.left(180)
    turtle.pendown()
    turtle.forward(60)
    turtle.done()


__clock__()
