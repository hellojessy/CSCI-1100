import math as m

# CREATE A CLASS FOR POKEMON THAT PROVIDES METHODS NEEDED FOR 
# FINDING POKEMON HEALTH WHEN HIT BY A PLAYER
class Pokemon(object):
    def __init__(self, n, x0, y0, r0, h):
        self.name = n
        self.x = x0
        self.y = y0
        self.radius = r0
        self.health = h
        
    def hitF(self): # CHECKS IF HIT FULL (DIRECT HIT)
        if self.health >= 2:
            self.health -= 2
        else:
            self.health = 0 
        
    def hitP(self): # CHECKS IF HIT PARTIAL (AREA OF EFFECT)
        if self.health >= 1:
            self.health -= 1 
        else:
            self.health = 0

# CREATE PLAYERS IN CLASS FOR EASIER ACCESS TO PLAYER NAME, X, Y
class Players(object):
    def __init__(self, n, x0, y0):
        self.name = n
        self.x = x0
        self.y = y0

# CONVERT INPUT INTO READABLE INFORMATION
def convert_input_pokemon(line):
    m = line.strip().split('|')
    name   = m[0]
    x0     = int(m[1])
    y0     = int(m[2])
    rad    = int(m[3])
    health = int(m[4])
    
    return Pokemon(name, x0, y0, rad, health)

def convert_input_players(line):
    m = line.strip().split('|')
    name = m[0]
    x0 = int(m[1])
    y0 = int(m[2])
    
    return Players(name, x0, y0)

numP = 0
def pokes(file_name):
    pokemons = []
    playyy = []
    count = 0
    for line in open(file_name):
        if count == 0:
            numP = int(line) # COUNT NUMBER OF POKEMON BEING USED
            count += 1
            continue
        if count <= numP: # APPEND POKEMON TO A LIST FOR LENGTH OF POKEMON LIST
            pokemons.append(convert_input_pokemon(line))
            count += 1
        else:
            playyy.append(convert_input_players(line))
            count += 1
            
    return pokemons, playyy, numP

def calcDist(x, y): 
    return(float(m.sqrt(x**2+y**2)))

def distance(x1, y1, x2, y2): # CALCULATE DISTANCE BETWEEN POKEMON AND POKEBALL
    return(float(calcDist(x2-x1, y2-y1)))

def directHit(dist, rad): # CHECK IF DIRECT HIT (POKEBALL < RADIUS OF POKEMON)
    return(float(dist < rad))

def effectA(dist, rad): # CHECK IF EFFECT OF AREA (POKEBALL < RADIUS + 5)
    return(float(dist < (rad + 5) ))
    

if __name__ == '__main__':
    numP = 0
    fileIn = input('File name => ')
    print(fileIn)
    pokemons, playyy, numP = pokes(fileIn)
    
    # PRINT OUT GIVEN POKEMON WITH INITIAL LOCATION AND HEALTH
    for line in pokemons:
        print('{:>12}: ({},{},{}) Health: {}'.format(line.name, line.x, line.y, line.radius, line.health))
    print()
    caughtP = dict()
    
    for line in playyy:
        if line.name not in caughtP.keys():
            caughtP[line.name] = [0, [] ] # IF THE NAME IS NOT YET IN DICTIONARY
            
        hit = 0
        if numP <= 0: # CHECKS IF THERE ARE NO POKEMON LEFT
            break
        for loc in pokemons:
            if loc.health > 0: # SPECIAL CONDITION SO ONE POKEMON DOESNT GET CAPTURED TWICE
                
                # CHECK IF DIRECT HIT
                if directHit( distance( loc.x, loc.y, line.x, line.y ) , loc.radius):
                    loc.hitF()
                
                    if loc.health >= 0: # POKEMON STILL ALIVE AND BARELY BREATHING
                        hit = True
                        print('{} throws a pokeball to position ({}, {}) hits {}:'.format(line.name, line.x, line.y, loc.name))
                        print('{:>12}: ({},{},{}) Health: {}'.format(loc.name, loc.x, loc.y, loc.radius, loc.health))
                          
                    if loc.health == 0: # POKEMON IS CAUGHT
                        hit = True
                        print('{} is caught!'.format(loc.name))
                        numP -= 1
                        caughtP[line.name][0] += 1 # INCREASE AMOUNT OF POKEMON CAUGHT BY SINGLE PLAYER
                        caughtP[line.name][1].append(loc.name) # ADD NAME OF POKEMON CAUGHT BY PLAYER 
        
                # CHECK IF PARTIAL HIT    
                elif effectA (distance( loc.x, loc.y, line.x, line.y ) , loc.radius):
                    loc.hitP()
                    
                    if loc.health >= 0:
                        hit = True
                        print('{} throws a pokeball to position ({}, {}) hits {}:'.format(line.name, line.x, line.y, loc.name))
                        print('{:>12}: ({},{},{}) Health: {}'.format(loc.name, loc.x, loc.y, loc.radius, loc.health))
            
                    if loc.health == 0:
                        hit = True
                        print('{} is caught!'.format(loc.name))  
                        numP -= 1
                        caughtP[line.name][0] += 1 
                        caughtP[line.name][1].append(loc.name)                    
       
        # WHEN PLAYER MISSES POKEMON
        if hit == False:
            print('{} misses at ({}, {})'.format(line.name, line.x, line.y))
            
    # ALL POKEMON ARE CAUGHT    
    if numP == 0:
        print('\nAll pokemon caught, results:')
        
    # PLAYERS RUN OUT OF POKEBALLS, STILL POKEMON LEFT    
    else:
        print('\nPlayers run out of pokeballs, results:')
    
    # PRINT POKEMON CAUGHT BY PLAYERS
    for key in sorted(caughtP.keys()):
        print('{} caught {} pokemon'.format(key, caughtP[key][0]))
        for x in caughtP[key][1]:
            print('{:>12}'.format(x))