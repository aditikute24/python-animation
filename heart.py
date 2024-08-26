import turtle
t = turtle.Turtle()
t.shapesize(0.2,0.2)
s = turtle.Screen()
s.bgcolor('white')

t.fillcolor('red')
t.begin_fill()

t.left(50)
t.forward(240)
t.circle(90,200)
t.left(221)
t.circle(90,200)
t.forward(260)


t.end_fill()

turtle.done()
