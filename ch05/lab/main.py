import pygame
import time

pygame.init()

display = pygame.display.set_mode((500,500))
display.fill("white")
max_val = 0
max_so_far = 0

def threenaddone(n):
    counter = 0
    while n != 1:
      #print(n,"count:",counter)
      if n % 2 == 0:        # n is even
        n = n // 2
        counter+=1   
      else:                 # n is odd
        n = n * 3 + 1
        counter += 1  
    #print(n,"count:",counter)  
    return counter
print("count:",threenaddone(101)) #print(4)

upper_limit = 20
iters = {}
start = 2

for i in range (start, upper_limit+1):
  count = threenaddone(i)
  iters[i] = count
print(iters)

for i in range (start, upper_limit+1):
  count = threenaddone(i)
  if count > max_so_far:
    max_so_far = count
    max_val = i
print("max value:",max_val,"max so far:",m```````````````````````````````````````````ax_so_far)
coordinates = list(iters.items())
pygame.draw.lines(display, 'black', False, coordinates)
font = pygame.font.SysFont('Arial',15)
maxsofar = str(max_so_far)
msg = display.blit(pygame.font.Font.render(font,"Max_so_far:",1,'black'),(300,20))
msg2 = display.blit(pygame.font.Font.render(font, maxsofar,1,'black'),(430,20))
pygame.display.flip()

time.sleep(1000)