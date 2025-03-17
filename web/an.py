import turtle

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Red Heart Drawing")

pen = turtle.Turtle()
pen.color("red")
pen.pensize(3)

pen.begin_fill()

pen.left(50)
pen.forward(133)
pen.circle(50, 200)
pen.right(140)
pen.circle(50, 200)
pen.forward(133)

pen.end_fill()

pen.hideturtle()

wn.mainloop()
