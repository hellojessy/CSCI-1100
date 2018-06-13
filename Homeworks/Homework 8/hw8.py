from Bird import *
from Pig import *
from Barrier import *
import math as m
'''
Create a simulation of Angry birds using the position and speeds
of moving objects and checking them for collisions with barriers
and pigs. The simulation should take place on a 1000x1000 size
board where the birds will move along a line, possibly interacting
with pigs or barriers. The user should be asked files to input for
each scenario needed.
'''
def convert_input_to_birdy(line):
    '''
    Parse the bird input to create a bird object.
    '''
    m = line.strip().split('|')
    name = m[0]
    mass = float(m[1])
    initX = float(m[2])
    initY = float(m[3])  
    radB = float(m[4])
    moveX = float(m[5])
    moveY = float(m[6])
   
    return Bird(name, mass, initX, initY, radB, moveX, moveY)

def convert_input_to_piggy(line):
    '''
    Parse the pig input to create pig object.
    '''
    m = line.strip().split('|')
    name = m[0]
    xCent = float(m[1])
    yCent = float(m[2])  
    radP = float(m[3])
    return Pig(name, xCent, yCent, radP)    

def convert_input_to_barrier(line):
    '''
    Parse the pig input to create pig object.
    '''
    m = line.strip().split('|')
    name = m[0]
    strength = float(m[1])
    xCent = float(m[2])  
    yCent = float(m[3])
    radBa = float(m[4])
    return Barrier(name, strength, xCent, yCent, radBa)

def build_bird_list(file_name):
    '''
    Create the bird list using object
    '''
    birdy = []
    for line in open(file_name):
        birdy.append(convert_input_to_birdy(line))
    return birdy

def build_pig_list(file_name):
    '''
    Create the pig list using object
    '''    
    piggy = []
    for line in open(file_name):
        piggy.append(convert_input_to_piggy(line))
    return piggy

def build_barrier_list(file_name):
    '''
    Create the barrier list using object
    '''    
    barriers = []
    for line in open(file_name):
        barriers.append(convert_input_to_barrier(line))
    return barriers

def totalV(x, y):
    '''
    Calculate total velocity of bird
    '''
    return(m.sqrt(x**2+y**2))


def intersect(x1, y1, x2, y2, r1, r2):
    '''
    Checks intersection of bird and pig or bird and barrier
    '''
    return(totalV(x2-x1, y2-y1) <= (r1 + r2))

if __name__ == '__main__':
    file_nameB = input('Enter the name of the bird file => ')
    print(file_nameB)
    file_nameP = input('Enter the name of the pig file => ')
    print(file_nameP)    
    file_nameBa = input('Enter the name of the barrier file => ')
    print(file_nameBa)    
    print()
    
    # PRINT INITIAL AMOUNTS OF BIRDS, PIGS, BARRIERS
    birdy = build_bird_list(file_nameB)
    print('There are', len(birdy), 'birds:')
    for line in birdy:
        print('    {}: ({},{})'.format(line.name, line.x, line.y))
    print()
        
    piggy = build_pig_list(file_nameP)
    print('There are', len(piggy), 'pigs:')
    for line in piggy:
        print('    {}: ({},{})'.format(line.name, line.x, line.y))
    print()
        
    barriers = build_barrier_list(file_nameBa)
    print('There are', len(barriers), 'barriers:')
    for line in barriers:
        print('    {}: ({},{})'.format(line.name, line.x, line.y))
    print()   
    
    # INITIALIZE STEPS (TIME) AND LENGTH OF LISTS
    steps = 0
    lenB = len(birdy)
    lenP = len(piggy)
    
    for b in birdy:
        stop = 0 # STOP SET TO 0 TO CHECK
        if lenP > 0: # IF THE LENGTH OF PIGGIES IS NOT 0, GO THROUGH LOOP
            dx = b.x
            dy = b.y     
            print('Time {}: {} starts at ({},{})'.format(steps, b.name, dx, dy))
            
            while (dx + b.radius <= 1000) and (dx - b.radius >= 0) and (dy + b.radius <= 1000) and (dy-b.radius >= 0) and lenP > 0: # CHECKING BOUNDARY CONDITIONS
                (dx, dy) = b.fly()    
                steps +=1
                for p in piggy:
                    if intersect(b.x, b.y, p.x, p.y, b.radius, p.radius): # IF THIS IS TRUE
                        print('Time {}: {} at ({:.1f},{:.1f}) pops {}'.format(steps, b.name, b.x, b.y, p.name))
                        piggy.remove(p) # REMOVE PIGGY FROM LIST OF PIGGIES
                        b.collide_pig() 
                        lenP -= 1 # DECREASE LENGTH OF PIGGY LIST
                        print('Time {}: {} at ({:.1f},{:.1f}) has (dx, dy) = ({:.1f},{:.1f})'.format(steps, b.name, b.x, b.y, b.vx, b.vy))
                        break # ONE PIGGY ALREADY CHECKED, DON'T HAVE TO CONTINUE CHECKING LIST
                    
                for ba in barriers: # CHECK TO SEE IF INTERSECTION WITH BARRIER
                    if intersect(b.x, b.y, ba.x, ba.y, b.radius, ba.radius):
                        strength = ba.collide_bird(b.mass, totalV(b.vx, b.vy)) 
                        b.collide_barrier()
                        if strength < 0:  # STRENGTH CANNOT BE NEGATIVE
                            strength = 0.0
                            print('Time {}: {} at ({:.1f},{:.1f}) hits {}, Strength {:.1f}'.format(steps, b.name, b.x, b.y, ba.name, strength))
                            print('Time {}: {} crumbles'.format(steps, ba.name))  # BARRIER CRUMBLES WHEN BARRIER 0
                            print('Time {}: {} at ({:.1f},{:.1f}) has (dx, dy) = ({:.1f},{:.1f})'.format(steps, b.name, b.x, b.y, b.vx, b.vy))   
                        else:
                            print('Time {}: {} at ({:.1f},{:.1f}) hits {}, Strength {:.1f}'.format(steps, b.name, b.x, b.y, ba.name, strength))
                        break
                    
                totalvB = totalV(b.vx, b.vy) 
                if totalvB < 6: # IF THE VELOCITY DROPS BELOW 6, BIRD STOPS
                    print('Time {}: {} at ({:.1f},{:.1f}) with speed {:.1f} stops'.format(steps, b. name, b.x, b.y, totalvB))
                    stop = True
                    break 
                
        if lenP <= 0:
            break
        if stop == 0: # IF CONDITION IS FALSE
            print('Time {}: {} at ({:.1f},{:.1f}) has left the game'.format(steps, b.name, dx, dy))
        lenB -=1   # DECREASE AMOUNT OF BIRDIES
        
    if lenP > lenB: # CHECK IF MORE BIRDIES OR PIGGIES LEFT
        print('Time {}: No more birds. The pigs win!'.format(steps)) 
        print('Remaining pigs:')
        for p in piggy:
            print(p.name) # PRINT REMAINING PIGGIES
    else:
        print('Time {}: All pigs are popped. The birds win!'.format(steps))