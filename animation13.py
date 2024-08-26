import turtle as tur
import colorsys as cs
tur.setup(800,800)
tur.speed(0)
tur.tracer(10)
tur.width(2)
tur.bgcolor('black')
for i in range(25):
    for j in range(15):
        tur.color(cs.hsv_to_rgb(j/15,i/25,1))
        tur.right(90)
        tur.circle(200-i*4, 90)
        tur.left(90)
        tur.circle(100-i*4, 90)
        tur.right(180)
        tur.circle(50,20)

tur.hideturtle()
tur.done()
