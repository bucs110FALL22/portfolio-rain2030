import pygame
import random
import math
import time
# Initializing Pygame
pygame.init()
  
# Initializing surface
surface = pygame.display.set_mode((300,300))
window = pygame.display.get_window_size()
# Initialing Color
color = (102,205,170)
  
# Drawing Dart Board
pygame.draw.rect(surface, color, pygame.Rect(0, 0, window[0], window[1]))
hitbox = pygame.draw.circle(surface, 'yellow', ( window[0]/2, window[1]/2), window[0]/2)
pygame.draw.line(surface, 'black', (window[0]/2, 0),(window[0]/2, 300))
pygame.draw.line(surface, 'black', (0, window[1]/2),(300, window[1]/2))
pygame.display.flip()

#dart1coords= []

p1pt = 0
p2pt = 0
for i in range(5):
  x1 = random.randint(0,401)
  y1 = random.randint(0,301)
  set1 = pygame.draw.circle(surface,'blue',(x1,y1),3)
  #pygame.draw.circle(surface,'blue',dart1coords,5)
  pygame.time.wait(200)
  x2 = random.randint(0,401)
  y2 = random.randint(0,301)
  set2 = pygame.draw.circle(surface,'red',(x2,y2),3)
  pygame.display.flip()
  pygame.time.wait(200)
  set1_from_center = math.hypot(150-x1, 150-y1)
  set2_from_center = math.hypot(150-x2, 150-y2)
  if(set1_from_center < 150):
    p1pt +=1
    print("Player1 is on the board, current points:" + str(p1pt))
  else:
    p1pt = p1pt
    print("Player1 is off the board, current points:" + str(p1pt))
    
  if(set2_from_center < 150):
    p2pt +=1
    print("Player2 is on the board, current points:" + str(p2pt))
    
  else:
    p2pt = p2pt
    print("Player2 is off the board, current points:" + str(p2pt))

if (p2pt<p1pt):
  print("player1 wins!")
else:
  print("player2 wins!")
time.sleep(10)