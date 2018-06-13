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
    print('count: ', count)
    print(text)
    
    
input_file = input('Input a file: ')
for line in open(input_file):
    get_words(line)