import turtle
#Import random module to use random methods
import random

#drawSquare method to draw square
def drawSquare(myturtle, width, top_left_x, top_left_y):
  myturtle.up()
  myturtle.goto(top_left_x,top_left_y)
  myturtle.down()
  drawLine (myturtle,top_left_x, top_left_y,top_left_x+width, top_left_y)
  drawLine (myturtle,top_left_x,top_left_y,top_left_x,top_left_y-width)
  drawLine (myturtle,top_left_x, top_left_y-width, top_left_x+width, top_left_y-width)
  drawLine (myturtle,top_left_x-width, top_left_y-width, top_left_x+width, top_left_y)
  myturtle.up()

#drawLine method to draw line from one position to another
def drawLine(myturtle, x_start, y_start, x_end, y_end):
  myturtle.up ()
  myturtle.goto(x_start,y_start)
  myturtle.down ()
  myturtle.goto(x_end, y_end)
  myturtle.up ()

#drawCircle to draw circle inside square
def drawCircle(myturtle, radius):
  myturtle.goto(0,-1)
  myturtle.down()
  myturtle.circle (radius)

def setUpDartboard(wn,myturtle):
  wn.setworldcoordinates (-2.5,-2.5,2.5,2.5)
  myturtle.down()
  #Draw the square with 2units side
  drawSquare (myturtle,2,-1,1)
  #Draw circle with 1 unit radius
  drawCircle (myturtle, 1)

def throwDart (myturtle) :
  myturtle.up()
  #Go to the center
  myturtle.goto (0,0)
  #Random number between -1 to 1 for xpos and ypos
  x=round (random. uniform (-1,1) ,5)
  y=round (random. uniform (-1,1) ,5)
  #I£ the point is in circle use color blue
  if isInCircle(myturtle, x,y):
    myturtle.goto (x,y)
    myturtle.dot ("blue")
    return True
#Else use color red
  else:
    myturtle.goto (x,y)
    myturtle.dot ("red")
    return False

#Check the point is in circle
def isInCircle(myturtle,x,y):
#Check if the distance is less than 1
  if myturtle.distance (x,y) <1:
    #Return True
    return True
#Return False
  return False

def playDarts(myturtle):
#To store the scores
  player_scores=[0,0]
#For 2 players
  for i in range(2):
  #Each 10 rounds
    for j in range(10):
      if (throwDart (myturtle)):
        player_scores[i]=player_scores[i]+1
#I£ player 1 scores more than player 2
  if player_scores[0]>player_scores[1]:
    print ("Playerl won")
  else:
    print ("Player2 won")

def montePi(myturtle,number_darts):
  inside_count=0
  for i in range (number_darts):
    if (throwDart (myturtle)):
      inside_count+=1
  return inside_count

def main():
  print("This is a program that simulates throwing darts at a dartboard\n" \
  "in order to approximate pi: The ratio of darts in a unit circle\n"\
  "to the total number of darts in a 2X2 square should be\n"\
  "approximately equal to pi/4")
  print(" = Part A = ")
  window = turtle.Screen()
  darty = turtle.Turtle()
  darty.speed(0) # as fast as it will go!
  setUpDartboard (window, darty)
# Loop for 10 darts to test your code
  for i in range(10):
    throwDart (darty)
  print ("Part A Complete")
  print (" = Part B= ")
  darty.clear()
  setUpDartboard (window, darty)
  playDarts (darty)
  print ("Part B Complete...")
  # Keep the window up until dismissed
  print ("Part C")
  darty.clear()
  setUpDartboard (window, darty)
# Includes the following code in order to update animation periodically
# instead of for each throw (saves LOTS of time):
  BATCH_OF_DARTS = 5000
  window. tracer(BATCH_OF_DARTS)
  number_darts = int (input("Please input the number of darts to be thrown in the             simulation: "))
  approx_pi = montePi(darty, number_darts)
  print("The estimation of pi using" +str(number_darts)+" virtual darts is "+str(approx_pi))
  print("Part C Complete...")
  window. exitonclick()
main ()
