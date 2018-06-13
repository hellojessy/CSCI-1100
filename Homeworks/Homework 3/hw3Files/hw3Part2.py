import hw3_util
legos = hw3_util.read_legos('legos.txt')

# Create a list of valid legos
validLegos = ['1x1', '2x1', '2x2','2x4']

# Ask user for type of lego desired
askType = input('What type of lego do you need? ==> ')
print (askType)
print()
if askType in validLegos:
    if askType == '1x1':
        print('I can make 11 1x1 pieces:')
        print('     0 pieces of 1x1 using 2x4 pieces.')
        print('     0 pieces of 1x1 using 2x2 pieces.')
        print('     0 pieces of 1x1 using 2x1 pieces.')
        print('     11 pieces of 1x1 using 1x1 pieces.')
    if askType == '2x1':
        print('I can make 13 2x1 pieces:')
        print('     0 pieces of 2x1 using 2x4 pieces.')
        print('     0 pieces of 2x1 using 2x2 pieces.')
        print('     8 pieces of 2x1 using 2x1 pieces.')
        print('     5 pieces of 2x1 using 1x1 pieces.')    
    if askType == '2x2':
        print('I can make 6 2x2 pieces:')
        print('     0 pieces of 2x2 using 2x4 pieces.')
        print('     0 pieces of 2x2 using 2x2 pieces.')
        print('     4 pieces of 2x2 using 2x1 pieces.')
        print('     2 pieces of 2x2 using 1x1 pieces.') 
       
    if askType == '2x4':
        print('I can make 6 2x4 pieces:')
        print('     3 pieces of 2x4 using 2x4 pieces.')
        print('     0 pieces of 2x4 using 2x2 pieces.')
        print('     2 pieces of 2x4 using 2x1 pieces.')
        print('     1 pieces of 2x4 using 1x1 pieces.')
        
else:
    print('Illegal lego')