import turtle
  
my_turtle = turtle.Turtle()

length = 50
angle = 90
Screen = turtle.Screen()
my_turtle.color('purple')
my_turtle.fd(length)
my_turtle.left(angle)
my_turtle.fd(length)
my_turtle.left(angle)
my_turtle.fd(length)
my_turtle.left(angle)
my_turtle.fd(length)
my_turtle.left(angle)
#done with the first rectangle
my_turtle.penup()
my_turtle.color('red')
#change pen color to red
my_turtle.forward(80)
#relocate the pen 30 units to the right
my_turtle.pendown()
#drawing a smaller red square
my_turtle.forward(20)
my_turtle.right(90)
my_turtle.forward(20)
my_turtle.right(90)
my_turtle.forward(20)
my_turtle.right(90)
my_turtle.forward(20)
my_turtle.right(90)