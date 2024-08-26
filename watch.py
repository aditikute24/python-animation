import turtle as tur

x = 150
tur.speed(7)

tur.penup()
tur.goto(0,x)
tur.seth(0)
for i in range(12):
     tur.circle(-x,29 if i>= 9 else 30)
     tur.write(i+1, font=("Arial",40,'bold'))

tur.goto(10,10)
tur.pendown()
tur.seth(140)
tur.width(15)
tur.forward(x-70)

tur.goto(10,10)
tur.seth(30)
tur.width(5)
tur.forward(x-30)


tur.seth(90)
tur.width(10)
tur.goto(20,10)
tur.pendown()
tur.color("#d4af37")
tur.circle(10)

tur.penup()
tur.goto(10, x+70)
tur.pendown()
tur.color('#2e2eb8')
tur.width(40)
tur.seth(180)
tur.circle(x+50)

tur.penup()
tur.color('black')
tur.goto(-30,x-40)
tur.pendown()
tur.write("ADITI KUTE")

tur.hideturtle()
tur.done()
