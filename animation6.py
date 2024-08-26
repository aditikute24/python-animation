from turtle import *
import colorsys
tracer(2)
pensize(2)
h = 0.2
bgcolor('black')
lt(80)
fd(250)
lt(180)
lt(80)
for i in range(10000):
    c = colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h += 0.004
    fd(i)
    rt(50)
    rt(40)
    fd(500)
    rt(120)
done()
