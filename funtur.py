import turtle
turtle.color("red", "green")
turtle.speed(10)

def turtle_circle(height, degree1 , degree2):
    for i in range(20):
        for j in range(4):
            turtle.forward(height)
            turtle.left(degree1)
        turtle.left(degree2)
    turtle.exitonclick()

while True:
    heig = input("What is the height? : ")
    deg1 = input("What is the first degree? :")
    deg2 = input("What is the trird degree? :")

    heig = int(heig)
    deg1 = int(deg1)
    deg2 = int(deg2)
    turtle_circle(heig,deg1,deg2)


