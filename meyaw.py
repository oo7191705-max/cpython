import turtle
t = turtle.Turtle()
turtle.bgcolor("black")
t.color("red")
t.speed(0)

t.penup()
t.goto(0,-200)
t.pendown()

for i in range(200):
    t.forward(i*2)
    t.left(91)
    
turtle.done()

