import pygame
import time
import math
import turtle


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
