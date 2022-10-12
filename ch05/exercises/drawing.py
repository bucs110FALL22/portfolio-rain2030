import turtle


def getRectangle():
  length = int(input("Enter length value: "))
  print(length)
  width = int(input("Enter width value: "))
  print(width)
  return length, width

def drawRectangle(turtle):
  length, width = getRectangle()
  turtle.goto(0,0)
  turtle.pendown()
  turtle.forward(length)
  turtle.right(90)
  turtle.forward(width)
  turtle.right(90)
  turtle.forward(length)
  turtle.right(90)
  turtle.forward(width)

def main():
  turtle1 = turtle.Turtle()
  window = turtle.Screen()
  window.bgcolor("green")
  drawRectangle(turtle1)
  window.exitonclick()

main()
