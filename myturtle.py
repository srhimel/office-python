import turtle
turtle.shape("turtle")
turtle.speed(1)

for i in range(101):
    for j in range(5):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(3)
        turtle.pendown()
    turtle.left(90)

turtle.exitonclick()