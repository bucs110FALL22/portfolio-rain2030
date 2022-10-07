import turtle
import random

window = turtle.screensize(canvwidth = 400, canvheight = 400,bg = "lightblue")
point1 = turtle.Turtle()
point1.color('red')
coin = ["Heads", "Tails"]
x = 0
y = 0
point1.goto(x,y)
while (x < 200 and y < 200 or y > -200 and x > -200 or y < 200 and x > -200 or y > -200 and x > 200):
  outcome = random.choice(coin)
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
  else:
    break
    #unreakable?? something is wrong here
    
    
