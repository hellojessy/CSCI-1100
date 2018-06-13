class Bird(object):
    def __init__ (self, n, m, x0, y0, r0, dx, dy):
        self.name = n
        self.mass = m
        self.x = x0
        self.y = y0
        self.radius = r0
        self.vx = dx
        self.vy = dy
        
    def fly (self): # MAKES BIRDY FLY
        self.x += self.vx
        self.y += self.vy
        return(self.x, self.y)
    
    def collide_pig(self): # BIRDY COLLIDE WITH PIG, SPEED DECREASED
        self.vx = self.vx/2
    
    def collide_barrier(self): # BIRDY COLLIDE WITH BARRIER, SPEED = 0
        self.vx = 0
        self.vy = 0