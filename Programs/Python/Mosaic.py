
# Import turtle module
import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(0)

# Set the color of the turtle
t.color("black")

# Move the turtle to the left
t.penup()
t.goto(-200, 0)
t.pendown()

# Draw the hull of the ship
t.begin_fill()
t.fillcolor("brown")
t.forward(400)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.left(90)
t.forward(200)
t.left(90)
t.forward(50)
t.right(90)
t.forward(100)
t.left(90)
t.forward(50)
t.end_fill()

# Draw the mast of the ship
t.penup()
t.goto(-50, 50)
t.pendown()
t.begin_fill()
t.fillcolor("black")
t.left(90)
t.forward(150)
t.right(90)
t.forward(10)
t.right(90)
t.forward(150)
t.end_fill()

# Draw the sail of the ship
t.penup()
t.goto(-40, 200)
t.pendown()
t.begin_fill()
t.fillcolor("white")
t.right(135)
t.forward(100)
t.left(135)
t.forward(70)
t.left(135)
t.forward(100)
t.end_fill()

# Draw the flag of the ship
t.penup()
t.goto(-40, 200)
t.pendown()
t.begin_fill()
t.fillcolor("red")
t.left(45)
t.forward(30)
t.right(90)
t.forward(15)
t.right(90)
t.forward(30)
t.end_fill()

# Hide the turtle
turtle.hideturtle()

# Keep the window open until the user closes it
turtle.done()
