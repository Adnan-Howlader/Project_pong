
##algorithm function
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