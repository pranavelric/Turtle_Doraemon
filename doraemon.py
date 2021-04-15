from turtle import *
t = Turtle()


def my_goto(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def eyes():
    t.fillcolor("#ffffff")
    t.begin_fill()
    tracer(False)
    a = 2.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            t.left(3)
            t.forward(a)
        else:
            a += 0.05
            t.left(3)
            t.forward(a)
    tracer(True)
    t.end_fill()


def beard():
    my_goto(-32, 135)
    t.seth(165)
    t.forward(60)

    my_goto(-32, 125)
    t.seth(180)
    t.forward(60)

    my_goto(37, 135)
    t.seth(15)
    t.forward(60)
    my_goto(37, 125)
    t.seth(0)
    t.forward(60)
    my_goto(37, 115)
    t.seth(-13)
    t.forward(60)
    my_goto(-32, 115)
    t.seth(-165)
    t.forward(60)


def mouth():
    my_goto(5, 148)
    t.setheading(270)
    t.forward(100)
    t.setheading(0)
    t.circle(120, 50)
    t.setheading(230)
    t.circle(-120, 100)


def scarf():
    t.fillcolor("#e70010")
    t.begin_fill()
    t.seth(0)
    t.forward(200)
    t.circle(-5, 90)
    t.forward(10)
    t.circle(-5, 90)
    t.forward(207)
    t.circle(-5, 90)
    t.forward(10)
    t.circle(-5, 90)
    t.end_fill()


def nose():
    my_goto(-10, 158)
    t.setheading(315)
    t.fillcolor("#e70010")
    t.begin_fill()
    t.circle(20)
    t.end_fill()


def black_eyes():
    t.setheading(0)
    my_goto(-20, 195)
    t.fillcolor("#000000")
    t.begin_fill()
    t.circle(13)
    t.end_fill()

    # second eye and white dot
    t.pensize(6)
    my_goto(20, 205)
    t.setheading(75)
    t.circle(-10, 150)
    t.pensize(3)

    # right eye
    my_goto(-17, 200)
    t.setheading(0)
    t.fillcolor("#ffffff")
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    my_goto(0, 0)


def face():
    t.forward(183)
    t.left(45)
    t.fillcolor("#ffffff")
    t.begin_fill()
    t.circle(120, 100)
    t.setheading(180)
    t.forward(121)
    t.pendown()
    t.setheading(215)
    t.circle(120, 100)
    t.end_fill()

    my_goto(63.56, 218.24)
    t.setheading(90)
    eyes()
    t.setheading(180)
    t.penup()
    t.forward(60)
    t.pendown()
    t.setheading(90)
    eyes()
    t.penup()
    t.setheading(180)
    t.forward(64)


def head():
    t.penup()
    t.circle(150, 40)
    t.pendown()
    t.fillcolor("#00a0de")
    t.begin_fill()
    t.circle(150, 280)
    t.end_fill()


def doraemon():
    head()
    scarf()
    face()
    nose()
    mouth()
    beard()

    my_goto(0, 0)
    t.setheading(0)
    t.penup()
    t.circle(150, 50)
    t.pendown()
    t.setheading(30)
    t.forward(40)
    t.setheading(70)
    t.circle(-30, 270)

    t.fillcolor("#00a0de")
    t.begin_fill()

    t.setheading(230)
    t.forward(80)
    t.setheading(90)
    t.circle(1000, 1)
    t.setheading(-89)
    t.circle(-1000, 10)

    t.setheading(180)
    t.forward(70)
    t.setheading(90)
    t.circle(30, 180)
    t.setheading(180)
    t.forward(70)

    t.setheading(100)
    t.circle(-1000, 9)

    t.setheading(-86)
    t.circle(1000, 2)
    t.setheading(230)
    t.forward(40)

    t.circle(-30, 230)
    t.setheading(45)
    t.forward(81)
    t.setheading(0)
    t.forward(203)
    t.circle(5, 90)
    t.forward(10)
    t.circle(5, 90)
    t.forward(7)
    t.setheading(40)
    t.circle(150, 10)
    t.setheading(30)
    t.forward(40)
    t.end_fill()

    t.seth(70)
    t.fillcolor('#ffffff')
    t.begin_fill()
    t.circle(-30)
    t.end_fill()

    my_goto(103.74, -182.59)
    t.seth(0)
    t.fillcolor('#ffffff')
    t.begin_fill()
    t.fd(15)
    t.circle(-15, 180)
    t.fd(90)
    t.circle(-15, 180)
    t.fd(10)
    t.end_fill()

    my_goto(-96.26, -182.59)
    t.seth(180)
    t.fillcolor('#ffffff')
    t.begin_fill()
    t.fd(15)
    t.circle(15, 180)
    t.fd(90)
    t.circle(15, 180)
    t.fd(10)
    t.end_fill()

    my_goto(-133.97, -91.81)
    t.seth(50)
    t.fillcolor('#ffffff')
    t.begin_fill()
    t.circle(30)
    t.end_fill()

    my_goto(-103.42, 15.09)
    t.seth(0)
    t.fd(38)
    t.seth(230)
    t.begin_fill()
    t.circle(90, 260)
    t.end_fill()

    my_goto(5, -40)
    t.seth(0)
    t.fd(70)
    t.seth(-90)
    t.circle(-70, 180)
    t.seth(0)
    t.fd(70)

    my_goto(-103.42, 15.09)
    t.fd(90)
    t.seth(70)
    t.fillcolor('#ffd200')

    t.begin_fill()
    t.circle(-20)
    t.end_fill()
    t.seth(170)
    t.fillcolor('#ffd200')
    t.begin_fill()
    t.circle(-2, 180)
    t.seth(10)
    t.circle(-100, 22)
    t.circle(-2, 180)
    t.seth(180-10)
    t.circle(100, 22)
    t.end_fill()
    t.goto(-13.42, 15.09)
    t.seth(250)
    t.circle(20, 110)
    t.seth(90)
    t.fd(15)
    t.dot(10)
    my_goto(0, -150)

    black_eyes()


if __name__ == '__main__':
    screen = Screen()
    screen.bgcolor("#f0f0f0")
    screen.setup(width=800, height=600)
    t.pensize(3)
    t.speed(9)
    doraemon()
    my_goto(100, -300)
    t.write("Pranav Elric", font=("Bradley Hand ITC", 30, "bold"))
    t.getscreen()._root.mainloop()
