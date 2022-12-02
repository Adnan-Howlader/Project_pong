

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





