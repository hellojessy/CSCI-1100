i = 0
x = 200
y = 200
direction = 'right'
command = []


# Function to create movement of turtle
def move(x, y, direction, amount):
    if direction == 'right':
        if x + amount > 400:
            x = 400
        else:
            x += amount
        
    elif direction == 'left':
        if x - amount < 0:
            x = 0
        else:
            x -= amount
    elif direction == 'up':
        if y - amount < 0:
            y = 0
        else:
            y -= amount
        
    elif direction == 'down':
        if y + amount > 400:
            y = 400
        else:
            y += amount
        
    return [x,y]
        
# Function to turn the turtle counterclockwise
def turn(direction):
    if direction == 'right':
        return 'up'    
    elif direction == 'up':
        return  'left'
    elif direction == 'left':
        return  'down'
    elif direction == 'down':
        return  'right'
# Loop user input 5 times to give variation in turtle movement        
while i < 5:  
    print('Turtle: ','( ',x,',',y,' ) ', 'facing:', direction, sep ='') 
    commandI = input('Command (move, jump, turn, sleep) ==> ')
    print(commandI)
    command.insert(i, commandI)
    if commandI.lower() == 'move':
        #print(commandI)
        [x,y] = move(x, y, direction, 20)
        #x = loc[0]
        
    elif commandI.lower() =='jump':
        #print(commandI)
        [x,y] = move(x, y, direction, 50)
        #x = loc[0]
                
    elif commandI.lower() == 'turn':
        direction = turn(direction)
                
    elif commandI.lower() == 'sleep':
        #print(commandI)
        print('Turtle falls asleep.')
        i += 1
        if i < 5:
            print('Turtle: ','( ',x,',',y,' ) ', 'facing:', direction, sep ='')
            print('Turtle is currently sleeping .. no command this turn.')
        else:
            print('Turtle:', '(', x , y ,')', 'facing:', direction)
    i += 1
        
        
# Print statements with all commands entered and new print line with all commands sorted
print()
print('All commands entered:', command)
command.sort()
print('Sorted commands:', command)