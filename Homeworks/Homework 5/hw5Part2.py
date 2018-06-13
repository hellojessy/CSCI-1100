import random

# CREATE FUNCTION MOVE TRAINER TO FIND POSITION
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



def run_one_simulation(grid, pr):
    
    
    '''
    runs the simulation and keeps track of the number of pokemon caught
    on each space in the grid. prob is the probability a pokemon will be caught
    at each turn
    '''
    
    positionC = [M//2, N//2]
    bounds = [M-1, N-1]
    turns = 1
    pokeTotal = 0
    
    while turns <= 250:
        (positionC, pokeFound) = move_trainer(positionC, bounds, pr)
        '''
        create loop to count pokemon caught since last turn
        and total pokemon throughout loop
        '''
        if pokeFound == 1:
            pokeTotal += 1
            grid[positionC[0]][positionC[1]] += 1
        
        turns+= 1
        
    return grid, pokeTotal
    
   
# READ INITIAL INPUTS FROM USER 
M = int(input('Enter the integer number of rows => '))
print(M)
N = int(input('Enter the integer number of cols => '))
print(N)
p = float(input('Enter the probability of finding a pokemon (<= 1.0) => '))
print(p) 
sim = int(input('Enter the number of simulations to run => '))
print(sim)



# CREATE SEED VALUE TO MATCH REQUIRED OUTPUT
seed_value = 10*M + N
random.seed(seed_value)


grid_count = []
for i in range(M):
    grid_count.append([0]*N)

    
# CREATE LOOP TO RUN FOR GIVEN SIMULATIONS
i = 0
pokeTotal = [0]*sim
pokeMax = 0
pokeMin = 0
simMax = 0
simMin = 0
while i < sim:
    #pokeTotal[i] = 0
    (grid_count, pokeTotal[i]) = run_one_simulation(grid_count, p)
    i += 1
    
    
# INITIALIZE VARIABLES    
grid_countS = ''
count = 0
minimum = grid_count[0][0]
maximum = grid_count[0][0]
for i in range(M):
    for j in range(N):
        grid_countS = grid_countS + str('{:4d}'.format(grid_count[i][j]))
        count += grid_count[i][j]
        
           
            
    grid_countS = grid_countS + ('\n')

print(grid_countS)
print('Total pokemon caught is', count)

print('Minimum pokemon caught was {} in simulation'.format(min(pokeTotal)))
print('Maximum pokemon caught was {} in simulation'.format(max(pokeTotal)))
print('Max number of pokemon caught on a space is {} which was'.format(maximum))