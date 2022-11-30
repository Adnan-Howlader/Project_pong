import pygame
from pygame import gfxdraw
import Line as line
##player 1 line info
px1=6
py1=2
px2=6
py2=100



##draw pixel function
def drawPixel(x, y):
    pygame.gfxdraw.pixel(screen, x, y, (255, 255, 255))


def draw_middle_line():
  ##first find the zone
   x1=350
   x2=350
   y1=0
   y2=500
   dx=x2-x1
   dy=y2-y1
   z=line.find_zone(dx,dy)
  
     ##convert to zone 0
   x1,y1=line.convert_to_zone0(z,x1,y1)
   x2,y2=line.convert_to_zone0(z,x2,y2)
       

   point=line.midPoint(x1,y1,x2,y2)

   for x,y in point:

     x,y=line.convert_original(z,x,y)
     drawPixel(x,y)

def draw_player1_line(x1,y1,x2,y2):
  ##first find the zone
   dx=x2-x1
   dy=y2-y1
   z=line.find_zone(dx,dy)
  
     ##convert to zone 0
   x1,y1=line.convert_to_zone0(z,x1,y1)
   x2,y2=line.convert_to_zone0(z,x2,y2)
       

   point=line.midPoint(x1,y1,x2,y2)

   for x,y in point:

     x,y=line.convert_original(z,x,y)
     drawPixel(x,y)

def draw_player2_line(x1,y1,x2,y2):
  ##first find the zone
   dx=x2-x1
   dy=y2-y1
   z=line.find_zone(dx,dy)
  
     ##convert to zone 0
   x1,y1=line.convert_to_zone0(z,x1,y1)
   x2,y2=line.convert_to_zone0(z,x2,y2)
       

   point=line.midPoint(x1,y1,x2,y2)

   for x,y in point:

     x,y=line.convert_original(z,x,y)
     drawPixel(x,y)




pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

##The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------

while carryOn:

    for event in pygame.event.get(): ##User did something
        if event.type==pygame.QUIT:
            carryOn=False

    

    screen.fill(BLACK)

    
    
    
    
    ##apply middle point algorithm
    draw_middle_line()

    ##draw player line
    
    
    draw_player1_line(px1,py1,px2,py2)

    ##if player 1 press up
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_UP and py1>0:
            py1=py1-2
            py2=py2-2
        if event.key==pygame.K_DOWN and py2<500:
            py1=py1+2
            py2=py2+2
    
  
  

    pygame.display.flip()

    clock.tick(60)


pygame.quit()



