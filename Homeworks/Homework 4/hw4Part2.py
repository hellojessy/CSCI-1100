
import hw4_util

def deathCount(city1, city2, cdata1, cdata2): # Take 4 arguments

    ##print(city1, cdata1)	 
    ##print(city2, cdata2)

    ##cdata = [0] * len(cdata1)
    cdata =[] # Create new list for county data
    if len(cdata1) == len(cdata2):    
        i =  0
        count = 0 # Inital count to 0 so that it is easier to compare
        ## countM = 0
        while i < len(cdata1):
            ##cdata.append('{:.1f}'.format(cdata1[i]-cdata2[i]))
            '''
            Create conditions necessary to check if +, -, or = to create trend
            '''
            if (cdata1[i] - cdata2[i] <= 50) and (cdata1[i] - cdata2[i] >= -50):
                cdata.append('=')
            elif (cdata1[i] - cdata2[i] > 50):
                cdata.append('-')
                ##countM += 1
                count -= 1
            else:
                cdata.append('+')
                count += 1
                ##    cdata[i] = cdata1[i] - cdata2[i]
            i += 1
        
        cdata.reverse()
        print()
        print (' ' * 6, '2013   2003') # Create trend graph
        print ('Trend:', ''.join(cdata)) # Combine data in the list
        print()
        
        if count > 0:
            print('I would rather live in', city1, 'than', city2)
        elif count < 0:
            print('I would rather live in', city2, 'than', city1)
        else:
            print(city1, 'and', city2, 'are the same')
    
    
    else:
        print('not equal lists')


area1 = input('Enter the first area to check => ')
print(area1)

dataC1 = hw4_util.read_deaths(area1) # Read data from file
##print(dataC1)
if dataC1 == []: # Check if data exists in list
    print (area1, 'is an invalid name')
        
else:
    area2 = input('Enter the second area to check => ')
    print(area2)

    dataC2 = hw4_util.read_deaths(area2)
##    print(dataC2)
    if dataC2 == []:
        print (area2, 'is an invalid name')
    
    else:
        deathCount(area1, area2, dataC1, dataC2)