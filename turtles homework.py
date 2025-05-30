import turtle
turtle.Screen().bgcolor("green")
t=turtle.Screen()
t.setup(400,300)
t.title("Let's create drawing: How to daw a Star")
#first triangle for the star
t=turtle.Turtle()
t.shape("circle")
t.color("white")
t.pensize(5)
t.fillcolor("yellow")

t.begin_fill()
t.forward(100) #base
t.left(120)
t.forward(100)

t.left(120)
t.forward(100)

t.penup()
t.right(150)
t.forward(50)
#second triangle for the star
t.pendown()
t.right(90)
t.forward(100)

t.right(120)
t.forward(100)

t.right(120)
t.forward(100)
t.end_fill()

turtle.done()