import turtle #1. import modules
import random
from random import randint
import pygame

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
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
 
# Fill the scree with white color
window.fill((255, 255, 255))
 
# Using draw.rect module of
# pygame to draw the outlined rectangle
pygame.draw.rect(window, (0, 0, 255),[100, 100, 400, 100], 2)

pygame.display.update()


window.exitonclick()
