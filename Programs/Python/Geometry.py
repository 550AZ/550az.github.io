# A graph with multiple geometric shapes
# This program draws a circle, a rectangle, and a hexagon
# on the screen.

import turtle

# Create a turtle named t
t = turtle.Turtle()

# Draw a circle
t.circle(50)

# Move to a new location
t.penup()
t.goto(100, 100)
t.pendown()

# Draw a rectangle
for i in range(2):
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)

# Move to a new location
t.penup()
t.goto(-100, 100)
t.pendown()

# Draw a hexagon
for i in range(6):
    t.forward(50)
    t.left(60)

# 移动画笔
t.penup()
t.goto(100, 300)
t.pendown()

# 画“2”
t.color("black")
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

# 移动画笔
t.penup()
t.goto(160, 300)
t.pendown()

# 画“0”
t.color("black")
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)

# 移动画笔
t.penup()
t.goto(220, 300)
t.pendown()

# 画“2”
t.color("black")
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

# 移动画笔
t.penup()
t.goto(280, 300)
t.pendown()

# 画“1”
t.color("black")
t.right(90)
t.forward(100)

#移动画笔
t.penup()
t.goto(340, 250)
t.pendown()

# 画“8”
for i in range(2):
  t.forward(50)
  t.right(90)
  t.forward(50)
  t.right(90)

for i in range(2):
  t.forward(-50)
  t.right(-90)
  t.forward(-50)
  t.right(-90)

t.hideturtle()  # 隐藏画笔

# Wait for the user to close the window
turtle.exitonclick()


turtle.done()   # 释放画笔
