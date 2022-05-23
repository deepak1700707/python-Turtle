import turtle
turtle.showturtle()
turtle.penup()
##turtle.goto(-150,150)
turtle.bgcolor('black')
turtle.pensize(5)
turtle.pendown()
turtle.hideturtle()
l=['red','green','yellow','pink','orange','blue','white']
turtle.begin_fill()
for i in l:
    for j in range(6):
        turtle.color(i)
        turtle.right(60)
        turtle.forward(100)
        turtle.left(120)
        turtle.forward(100)
turtle.end_fill()
