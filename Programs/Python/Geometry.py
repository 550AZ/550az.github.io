# A graph with multiple geometric shapes
# This program draws a circle, a rectangle, and a hexagon
# on the screen.

import turtle

# Create a turtle named tom
tom = turtle.Turtle()

# Draw a circle
tom.circle(50)

# Move to a new location
tom.penup()
tom.goto(100, 100)
tom.pendown()

# Draw a rectangle
for i in range(2):
    tom.forward(100)
    tom.left(90)
    tom.forward(50)
    tom.left(90)

# Move to a new location
tom.penup()
tom.goto(-100, 100)
tom.pendown()

# Draw a hexagon
for i in range(6):
    tom.forward(50)
    tom.left(60)

# Wait for the user to close the window
turtle.exitonclick()

# Save the image to a file
# turtle.getscreen().getcanvas().postscript(file="geometry.eps")

# Save the image to a file
# turtle.getscreen().getcanvas().postscript(file="geometry.eps")
