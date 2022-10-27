import turtle

pclength = 135 #pc frame length
pcwidth = 225 #pc frame width
pslength = 100 #powersupply length
pswidth = 20 #powersupply power button width
window = turtle.Screen()
window.bgcolor("white")

def cfspecs():
  cf = int(input("Enter color for the cooling fans (1-5): "))
  return cf

def drawfan(turtle):
  cf = cfspecs()
  if cf == 1:
    turtle.color("magenta")
    turtle.fillcolor("dark orchid")
  elif cf == 2:
    turtle.color("navy")
    turtle.fillcolor("medium blue")
  elif cf == 3:
    turtle.color("gold")
    turtle.fillcolor("red")
  elif cf == 4:
    turtle.color("lightgreen")
    turtle.fillcolor("forest green")
  elif cf == 5:
    turtle.color("black")
    turtle.fillcolor("indigo")
  for i in range (1,3):
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(25, 10)
    turtle.pendown()
    turtle.circle(35)
    turtle.end_fill()
    
  
def pcFrame(turtle):
  turtle.goto(-50,115)
  turtle.clear()
  turtle.fillcolor("royal blue")
  turtle.begin_fill()
  turtle.pendown()
  turtle.forward(pclength)
  turtle.right(90)
  turtle.forward(pcwidth)
  turtle.right(90)
  turtle.forward(pclength)
  turtle.right(90)
  turtle.forward(pcwidth)
  turtle.color("royal blue")
  turtle.end_fill()
  turtle.penup()
  turtle.fillcolor("light green")
  turtle.begin_fill()
  turtle.goto(65,95)
  turtle.pendown()
  turtle.forward(pswidth)
  turtle.right(90)
  turtle.forward(pswidth)
  turtle.right(90)
  turtle.forward(pswidth)
  turtle.right(90)
  turtle.forward(pswidth)
  turtle.end_fill()
  
def powersupply(turtle):
  turtle.penup()
  turtle.goto(-50, -100)
  turtle.pendown()
  turtle.fillcolor("orange")
  turtle.begin_fill()
  turtle.forward(pswidth)
  turtle.right(90)
  turtle.forward(pslength)
  turtle.right(90)
  turtle.forward(pswidth)
  turtle.right(90)
  turtle.pendown()
  turtle.end_fill()
  
def main():
  turtle1 = turtle.Turtle()
  turtle1.hideturtle()
  pcFrame(turtle1)
  drawfan(turtle1)
  powersupply(turtle1)
  window.exitonclick()

main()
