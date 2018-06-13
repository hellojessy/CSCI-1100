class Ball(object):
    def __init__(self, x, y, dx, dy, radius, color):
        self.ball_x,self.ball_y = (x, y)    # initial location
        self.ball_radius = radius
        self.ball_dx,self.ball_dy = dx, dy   # the movement of the ball object
        self.ball_color = color
        
    def position(self):
        return((self.ball_x, self.ball_y))
    
    def move(self):
        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy
        
    def bounding_box(self):
        return(self.ball_x-self.ball_radius, self.ball_y-self.ball_radius, self.ball_x+self.ball_radius, self.ball_y+self.ball_radius)
    
    def get_color(self):
        return(self.ball_color)
    
    def some_inside(self,maxx, maxy):
        return(0 < self.ball_x + self.ball_radius and \
              self.ball_x - self.ball_radius < maxx and \
              0 < self.ball_y + self.ball_radius and \
              self.ball_y - self.ball_radius < maxy)
    
    def check_and_reverse(self, maxx, maxy):
        #print((self.ball_x + self.ball_radius),"\n")
        if (((self.ball_x + self.ball_radius) >= maxx) or ((self.ball_x - self.ball_radius) <= 0)):
            self.ball_dx *= -1
        elif(((self.ball_y + self.ball_radius) >= maxy) or ((self.ball_y - self.ball_radius) <= 0)):
            self.ball_dy *= -1
        else:
            return