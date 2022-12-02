import pygame
from pygame import gfxdraw
import Line as line
import numpy as np

##player 1 line info
p1x1=6
p1y1=2
p1x2=6
p1y2=100

##player 2 line info
p2x1=694
p2y1=0
p2x2=694
p2y2=100
up=False



##draw pixel function
def drawPixel(x, y):
    pygame.gfxdraw.pixel(screen, x, y, (255, 255, 255))

##circle functions
def midpoint(x0, y0, radius):
    d = 1-radius
    x = 0
    y = radius 
    zone_Conversion(x, y, x0, y0)
    while x < y:
        if d >= 0: 
            d = d + 2 * x - 2 * y + 5
            x = x + 1
            y = y - 1
        else:
            d = d + 2 * x + 3
            x = x + 1
        zone_Conversion(x, y, x0, y0)



def zone_Conversion(x, y, x0, y0):
    drawPixel(x + x0,y + y0)
    drawPixel(y + x0, x + y0)
    drawPixel(y + x0, -x + y0)
    drawPixel(x + x0, -y + y0)
    drawPixel(-x + x0, -y + y0)
    drawPixel(-y + x0, -x + y0)
    drawPixel(-y + x0, x + y0)
    drawPixel(-x + x0, y + y0)


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
    
    
    draw_player1_line(p1x1,p1y1,p1x2,p1y2)
    draw_player2_line(p2x1,p2y1,p2x2,p2y2)

    ##if player 1 press up
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_UP and p1y1>0:

            translation_matrix=np.array([[1,0,-2],[0,1,-2],[0,0,1]])
            coordinate_matrix=np.array([[p1y1],[p1y2],[1]])
            
            result=np.matmul(translation_matrix,coordinate_matrix)

            p1y1=result[0][0]
            p1y2=result[1][0]
            
            
           
           
        if event.key==pygame.K_DOWN and p1y2<500:


            translation_matrix=np.array([[1,0,2],[0,1,2],[0,0,1]])
            coordinate_matrix=np.array([[p1y1],[p1y2],[1]])
            
            result=np.matmul(translation_matrix,coordinate_matrix)

            p1y1=result[0][0]
            p1y2=result[1][0]
            
     ##computer ai

   
    if p2y1 <= 0: 
      up=False
    if p2y2 >= 500:
      up=True
    
    if up==False:
      translation_matrix=np.array([[1,0,3],[0,1,3],[0,0,1]])
      coordinate_matrix=np.array([[p2y1],[p2y2],[1]])
            
      result=np.matmul(translation_matrix,coordinate_matrix)

      p2y1=result[0][0]
      p2y2=result[1][0]
    else:
      translation_matrix=np.array([[1,0,-3],[0,1,-3],[0,0,1]])
      coordinate_matrix=np.array([[p2y1],[p2y2],[1]])
            
      result=np.matmul(translation_matrix,coordinate_matrix)

      p2y1=result[0][0]
      p2y2=result[1][0]
    ##draw circle

    midpoint(50, 50, 20)



     
    
 
    
    
           
  
      






            
     
            
    
  
  

    pygame.display.flip()

    clock.tick(60)


pygame.quit()



