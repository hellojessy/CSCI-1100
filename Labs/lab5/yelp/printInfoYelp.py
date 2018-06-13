import lab05_util

def print_info(restaurant):
    print (restaurant[0], '(' + restaurant[5] + ')')
    string1 = restaurant[3]
    .split('+')
    print('\t', string1[0])
    print('\t', string1[1])
    listR = restaurant[-1]
    average = sum(listR)/len(listR)
    print ('Average score: {:.2f}'.format(average))
    
# Main code starts here
restaurants = lab05_util.read_yelp('yelp.txt')
print_info(restaurants[0])
print()
print_info(restaurants[1])