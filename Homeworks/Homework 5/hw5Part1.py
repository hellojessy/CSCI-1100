import random

'''
Create a function that uses:
position - (row, col) passed as tuple
bounds - (rows, cols) passed as a tuple
prob - probability that pokemon will be found at current position
'''

def move_trainer(position, bounds, prob):
    a = random.randint(0, 3)
    pokemon = 0
    if a == 0:
        if position[0] - 1 < 0:
            position[0] = 0
        else:
            position[0] -= 1
    elif a == 1:
        if position[0] + 1 > bounds[0]:
            position[0] = bounds[0]
        else:
            position[0] += 1
    elif a == 2:
        if position[1] + 1 > bounds[1]:
            position[1] = bounds[1]
        else:
            position[1] += 1
    elif a == 3:
        if position[1] -1 < 0:
            position[1] = 0
        else:
            position[1] -= 1
            
    # ADD RANDOM.RANDOM TO CHECK PROBABILITY OF CATCHING POKEMON
    if random.random() <= prob:
        pokemon = 1
    else:
        pokemon = 0   
        
    return position, pokemon

# READ INITIAL INPUTS FROM USER            
M = int(input('Enter the integer number of rows => '))
print(M)
N = int(input('Enter the integer number of cols => '))
print(N)
p = float(input('Enter the probability of finding a pokemon (<= 1.0) => '))
print(p) 

# SET CURRENT POSITION INITIAL
positionC = [M//2, N//2]

# SET BOUNDS FOR GRID
bounds = [M-1, N-1]

# CREATE SEED VALUE TO MATCH REQUIRED OUTPUT
seed_value = 10*M + N
random.seed(seed_value)

# INITIALIZE VARIABLES
turns = 1
pokeCaught = 0
pokeTotal = 0

# CREATE LOOP TO RUN FOR 250 TERMS
while turns <= 250:
    (positionC, pokeFound) = move_trainer(positionC, bounds, p)
    '''
    create loop to count pokemon caught since last turn
    and total pokemon throughout loop
    '''
    if pokeFound == 1:
        pokeCaught += 1
        pokeTotal += 1
    
    if turns % 20 == 0 and turns != 0:
        print('Time step {}: position ({}, {}) pokemon caught \
since the last report {}'.format(turns, positionC[0], positionC[1], pokeCaught))
        pokeCaught = 0
        
    turns+= 1
    
    
print('After 250 time steps the trainer ended at position ({}, {}) with {} \
pokemon.'.format(positionC[0], positionC[1], pokeTotal))