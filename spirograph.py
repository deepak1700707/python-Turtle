import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
turtle.hideturtle()

for i in range(100):
    for color in ["red","magenta","blue","cyan","green","yellow","white"]:
        turtle.color(color)
        turtle.circle(100)
        turtle.left(10)

