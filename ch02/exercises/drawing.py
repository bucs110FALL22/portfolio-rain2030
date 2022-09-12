import turtle

new = turtle.Turtle()

sides = int(input("How many sides does this polygon you want to create"))

length = int(input("what is the length of this polygon's sides"))

for _ in range(sides):
    turtle.forward(length)
    turtle.right(360 / sides)