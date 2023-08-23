#1.6绘制一个太阳花。
import turtle

turtle.pensize(2)
turtle.pencolor("yellow")
turtle.fillcolor("red")
turtle.begin_fill()

for _ in range(13):
    turtle.forward(200)
    turtle.right(166)
turtle.end_fill()
turtle.seth(to_angle=90)
turtle.pencolor("blue")
turtle.pensize()
turtle.circle(-100,360)


turtle.exitonclick()