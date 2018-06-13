import lab05_util
import webbrowser

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

def directions(restaurant):
    print('What would you like to do next?')
    print('1. Visit homepage')
    print('2. Show on Google Maps')
    print('3. Show directions to this restaurant')    
    userInput = int(input('Your choice (1-3)? ==> '))
    string1 = restaurant[3].split('+')
    web = restaurant[4]
    if userInput == 1:
        webbrowser.open(web)
    if userInput == 2:
        webbrowser.open('http://www.google.com/maps/place/' + string1[0] + ' ' + string1[1])
    if userInput == 3:
        webbrowser.open('http://www.google.com/maps/dir/110 8th Street Troy NY/' + string1[0] + string1[1])  
    
    
# Main code starts here
restaurants = lab05_util.read_yelp('yelp.txt')
print_info(restaurants[i-1])
directions(restaurants[i-1])