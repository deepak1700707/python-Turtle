import turtle as t
t.bgcolor('black')
l=['red','yellow','pink','green','blue','violet','orange','purple']
t.speed(200)
t.hideturtle()
t.pensize(4)
for i in range(25):
    for i in l:
        t.color(i)
        t.circle(100)
        t.left(15)
    
