import lab05_util

i = 1
i = int(input('Enter an ID of a restaurant: '))
def print_info(restaurant):
    if i >= 1 and i <= len(restaurants):
        print (restaurant[0], '(' + restaurant[5] + ')')
        string1 = restaurant[3].split('+')
        print('\t', string1[0])
        print('\t', string1[1])
        listR= restaurant[-1]
        sumTotal = sum(listR) - max(listR)- min(listR)
        average = sumTotal/len(listR)
        if average >= 0 and average < 2:
            print('This restaurant is rated bad, based on', len(listR), 'reviews')
        elif average >= 2 and average < 3:
            print('This restaurant is rated average, based on', len(listR), 'reviews')
        elif average >= 3 and average < 4:
            print('This restaurant is rated above average, based on', len(listR), 'reviews.')
        else:
            print('This restaurant is rated vey good, based on', len(listR), 'reviews')
            
    else:
        print ('Warning, ID is invalid')
    
# Main code starts here
restaurants = lab05_util.read_yelp('yelp.txt')
print_info(restaurants[i-1])