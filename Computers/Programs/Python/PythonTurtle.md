# Python Turtle

## Install Turtle

```shell
pip3 install turtle
```



## Basic

### Canvas 画布

设置绘图区域

#### screensize( )

```python
# parameters
# width, height: 画布的宽和高的像素
# bg: 背景颜色
turtle.screensize(width, height, bg)

# examples
turtle.screensize(800, 600, "green")
```

#### setup( )

```python
# parameters
# width, height: 整数表示宽和高的像素；小数表示占据电脑屏幕的比例
# startx, starty: 矩形窗口左上角顶点的位置
turtle.setup(width, height, startx, starty)

# examples
turtle.setup(800, 600, 100, 100)
turtle.setup(0.6, 0.6)
```

### Pen 画笔

#### 画笔的属性

##### pensize( )

设置画笔的宽度

```python
turtle.pensize(10)
```



##### pencolor( )

设置画笔颜色

```python
turtle.pencolor('green')
rgb = (0.2, 0.8, 0.5)
turtle.pencolor(rgb)
```



##### speed( )

设置画笔移动速度

```python
# parameters
# speed: 画笔移动速度[0, 10],数字越大越快
turtle.speed(speed)

# examples
turtle.speed(5)
```



#### 绘图函数

##### 画笔运动

```python
turtle.forward(distance) # 向前移动distance像素
turtle.backward(distance)	# 向后移动distance像素
turtle.right(degree)	# 顺时针转动degree度数
turtle.left(desgree)	# 逆时针转动degree度数
turtle.pendown()	# 放下画笔
turtle.penup()	# 抬起画笔
turtle.goto(x, y)	# 将画笔移动到(x, y)的位置
turtle.circle()
turtle.write('text', align='center', font=('font_name', font_size, ))
```

##### 画笔控制

```python
turtle.fillcolor('color')	# 图形的填充色
turtle.color(pencolor, fillcolor)	# 设置画笔颜色，填充色
turtle.filling()	# 返回当前是否在填充状态
turtle.begin_fill()	# 开始填充
turtle.end_fill()	# 完成填充
turtle.hideturtle()	# 隐藏箭头
turtle.showturtle()	# 显示箭头
```

##### 全局控制

```python
turtle.clear()	# 清空画布，turtle的位置和状态不变
turtle.reset()	# 清空画布，重置turtle状态
turtle.undo()	# 撤销上一个动作
```



