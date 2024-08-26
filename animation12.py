from turtle import *
speed(0)
hideturtle()
bgcolor('black')
for i in range(150):
    color('blue')
    circle(i)
    color('red')
    circle(i*1.2)
    color('orange')
    circle(1*1.5)
    left(5)
    backward(5)

done()
