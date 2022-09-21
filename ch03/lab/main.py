import turtle #1. import modules
import random
from random import randint
import pygame
import math
import time

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here



for turn in range(30):
  michelangelo.down()
  leonardo.down()
  michelangelo.forward(randint(1,5))
  leonardo.forward(randint(1,5))
  michelangelo.up()
  leonardo.up()
  #-----------------------------------------
# PART B - complete part B here
michelangelo.ht()
leonardo.ht()
michelangelo.clear()
leonardo.clear()

pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((100, 100))
 
# Fill the scree with white color
window.fill((255, 255, 255))
turtle.fillcolor('orange')
turtle.begin_fill()
coords = []
num_sides = 360
side_length = 1
offset = 15
for nums in range(2):
  for nums in range(num_sides):
    theta = (2.0 * math.pi * nums / num_sides)
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    coords.append((x, y))
    turtle.pendown()
    turtle.forward(side_length)
    turtle.left(360/num_sides)
    pygame.time.wait(10)
  pygame.draw.polygon(window, "purple", coords)
  pygame.display.flip()
  turtle.clear()
  window.fill('black')
  num_sides = 3
  side_length = 30
num_sides = 4
for nums in range(2):
  for nums in range(num_sides):
    theta = (2.0 * math.pi * nums / num_sides)
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    coords.append((x, y))
    turtle.pendown()
    turtle.forward(side_length)
    turtle.left(360/num_sides)
    pygame.time.wait(10)
  pygame.draw.polygon(window, "purple", coords)
  pygame.display.flip()
  turtle.clear()
  window.fill('black')
  num_sides = 6
  side_length = 30
  
num_sides = 9
for nums in range(num_sides):
  theta = (2.0 * math.pi * nums / num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x, y))
  turtle.pendown()
  turtle.forward(side_length)
  turtle.left(360/num_sides)
  pygame.time.wait(10)
pygame.draw.polygon(window, "purple", coords)
pygame.display.flip()
turtle.clear()
window.fill('black')

  
pygame.display.flip()
