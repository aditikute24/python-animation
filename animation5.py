from turtle import *
import colorsys
bgcolor('black')
pensize(2)
h = 0

for i in range(550):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.008
    color(c)
    up()
    fd(1/2)
    goto(0,0)
    down()
    rt(60)
    fillcolor('black')
    begin_fill()
    circle(-i,60)
    rt(144)
    for j in range(3):
        circle(j*20,100)
        rt(105)
done()
