def ok_to_add(row, col, num, data):
    if data[row][col] == '.':
        i = 0
        for i in range(0, 9):       
            if [data][i] == num:
                return False
        i = 0
        for j in range(0, 9):
            if [data][j] == num:
                return False
        
        r = row / 3
        c = column / 3
        
        if r == 0 and c ==0:
            if i in range(0, 3):
                if j in range(0, 3):
                    if [data][i][j] == num:
                        return False
        
        if r == 1 and c == 0:
            if i in range(3, 6):
                if j in range(0, 3):
                    if [data][i][j] == num:
                        return False
                    
        if r == 0 and c == 1:
            if i in range(0, 3):
                if j in range(3, 6):
                    if [data][i][j] == num:
                        return False
                    
        if r == 0 and c == 2:
            if i in range(0, 3):
                if j in range(6, 9):
                    if [data][i][j] == num:
                        return False   
                    
        if r == 2 and c == 0:
            if i in range(6, 9):
                if j in range(0, 3):
                    if [data][i][j] == num:
                        return False    
                    
        if r == 1 and c == 1:
            if i in range(3, 6):
                if j in range(3, 6):
                    if [data][i][j] == num:
                        return False
    
        if r == 1 and c == 2:
            if i in range(3, 6):
                if j in range(6, 9):
                    if [data][i][j] == num:
                        return False    
                            
        if r == 2 and c == 1:
            if i in range(6, 9):
                if j in range(3, 6):
                    if [data][i][j] == num:
                        return False 
        
        if r == 2 and c == 2:
            if i in range(6, 9):
                if j in range(6, 9):
                    if [data][i][j] == num:
                        return False  
    return True

    
    
    
bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]


print('-'*25)

# INITIATE WITH EMPTY STRING
sudokuN = ''

# CREATE LOOP TO FORMAT SUDOKU BOARD
for i in range(len(bd)):
    line = ' '.join(bd[i])
    for j in range(9):
        line = ' '.join(bd[i])
        
        # CHECK WHEN TO ADD VERTICAL COLUMN
        if j == 2 or j == 6: 
            bd[i].insert(j+1, '|')
    sudokuN += '| ' + line + ' |'
    sudokuN += '\n'
    
    # CHECK WHEN TO ADD HORIZONTAL ROW
    if i == 2 or i == 5: 
        sudokuN += '-' * 25 + '\n'
print(sudokuN + '-' * 25)


# INPUT STATEMENTS
rowCheck = int(input('Enter a row to check: '))
colCheck = int(input('Enter a column to check: '))
numCheck = int(input('Enter a number to input: ')) 

                 
if ok_to_add(rowCheck, colCheck, numCheck, bd) == True:
    bd[i].insert(num, i)
    bd[j].insert(num, j)
    print(bd)

else:
    print('Not ok to add')