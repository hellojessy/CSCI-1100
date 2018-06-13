import hw4_util

# Function to read pokemon list and coordinates given to each pokemon
# Prints out list of pokemon with coordinates
def print_pokemon(pokemon, coord):
    i = 0
    print('Current pokemon:')
    for i in range(len(pokemon)):
        print(' ' * 4, pokemon[i], 'at', coord[i])
    i += 1

# Function to complete movement of pokemon trainer around the field
def move(x, y, direction): 
    if direction == 'n':
        if y - 1 < 0:
            y = 0
        else:
            y -= 1        
    elif direction == 's':
        if y + 1 > 11:
            y = 11
        else:
            y += 1
    elif direction == 'e':
        if x + 1 > 11:
            x = 11
        else:
            x += 1
    elif direction == 'w':
        if x - 1 < 0:
            x = 0
        else:
            x -= 1
    return [x,y]

# Read file to obtain pokemon
currentPokemon, locations = hw4_util.read_pokemon()

# Initialize variables
x1 = 5
y1 = 5
command = 0
count = 0

# Print list of current pokemon
print_pokemon(currentPokemon, locations)
print()


while command != 'end': # Go through conditions if input does not equal false
    command = input("N,S,E,W to move, 'print' to list, or 'end' to stop ==> ")
    print (command)
    command = command.lower()
    if command != 'end':
        if command == 'print':
            print_pokemon(currentPokemon, locations)
            print()
            print('Currently at {}'.format((x1,y1)))
        else:
            [x1,y1] = move(x1, y1, command)
            print('Currently at {}'.format((x1,y1)))
            i = 0
            while i in range(len(locations)):
                '''
                Check if pokemon exists in the given list, if already 
                caught, remove it from the list and print what is left
                If new pokemon being caught, print out which turn caught on
                '''
                if ((x1 == locations[i][0]) and (y1 == locations[i][1])):
                    print('You capture a', currentPokemon[i], 'on turn', count)
                    currentPokemon.remove(currentPokemon[i]) 
                    locations.remove(locations[i])
                i += 1  
    count += 1