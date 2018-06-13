'''
Name: Jessy Koifman
Date: 10/29/2016
Homework: #6 (Six Degrees of Villainy)
Purpose: 

Given a file, read through the file to find villain names and the 
set of stories for each villain. 
Ask the user for a villain and count how many times it takes to find this 
villian from one of the top ten most popular villains
Find the top ten most popular villains- will become initial candidates

'''
# FUNCTION THAT CORRECTLY FORMATS THE INCOMING DATA FROM THE FILE
def villainName(x):	
    listV = []
    sh = []
    names = x.strip().split('\t')
    n = names[0].strip()
    shows = names[7].strip().replace(' ', '')
    show = shows.lower()
    sh = show.split(',')
    sh1 = set()
    for word in sh:
        word.strip().replace(' ', '')
        sh1.add(word)
        
    listV = [len(sh1), n, sh1] # CREATE LIST TO BE CREATED INTO LIST OF LIST
    
    return listV

# CREATE A FUNCTION TO CHECK IF GIVEN VILLAIN HAS SHOWS IN COMMON WITH ALL VILLAINS
def in_common(villain, all_villains):
    
    villainC = []
    for i in range(0, len(all_villains)):
        if all_villains[i][1] != villain[1]:
            common = list(villain[2] & all_villains[i][2] ) 
            common.sort()        
            if len(common) == 0:
                continue
            # APPEND TO THE EMPTY LIST LENGTH OF SHOWS, VILLAIN NAME, AND SHOWS
            villainC.append([all_villains[i][0], all_villains[i][1], all_villains[i][2]])
   
    return villainC # LIST OF LIST (ALL_VILLAINS AND VILLAINC)
        


if __name__ == "__main__":
    
    # ASK FOR INPUTS FROM USER FOR FILE AND TARGET VILLAIN
    
    targetV = input('Who are you trying to reach? ')
    print(targetV)
    print()
    targetV = targetV.title()
    
    villains = []
    
    file = "DrWhoVillains.tsv"
    for line in open(file, encoding = "ISO-8859-1"):
        villains.append(villainName(line)) # APPEND LINE FROM FILE TO MAKE LIST OF ALL VILLAINS
    
    
    # SORT LIST SO THAT IS GREATEST TO LEAST (DECREASING)
    villains.sort(reverse=True)
    
    # ASSOCIATE TOTALVILLAINS WITH ORIGINAL VILLAINS LIST
    totalvillains = villains
    
    # CREATE LIST OF TOP TEN VILLAINS
    for i in range(0, 10):
        print('{}. {}'.format(i+1, villains[i][1]))  
      
    # INITIALIZE VARIABLES TO BE USED IN WHILE LOOP
    selection = 0
    times = 0
    notFound = 1
    num = 10
    
    while notFound:
        
        selection = input('Enter a selection => ')
        print(selection)
        print()

        
        # CHECK IF SELECTION INPUT IS VALID
        if selection.isdigit() and (int(selection) >= 1 and int(selection) <= num):
            selection = int(selection)
           
        # PRINT LIST FOR A RANGE GIVEN
        else:
            for i in range(0, num):
                print('{}. {}'.format(i+1, villains[i][1]))
            continue
    
        # INCREASE THE AMOUNT OF TIMES IT TAKES TO FIND THE VILLAIN        
        times+= 1
        
        if targetV == villains[selection-1][1]:
            '''
            If the villain is found (selection matches target villain)
            then set notFound to 0 and finish the loop
            '''
            notFound = 0
            print("You reached the villain {} in {} steps.".format(targetV, times))
            print('Have a nice day.')
            continue
        
        if villains[selection-1][0] == 1:
            print(villains[selection-1][1], 'appeared in', villains[selection-1][0], 
                          'story and overlapped with:')
        else:
            print(villains[selection-1][1], 'appeared in', villains[selection-1][0], 
                  'stories and overlapped with:')
        
        print()
        
        # NEW LIST INITIALIZED TO COMPARE VILLAINS TO ORIGINAL TOTAL VILLAINS LIST
        listVillain = []
        listVillain = in_common(villains[selection-1], totalvillains)
        
        # INITIALIZE COUNT TO ZERO, CREATE NEW RANGE FOR THE LENGTH OF VILLAINS
        count = 0
        for i in range(len(listVillain)):
            count += 1
            print('{}. {}'.format(count, listVillain[i][1]))
        
        # ASSIGN NEW LIST OF VILLAINS TO VILLAIN LIST TO USE FOR NEXT LOOP 
        villains = listVillain
        num = len(listVillain)\
            
            