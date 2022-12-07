import pygame
from pygame import gfxdraw
import Line as line
import numpy as np

##player 1 line info
p1x1=10
p1y1=2
p1x2=10
p1y2=100
player_1_score=0
##player 2 line info
p2x1=694
p2y1=2
p2x2=694
p2y2=100
up=False
player_2_score=0

##circle info
cx=60
cy=60
cr=10
vx=3
vy=3




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

    ##draw players line
    
    
    draw_player1_line(p1x1,p1y1,p1x2,p1y2)
    draw_player2_line(p2x1,p2y1,p2x2,p2y2)

    ##if player 1 press up
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_UP and p1y1>0:

            translation_matrix=np.array([[1,0,-3],[0,1,-3],[0,0,1]])
            coordinate_matrix=np.array([[p1y1],[p1y2],[1]])
            
            result=np.matmul(translation_matrix,coordinate_matrix)

            p1y1=result[0][0]
            p1y2=result[1][0]
            
            
           
           
        if event.key==pygame.K_DOWN and p1y2<500:


            translation_matrix=np.array([[1,0,3],[0,1,3],[0,0,1]])
            coordinate_matrix=np.array([[p1y1],[p1y2],[1]])
            
            result=np.matmul(translation_matrix,coordinate_matrix)

            p1y1=result[0][0]
            p1y2=result[1][0]
            
     ##computer ai

    
    if p2y1 <= 0: 
      up=False
    if p2y2 >= 500:
      up=True
    ##if up is true move up else move down
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


    ##draw circle ##initial stage
    
    midpoint(cx, cy, cr)
    circle_translation_matrix=np.array([[1,0,vx],[0,1,vy],[0,0,1]])
    circle_coordinate_matrix=np.array([[cx],[cy],[1]])
    result=np.matmul(circle_translation_matrix,circle_coordinate_matrix)
    cx=result[0][0]
    cy=result[1][0]

    ##if ball hit the ground
    if cy+cr>=500:
        vy=-vy
        vx=vx
    ##if ball hit the ceiling
    if cy+cr<=0:
        vy=-vy
        vx=vx
       
    ##if ball hit the left wall
    if cx+cr<=0 :
        vx=-vx
        vy=vy
        player_2_score+=1
        ##play sound
        pygame.mixer.music.load("sound.mp3")
        pygame.mixer.music.play()
     
    ##if ball hit the right wall
    if cx+cr>=700:
        vx=-vx
        vy=vy
        player_1_score+=1
        pygame.mixer.music.load("sound.mp3")
        pygame.mixer.music.play()
        


    ##if ball hit the player 1 line
    if (cx+cr<=23 and p1y1<=cy<=p1y2 ):

        vx=-vx
        vy=vy
    ##if ball hit player 2 line
    if ( cx+cr>=693 and p2y1<=cy<=p2y2 ):
      vx=-vx
      vy=vy
     
    
    if player_1_score==5:
      player_1_score=0
      player_2_score=0
      
      
      print("Congratualations You win")
      
    if player_2_score==5:
      player_2_score=0
      player_1_score=0
      

      print("You lose")



    ###Number Drawing Code
    def find_zone(dx, dy):
          if abs(dx) <= abs(dy):
              if dx >= 0 and dy >= 0:
                  return 1
              elif dx <= 0 and dy >= 0:
                  return 2
              elif dx >= 0 and dy <= 0:
                  return 6
              elif dx <= 0 and dy <= 0:
                  return 5
          else:
              if dx >= 0 and dy >= 0:
                  return 0
              elif dx <= 0 and dy >= 0:
                  return 3
              elif dx >= 0 and dy <= 0:
                  return 7
              elif dx <= 0 and dy <= 0:
                  return 4

    def convert_to_zone0(z, x, y):
   
        if z==0:

            return x, y
        elif z==1:
            return y, x
        elif z==2:
            return y, -x
        elif z==3:
            return -x, y
        elif z==4:
            return -x, -y
        elif z==5:
            return -y, -x
        elif z==6:
            return -y, x
        elif z==7:
            return x, -y

    def convert_original(z, x, y):
        if z==0:
            return x, y
        elif z==1:
            return y, x
        elif z==2:
            return -y, x
        elif z==3:
            return -x, y
        elif z==4:
            return -x, -y
        elif z==5:
            return -y, -x
        elif z==6:
            return y, -x
        elif z==7:
            return x, -y

    def midPoint(X1,Y1,X2,Y2):
          # calculate dx & dy
          dx = X2 - X1
          dy = Y2 - Y1
          points=[]
       
          # initial value of decision parameter d
          d = dy - (dx/2)
          x = X1
          y = Y1
       
          # Plot initial given point
          # putpixel(x,y) can be used to print pixel
          # of line in graphics
         
          # iterate through value of X
          while (x < X2):
              x=x+1
              # E or East is chosen
              if(d <= 0):
                  d = d + dy
       
              # NE or North East is chosen
              else:
                  d = d + (dy - dx)
                  y=y+1
           
       
              # Plot intermediate points
              # putpixel(x,y) is used to print pixel
              # of line in graphics
              points.append((x,y))
          return points

    
    
    def first_num_left_right_first_line():
        ##first find the zone
         x1=-100+300
         x2=0+300
         y1=200
         y2=200
         dx=x2-x1
         dy=y2-y1
         z=find_zone(dx,dy)
        
           ##convert to zone 0
         x1,y1=convert_to_zone0(z,x1,y1)
         x2,y2=convert_to_zone0(z,x2,y2)
             
      
         point=midPoint(x1,y1,x2,y2)
      
         for x,y in point:
      
           x,y=convert_original(z,x,y)
           drawPixel(x,y)
            
             
      
        
       
      
    def first_num_up_down_right_side():
        x1=0+300
        y1=200
      
        x2=0+300
        y2=130
      
        dx=x2-x1
        dy=y2-y1
        z=find_zone(dx,dy)
        
           ##convert to zone 0
        x1,y1=convert_to_zone0(z,x1,y1)
        x2,y2=convert_to_zone0(z,x2,y2)
             
      
        point=midPoint(x1,y1,x2,y2)
      
        for x,y in point:
      
           x,y=convert_original(z,x,y)
           drawPixel(x,y)
      
      
    def first_num_left_right_second_line():
        ##first find the zone
         x1=-100+300
         x2=0+300
         y1=130
         y2=130
         dx=x2-x1
         dy=y2-y1
         z=find_zone(dx,dy)
        
           ##convert to zone 0
         x1,y1=convert_to_zone0(z,x1,y1)
         x2,y2=convert_to_zone0(z,x2,y2)
             
      
         point=midPoint(x1,y1,x2,y2)
      
         for x,y in point:
      
           x,y=convert_original(z,x,y)
           drawPixel(x,y)
      
      
    def first_num_up_down_left_side():
        x1=-100+300
        y1=200
      
        x2=-100+300
        y2=130
      
        dx=x2-x1
        dy=y2-y1
        z=find_zone(dx,dy)
        
           ##convert to zone 0
        x1,y1=convert_to_zone0(z,x1,y1)
        x2,y2=convert_to_zone0(z,x2,y2)
             
      
        point=midPoint(x1,y1,x2,y2)
      
        for x,y in point:
      
           x,y=convert_original(z,x,y)
           drawPixel(x,y)
      
      
    def first_num_up_down_left_side2():
        x1=-100+300
        y1=130
      
        x2=-100+300
        y2=60
      
        dx=x2-x1
        dy=y2-y1
        z=find_zone(dx,dy)
        
           ##convert to zone 0
        x1,y1=convert_to_zone0(z,x1,y1)
        x2,y2=convert_to_zone0(z,x2,y2)
             
      
        point=midPoint(x1,y1,x2,y2)
      
        for x,y in point:
      
           x,y=convert_original(z,x,y)
           drawPixel(x,y)
      
      
      
      
    def first_num_up_down_right_side2():
        x1=0+300
        y1=130
      
        x2=0+300
        y2=60
      
        dx=x2-x1
        dy=y2-y1
        z=find_zone(dx,dy)
        
           ##convert to zone 0
        x1,y1=convert_to_zone0(z,x1,y1)
        x2,y2=convert_to_zone0(z,x2,y2)
             
      
        point=midPoint(x1,y1,x2,y2)
      
        for x,y in point:
      
           x,y=convert_original(z,x,y)
           drawPixel(x,y)
      
      
    def first_num_left_right_3rd_line():
      ##first find the zone
       x1=-100+300
       x2=0+300
       y1=60
       y2=60
       dx=x2-x1
       dy=y2-y1
       z=find_zone(dx,dy)
      
         ##convert to zone 0
       x1,y1=convert_to_zone0(z,x1,y1)
       x2,y2=convert_to_zone0(z,x2,y2)
           
    
       point=midPoint(x1,y1,x2,y2)
    
       for x,y in point:
    
         x,y=convert_original(z,x,y)
         drawPixel(x,y)
    
       
    
    
    
    
    
    
    
    ##second number mid point algo
         
    def second_num_left_right_first_line():
      ##first find the zone
       x1=100+350
       x2=200+350
       y1=200
       y2=200
       dx=x2-x1
       dy=y2-y1
       z=find_zone(dx,dy)
      
         ##convert to zone 0
       x1,y1=convert_to_zone0(z,x1,y1)
       x2,y2=convert_to_zone0(z,x2,y2)
           
    
       point=midPoint(x1,y1,x2,y2)
    
       for x,y in point:
    
         x,y=convert_original(z,x,y)
         drawPixel(x,y)
          
           
    
      
     
    
    def second_num_up_down_right_side():
      x1=200+350
      y1=200
    
      x2=200+350
      y2=130
    
      dx=x2-x1
      dy=y2-y1
      z=find_zone(dx,dy)
      
         ##convert to zone 0
      x1,y1=convert_to_zone0(z,x1,y1)
      x2,y2=convert_to_zone0(z,x2,y2)
           
    
      point=midPoint(x1,y1,x2,y2)
    
      for x,y in point:
    
         x,y=convert_original(z,x,y)
         drawPixel(x,y)
    
    
    def second_num_left_right_second_line():
      ##first find the zone
       x1=100+350
       x2=200+350
       y1=130
       y2=130
       dx=x2-x1
       dy=y2-y1
       z=find_zone(dx,dy)
      
         ##convert to zone 0
       x1,y1=convert_to_zone0(z,x1,y1)
       x2,y2=convert_to_zone0(z,x2,y2)
           
    
       point=midPoint(x1,y1,x2,y2)
    
       for x,y in point:
    
         x,y=convert_original(z,x,y)
         drawPixel(x,y)
    
    
    def second_num_up_down_left_side():
      x1=100+350
      y1=200
    
      x2=100+350
      y2=130
    
      dx=x2-x1
      dy=y2-y1
      z=find_zone(dx,dy)
      
         ##convert to zone 0
      x1,y1=convert_to_zone0(z,x1,y1)
      x2,y2=convert_to_zone0(z,x2,y2)
           
    
      point=midPoint(x1,y1,x2,y2)
    
      for x,y in point:
    
         x,y=convert_original(z,x,y)
         drawPixel(x,y)
    
    
    def second_num_up_down_left_side2():
      x1=100+350
      y1=130
    
      x2=100+350
      y2=60
    
      dx=x2-x1
      dy=y2-y1
      z=find_zone(dx,dy)
      
         ##convert to zone 0
      x1,y1=convert_to_zone0(z,x1,y1)
      x2,y2=convert_to_zone0(z,x2,y2)
           
    
      point=midPoint(x1,y1,x2,y2)
    
      for x,y in point:
    
         x,y=convert_original(z,x,y)
         drawPixel(x,y)
    
    
    
    
    def second_num_up_down_right_side2():
      x1=200+350
      y1=130
    
      x2=200+350
      y2=60
    
      dx=x2-x1
      dy=y2-y1
      z=find_zone(dx,dy)
      
         ##convert to zone 0
      x1,y1=convert_to_zone0(z,x1,y1)
      x2,y2=convert_to_zone0(z,x2,y2)
           
    
      point=midPoint(x1,y1,x2,y2)
    
      for x,y in point:
    
         x,y=convert_original(z,x,y)
         drawPixel(x,y)
    
    
    def second_num_left_right_3rd_line():
      ##first find the zone
       x1=100+350
       x2=200+350
       y1=60
       y2=60
       dx=x2-x1
       dy=y2-y1
       z=find_zone(dx,dy)
      
         ##convert to zone 0
       x1,y1=convert_to_zone0(z,x1,y1)
       x2,y2=convert_to_zone0(z,x2,y2)
           
    
       point=midPoint(x1,y1,x2,y2)
    
       for x,y in point:
    
         x,y=convert_original(z,x,y)
         drawPixel(x,y)

    
  
      




  
      
 

    







   
  

  
  
         

    






          
   
          
  



    def draw_first(n):
        if n==0:
             
              first_num_left_right_first_line()
              first_num_up_down_right_side()
              
              first_num_up_down_left_side()
              first_num_up_down_left_side2()
              first_num_up_down_right_side2()
              first_num_left_right_3rd_line()
        elif n==1:
              
              first_num_up_down_right_side()
             
              
              first_num_up_down_right_side2()
        
        elif n==5:
    
              first_num_left_right_first_line()
              first_num_up_down_right_side()
              first_num_left_right_second_line()
              
              first_num_up_down_left_side2()
              
              first_num_left_right_3rd_line()
    
        
        elif n==3:
          first_num_left_right_first_line()
          first_num_up_down_right_side()
          first_num_left_right_second_line()
         
          
          first_num_up_down_right_side2()
          first_num_left_right_3rd_line()
        elif n==4:
    
              
              first_num_up_down_right_side()
              first_num_left_right_second_line()
              first_num_up_down_left_side2()
             
              first_num_up_down_right_side2()
        elif n==2:
              first_num_left_right_first_line()
              
              first_num_left_right_second_line()
              first_num_up_down_left_side()
              
              first_num_up_down_right_side2()
              first_num_left_right_3rd_line()
        
             
         
      
    def draw_last(n):
      if n==0:
           
            second_num_left_right_first_line()
            second_num_up_down_right_side()
            
            second_num_up_down_left_side()
            second_num_up_down_left_side2()
            second_num_up_down_right_side2()
            second_num_left_right_3rd_line()
      elif n==1:
            
            second_num_up_down_right_side()
           
            
            second_num_up_down_right_side2()
      
      elif n==5:
  
            second_num_left_right_first_line()
            second_num_up_down_right_side()
            second_num_left_right_second_line()
            
            second_num_up_down_left_side2()
            
            second_num_left_right_3rd_line()
  
      
      elif n==3:
        second_num_left_right_first_line()
        second_num_up_down_right_side()
        second_num_left_right_second_line()
       
        
        second_num_up_down_right_side2()
        second_num_left_right_3rd_line()
      elif n==4:
  
            
            second_num_up_down_right_side()
            second_num_left_right_second_line()
            second_num_up_down_left_side2()
           
            second_num_up_down_right_side2()
      elif n==2:
            second_num_left_right_first_line()
            
            second_num_left_right_second_line()
            second_num_up_down_left_side()
            
            second_num_up_down_right_side2()
            second_num_left_right_3rd_line()
      
           
       
  

    draw_first(player_1_score)
    draw_last(player_2_score)
  
   
      
  
      
      
    pygame.display.flip()

    clock.tick(60)


pygame.quit()



