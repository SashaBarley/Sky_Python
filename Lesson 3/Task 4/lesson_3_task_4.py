from turtle import *

t = Turtle()

t.screen.setup(800, 800)
t.speed(0)

def p(n):
    for i in range(n):
        t.fillcolor("black")
        t.begin_fill()
        t.circle(15) 
        t.end_fill()
        t.left(360 / n)
        t.fd(50)
    

# туловище
t.fillcolor("red")
t.begin_fill()
t.circle(90)
t.end_fill() 

t.up()
t.goto(0,157)
t.setheading(157)
p(8)


# голова
t.goto(45,180)
t.setheading(180)
t.down()
t.fd(90)

t.right(270)
t.begin_fill()
t.circle(45, -180)
t.end_fill() 

t.screen.exitonclick()
t.screen.mainloop()