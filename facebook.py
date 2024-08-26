import turtle

def draw_square(color,size):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()

def draw_facebook_logo():
    turtle.speed(2)
    turtle.bgcolor("white")
    turtle.penup()
    turtle.goto(-80,60)
    turtle.pendown()

    # draw the blue background
    draw_square('#3b5998',200)

    # draw the white letter 'f'
    turtle.penup()
    turtle.goto(-60,60)
    turtle.pendown()
    turtle.color("white")
    turtle.write("f", font=('Arial',120,'normal'))

    #hide the turtle
    turtle.hideturtle()
    turtle.done()

draw_facebook_logo()

