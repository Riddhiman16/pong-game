import turtle
import  pyglet
#import winsound

wn = turtle.Screen()
wn.title("pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

i=0
j=3
k = .1
turtle.clear()
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("red")
pen2.penup()
pen2.hideturtle()
pen2.goto(0, 0)
pen2.write("Start Game? y for yes... n for no".format(i), align="center", font=("courier", 30, "normal"))
def game():
    turtle.clear()
    l=pyglet.resource.media('Mario-coin-sound.mp3',streaming=False)
    w=pyglet.resource.media('death.mp3',streaming=False)
    l.play()
    #paddle1
    turtle.clear()
    pen2.clear()
    i = 0
    j = 10
    k = .01
    q = 1

    pad_a=turtle.Turtle()
    pad_a.speed(0)
    pad_a.shape("square")
    pad_a.shapesize(stretch_wid=5,stretch_len=1)
    pad_a.color("red")
    pad_a.penup()
    pad_a.goto(-350,0)

    #paddle2
    pad_b=turtle.Turtle()
    pad_b.speed(0)
    pad_b.shape("square")
    pad_b.shapesize(stretch_wid=5,stretch_len=1)
    pad_b.color("blue")
    pad_b.penup()
    pad_b.goto(350,0)

    #ball
    ball=turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("yellow")
    ball.penup()
    ball.goto(0,0)
    ball.dx=.3
    ball.dy=.3

    #pen
    pen= turtle.Turtle()
    pen.speed(0)
    pen.color("red")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    #pen.write("Score:",align="center",font=("courier",12,"normal"))

    #function
    def a_up():
        y = pad_a.ycor()
        y += 80
        pad_a.sety(y)
        turtle.clear()

    def a_down():
        y = pad_a.ycor()
        y -= 80
        pad_a.sety(y)
        turtle.clear()

    def b_up():
        y = pad_b.ycor()
        y += 80
        pad_b.sety(y)
        turtle.clear()

    def b_down():
        y = pad_b.ycor()
        y -= 80
        pad_b.sety(y)
        turtle.clear()

    #keyboard config
    wn.listen()
    wn.onkeypress(a_up,"w")
    wn.onkeypress(a_down,"s")
    wn.onkeypress(b_up,"Up")
    wn.onkeypress(b_down,"Down")

    #main game
    while True:
        wn.update()

        #ball move
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #bouncer
        if ball.ycor()>290:
            ball.sety(290)
            ball.dy*=-1
            l.play()

        if ball.ycor()<-290:
            ball.sety(-290)
            ball.dy*=-1
            l.play()

        #game over
        if ball.xcor()>390:
            ball.goto(0,0)
            w.play()
            ball.dx=.3
            ball.dx*=-1
            j=j-1
            k=0.1
            pen.clear()
            pen.write("Score:{} Life:{}".format(i, j), align="center", font=("courier",12, "normal"))

        if ball.xcor()<-390:
            w.play()
            ball.goto(0,0)
            ball.dx=.3
            ball.dx*=-1
            j=j-1
            k=0.1
            pen.clear()
            pen.write("Score:{} Life:{}".format(i,j), align="center", font=("courier",12, "normal"))

        #pad ball collision
        if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()< pad_b.ycor()+50 and ball.ycor()> pad_b.ycor()-50):
            l.play()
            i=i+1
            k = (k + 0.1)
            ball.dx*=-(1+k)
            pen.clear()
            pen.write("Score:{} Life:{}".format(i,j), align="center", font=("courier",12, "normal"))

        if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()< pad_a.ycor()+50 and ball.ycor()> pad_a.ycor()-50):
            l.play()
            i=i+1
            k = (k + 0.1)
            ball.dx*=-(1+k)
            pen.clear()
            pen.write("Score:{} Life:{}".format(i,j), align="center", font=("courier", 12, "normal"))

        if(j<1):
            turtle.clear()
            pen.clear()
            pen1 = turtle.Turtle()
            pen1.speed(0)
            pen1.color("red")
            pen1.penup()
            pen1.hideturtle()
            pen1.goto(0,0)
            turtle.clear()
            pen1.write(" Your Score is:{}".format(i),align="center",font=("courier", 30, "normal"))

wn.listen()
wn.onkeypress(game, "y")


#main game
while True:
    wn.update()