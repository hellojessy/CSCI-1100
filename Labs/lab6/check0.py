line = ''

for i in range(0, 9):
    if i % 3 == 0 and i!= 0:
        line = line + ('\n')
    for j in range(0, 9):
        if j % 3 == 0 and j!= 0:
            line = line + str(' ')
        line = line + str(i) + str(',') + str(j) + str(' ')
    line = line + ('\n')
print(line)


def rowNumber(num):
    line = ''
    for i in range(0, 9):
        line = line + str(num) + ',' + str(i) + str(' ')
    print(line)
    
def colNumber(num):
    line = ''
    for j in range(0, 9):
        line = line + str(j) + ',' + str(num) + str(' ')
    print(line)

def square(rowS, rowE, colS, colE):
    line = ''
    for i in range(rowS, rowE):
        for j in range(colS, colE):
            line = line + str(i) + ',' + str(j) + str(' ')
        line = line + ('\n')
    print(line)

rowNumber(4)
print()
colNumber(5)
print()
square(0, 3, 0, 3)