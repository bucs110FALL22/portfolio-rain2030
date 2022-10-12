import turtle
import random

window = turtle.screensize(canvwidth = 400, canvheight = 400,bg = "lightblue")
point1 = turtle.Turtle()
point1.color('red')
coin = ["Heads", "Tails"]
is_in_screen = True
x = 0
y = 0
point1.goto(x,y)
while is_in_screen:
  outcome = random.choice(coin)
  #x_range = wn.window_width()/2
  #y_range = wn.window_width()/2
  if (outcome == "Heads"):
    print(outcome)
    point1.left(90)
    point1.forward(20)
    x = point1.xcor()
    y = point1.ycor()
    print("(",x,",",y,")")
  elif(outcome == "Tails"):
    print(outcome)
    point1.right(90)
    point1.forward(20)
    x = point1.xcor()
    y = point1.ycor()
    print("(",x,",",y,")")
if abs(x) > 400 or abs(y)> 400:
  is_in_screen = False
    
    #unreakable?? something is wrong here
    
    
