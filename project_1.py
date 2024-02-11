import turtle
window = turtle.Screen()
window.bgcolor("light blue")
pen = turtle.Turtle()

#ocean

pen.color("deep sky blue")
pen.pensize(10)
pen.up()
pen.begin_fill()
pen.goto(360,150)
pen.down()
pen.left(180)
pen.forward(722)
pen.left(90)
pen.forward(490)
pen.left(90)
pen.forward(722)
pen.left(90)
pen.forward(490)
pen.end_fill()

#sand

pen.color("wheat")
pen.up()
pen.begin_fill()
pen.goto(360,-250)
pen.left(90)
pen.down()
pen.forward(722)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(722)
pen.left(90)
pen.forward(100)
pen.end_fill()

#starfish

pen.color("violet")
pen.pensize(5)
pen.up()
pen.goto(-300,-280)
pen.begin_fill()
pen.left(20)
pen.down()
for i in range(5):
    pen.forward(20)
    pen.left(130)
    pen.forward(20)
    pen.right(60)
pen.end_fill()

pen.color("light yellow")
pen.up()
pen.goto(-100,-280)
pen.begin_fill()
pen.left(20)
pen.down()
for i in range(5):
    pen.forward(20)
    pen.left(130)
    pen.forward(20)
    pen.right(60)
pen.end_fill()

pen.color("violet")
pen.up()
pen.goto(150,-280)
pen.begin_fill()
pen.left(20)
pen.down()
for i in range(5):
    pen.forward(20)
    pen.left(130)
    pen.forward(20)
    pen.right(60)
pen.end_fill()

pen.color("light pink")
pen.up()
pen.goto(220,-280)
pen.begin_fill()
pen.left(20)
pen.down()
for i in range(5):
    pen.forward(20)
    pen.left(130)
    pen.forward(20)
    pen.right(60)
pen.end_fill()

#seaweed

pen.up()
pen.pensize(5)
pen.goto(-220,-250)
pen.color("green")
pen.down()
pen.right(20)
for i in range(6):
    pen.forward(20)
    pen.right(60)
    pen.forward(20)
    pen.left(60)
pen.up()
pen.color("light green")
pen.goto(-180,-250)
pen.down()
for i in range(6):
    pen.forward(20)
    pen.right(60)
    pen.forward(20)
    pen.left(60)
pen.up()
pen.color("green")
pen.goto(300,-250)
pen.down()
for i in range(6):
    pen.forward(20)
    pen.right(60)
    pen.forward(20)
    pen.left(60)

pen.up()
pen.color("light green")
pen.goto(-300,-250)
pen.down()
for i in range(6):
    pen.forward(20)
    pen.right(60)
    pen.forward(20)
    pen.left(60)

#fish

pen.up()
pen.pensize(5)
pen.right(20)
pen.color("orange")
pen.goto(-65,-60)
pen.down()
pen.begin_fill()
pen.circle(20)
pen.end_fill()
pen.begin_fill()
pen.right(60)
for i in range(3):
    pen.forward(20)
    pen.right(120)
pen.end_fill()

pen.up()
pen.goto(65,-170)
pen.down()
pen.color("pale violet red")
pen.left(60)
pen.begin_fill()
pen.circle(30)
pen.end_fill()
pen.begin_fill()
pen.right(60)
for i in range(3):
    pen.forward(35)
    pen.right(120)
pen.end_fill()

#eyes

pen.up()
pen.goto(-90,-58)
pen.pensize(2)
pen.color("black")
pen.begin_fill()
pen.circle(3)
pen.end_fill()

pen.up()
pen.goto(25,-166)
pen.pensize(2)
pen.color("black")
pen.begin_fill()
pen.circle(3)
pen.end_fill()

#bubbles

pen.up()
pen.goto(-115,-50)
pen.color("white")
pen.down()
pen.circle(5)
pen.up()
pen.goto(-100,-28)
pen.down()
pen.circle(7)
pen.up()
pen.goto(-120,-10)
pen.down()
pen.circle(9)

pen.up()
pen.goto(-5,-156)
pen.down()
pen.circle(5)
pen.up()
pen.goto(5,-130)
pen.down()
pen.circle(6)
pen.up()
pen.goto(-15,-115)
pen.down()
pen.circle(8)

#rock

pen.up()
pen.goto(200,-250)
pen.down()
pen.pensize(7)
pen.color("saddle brown")
pen.right(30)
pen.begin_fill()
pen.forward(50) 
pen.left(90)
pen.circle(50,180)
pen.right(270)
pen.forward(100)
pen.end_fill()

#sun

pen.up()
pen.goto(-180,300)
pen.down()
pen.pensize(3)
pen.color("orange", "yellow")
pen.begin_fill()
pen.left(90)
pen.circle(35)
pen.end_fill()

#clouds

pen.up()
pen.color("white")
pen.pensize(5)
pen.goto(210,240)
pen.down()
pen.begin_fill()
pen.forward(20)
pen.circle(20,180)
pen.right(180)
pen.circle(45,180)
pen.right(180)
pen.circle(30,180)
pen.forward(20)
pen.left(90)
pen.forward(190)
pen.end_fill()

#name

pen.up()
pen.goto(260,-330)
pen.color("black")
pen.down()
pen.write("Gazaal.Z , 2024")
window.exitonclick()