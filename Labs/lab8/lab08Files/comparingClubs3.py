def get_words(description):
    clubName = ''
    text = set()
    names = description.strip().split('|')
    descrip = names[1].replace('.', ' ').replace(',',' ').replace('()', ' ').replace('"', ' ').lower()
    words = descrip.split(' ')
    clubName = names[0]
    
    count = 0
    for x in words:
        if len(x) >= 4 and x.isalpha():
            text.add(x)
            count += 1
    
    return clubName, text

input_file1 = input('Input a file: ')
input_file2 = input('Input all clubs file: ')

club1 = get_words(open(input_file1).read())

inter = []
for club in open(input_file2):
    x = []
    club2 = get_words(club)
    if club1[0] != club2[0]:
        intersect = club1[1].intersection(club2[1])
        if len(intersect) > 0:
            inter.append([len(intersect), club2[0]])
                  
inter.sort(reverse=True)
print()
for i in range(0,5):
    print(inter[i][1])