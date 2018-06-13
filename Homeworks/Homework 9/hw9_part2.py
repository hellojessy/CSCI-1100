import json
import textwrap

busIn = input('Enter a business name => ')
print(busIn)

k = open('businesses.json')

# FUNCTION CRETAED TO FIND REVIEWS FOR GIVEN BUSINESS
def reviewBus(businessID):
    f = open('reviews.json')
    
    countRev = 0
    for lineN in f:
        review = json.loads(lineN)
        busID = review['business_id']
        rev   = review['text']
        
        # IF BUSINESS ID WANTED MATCHES WHAT USER WANTS..
        if businessID == busID:
            if rev != '': # CHECK IF NO REVIEWS EXIST FOR BUSINESS
                countRev += 1
                print()
                print('Review:', countRev) 
                # SPLIT REVIEWS BASED ON SPACING IN FILE
                revS = rev.split('\n\n')
                for x in revS:
                    # USE TEXTWRAP TO PROVIDE NECESSARY OUTPUT
                    wrapper = textwrap.TextWrapper( initial_indent = ' '*4, subsequent_indent = ' '*4 )
                    lines = wrapper.wrap(x) 
                    for y in lines:
                        print(y)
                    print()
                    
    # SPECIAL CONDITION IF NO REVIEWS FOUND FOR FOUND BUSINESS                
    if countRev == 0:
        print('No reviews for this business are found')
        

count = 1 
busList = []

# EXAMINE BUSINESS FILE TO GET BUSINESS NAME, ID AND ADDRESS
for lineK in k:
    business = json.loads(lineK)
    busName = business['name']
    address = business['full_address']
    myID = business['business_id']
    
    if busIn in busName:
        count += 1
        busList.append((address, myID))
        
if len(busList) == 0: # IF USER INPUTTED BUSINESS IS NOT FOUND
    print('This business is not found')

elif len(busList) > 1: # IF MORE THAN ONE LOCATION FOUND FOR ONE BUSINESS
    print('\nFound {} at:\n'.format(busIn))
    
    for x in range(len(busList)):
            print('{}.\n{}\n'.format(x+1, busList[x][0]))       
    
    # ASK USER FOR INPUT IF MORE THAN ONE ADDRESS FOUND
    numIn = int(input('Select one from 1 - {} ==> '.format(count-1)))
    print(numIn)
     
    while numIn < (1) or numIn > (count-1):
        numIn = int(input('Select one from 1 - {} ==> '.format(count-1)))
        print(numIn)    
    print()
    
    # USE SELECTION NUMBER FROM USER TO FIND REVIEWS FOR BUSINESS
    print('Using {} at:\n{}'.format(busIn, busList[numIn-1][0]))        
    reviewBus(busList[numIn-1][1])

# SPECIAL CONDITION IF ONLY ONE BUSINESS EXISTS FOR WHAT USER INPUTS
elif len(busList) == 1:
    print('\nUsing {} at:\n{}'.format(busIn, busList[0][0]))        
    reviewBus(busList[0][1])   