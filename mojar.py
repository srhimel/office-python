import turtle
import random
turtle.speed(1)
colors = ["black","blue","red","green","purple"]
for i in range(30):
    a = random.randint(-200,200)
    b = random.randint(-200,200)

    j = random.randint(0, len(colors)-1)
    turtle.dot(colors[j])
    turtle.setposition(a, b)
turtle.exitonclick()