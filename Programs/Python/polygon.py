import turtle
import math

t = turtle.Turtle()
radius = 200
numberOfSides = 96
colors = ["red", "green", "blue"]

t.color("white")
t.setpos(0, 0-radius)
t.color("black")
t.circle(radius)

i = 0
for sides in range(3, numberOfSides, 3):
    angle = 360 / sides
    r = math.radians(angle/2)
    s = math.sin(r)
    chord = s * radius * 2

    t.color("white")
    t.setpos(0, radius)
    t.setheading(0)
    t.right(angle/2)

    i = i + 1
    t.color(colors[i%3])

    for j in range(sides):
        t.forward(chord)
        t.right(angle)
        
turtle.done()
