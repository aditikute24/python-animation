from turtle import *
import colorsys
bgcolor('black')

h = 0.2
speed(0)

def draw():
    for i in range(300):
        c = colorsys.hsv_to_rgb(h,1,1)
        pencolor(c)
        fillcolor(c)
        circle(190-i, 90)
        left(90)
        circle(190-i,90)
        left(18)
draw()
done()
