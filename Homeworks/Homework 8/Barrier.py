class Barrier(object ):
    def __init__ (self, n, strength, x0, y0, r0):
        self.name = n
        self.s = strength
        self.x = x0
        self.y = y0
        self.radius = r0
        
    def collide_bird(self, massB, totalV): # COLLIDE WITH BIRD, STRENGTH DECREASES
        self.s = self.s-(massB*(totalV**2))
        return(self.s)   