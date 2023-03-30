import turtle   # 使用turtle绘图库

t = turtle.Turtle() # 创建画笔

# 设置画笔速度
t.speed(0)
t.pensize(4)

# 设置画笔颜色为绿色
t.color("green")

# 移动画笔到画板底部
t.penup()
t.goto(0, -400)
t.pendown()

# 画第一朵花的花枝
t.left(90)
t.forward(200)

# 画第一朵花
t.penup()
t.forward(50)
t.left(90)
t.forward(60)
t.right(90)
t.pendown()
t.color("red")

for i in range(6):
  t.penup()
  t.circle(20, 60)
  t.pendown()
  t.left(120)
  t.forward(100)
  t.left(120)
  t.forward(100)
  t.left(120)

# 移动画笔到左边
t.penup()
t.goto(-100, -300)
t.right(90)
t.pendown()

# 画第二朵花枝
t.color("green")
t.left(90)
t.forward(200)

# 画第二朵花
t.penup()
t.forward(50)
t.left(90)
t.forward(60)
t.right(90)
t.pendown()
t.color("purple")

for i in range(6):
  t.penup()
  t.circle(20, 60)
  t.pendown()
  t.left(120)
  t.forward(100)
  t.left(120)
  t.forward(100)
  t.left(120)

# 移动画笔
t.penup()
t.goto(-50, 250)
t.pendown()

# 画太阳
t.color("red")
t.begin_fill()
for i in range(36):
  t.forward(50)
  t.backward(50)
  t.left(10)
t.end_fill()

# 移动画笔
t.penup()
t.goto(150, 200)
t.pendown()

# 画“1”
t.color("black")
t.forward(100)

#移动画笔
t.penup()
t.goto(170, 250)
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
turtle.done()   # 释放画笔
