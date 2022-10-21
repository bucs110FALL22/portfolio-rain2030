import turtle
import pygame
import math
import random
window = turtle.Screen()
window.bgcolor('lightblue')
michelangelo = turtle.Turtle()
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')
michelangelo.up()
leonardo.up()
michelangelo.goto(-50,20)
leonardo.goto(-50,40)
michelangelo.pendown()
leonardo.pendown()
for turn in range(50):
  michelangelo.forward(random.randrange(1, 10,1))
  leonardo.forward(random.randrange(1, 10, 1))

michelangelo.up()
leonardo.up()
michelangelo.setposition(-50,20)
leonardo.setposition(-50,40)
turtle.clear()
window.exitonclick()

#Part B
pygame.init()
window = pygame.display.set_mode((500,500))

def drawShape(num_sides):
  coords = []
  offset = 200
  side_length = 60
  num_sides = num_sides

  for n in range(num_sides):
    thetha = (2.0 * math.pi * n) / num_sides
    x = side_length * math.cos(thetha) + offset
    y = side_length * math.sin(thetha) + offset
    coords.append([x,y])
    print(thetha)
    print('x=', x)
    print('y=', y)
  return coords



window.fill("white")
pygame.display.flip()
bg = 'green'

pygame.draw.polygon(window, bg, drawShape(3))
pygame.display.flip()
pygame.time.delay(150)
window.fill("white")
pygame.display.flip()
pygame.draw.polygon(window, bg, drawShape(4))
pygame.display.flip()
pygame.time.delay(150)
window.fill("white")
pygame.display.flip()
bg = 'red'
pygame.draw.polygon(window, bg, drawShape(6))
pygame.display.flip()
pygame.time.delay(150)
window.fill("white")
pygame.display.flip()
pygame.draw.polygon(window, bg, drawShape(9))
pygame.display.flip()
pygame.time.delay(150)
window.fill("white")
pygame.display.flip()
bg = 'yellow'
pygame.draw.polygon(window, bg, drawShape(360))
pygame.display.flip()
pygame.time.delay(150)
window.fill("white")
pygame.display.flip()