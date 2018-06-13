def get_line(fname, parno, lineno):
    para = 1
    lineP = 0
    fname = fname + str('.txt')
    f = open(fname)
    line = f.readline()
    for line in f:
        line = line.rstrip()
        if len(line.strip()) == 0:
            para += 1
        if para == parno:
            if lineP == lineno:
                print(line)
            lineP += 1                
                
                
fNum = input('Please enter the file number == > ')   
pNum = int(input('Please enter the paragraph number ==> '))
lNum = int(input('Please enter the line number ==> '))
get_line(fNum, pNum, lNum)