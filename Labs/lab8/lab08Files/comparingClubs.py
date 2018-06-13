def get_words(description):
    text = set()
    names = description.strip().split('|')
    descrip = names[1].replace('.', ' ').replace(',',' ').replace('()', ' ').replace('"', ' ').lower()
    words = descrip.split(' ')
    
    count = 0
    for x in words:
        if len(x) >= 4 and x.isalpha():
            text.add(x)
            count += 1
   
    return text
    
    
input_file1 = input('Input a file: ')
input_file2 = input('Input another file: ')

#line = open(input_file1).read()
club1 = get_words(open(input_file1).read())
    
#line = open(input_file2).read()
club2 = get_words(open(input_file2).read())

print()
print('Comparing clubs {} and {}: '.format(input_file1.replace('.txt', ''), input_file2.replace('.txt', '')))   
print()
print('Same words: ', club1.intersection(club2))
print(len(club1.intersection(club2)))
print('Unique to {}: {}'.format(input_file1.replace('.txt', ''), club1.difference(club2)))
print(len(club1.difference(club2)))
print('Unique to {}: {}'.format(input_file2.replace('.txt', ''), club2.difference(club1)))
print(len(club2.difference(club1)))