import json

'''
This program is designed to read a file with data of a list
of dictionaries in which each dictionarycontains climate values
for a single month and year. The program should read in a year of
the interval 1956 through 2015 and find out the climate information
for a given year
'''

# THIS FUNCTION CREATES A LIST CONTAINING YEAR MONTH, AND INFO
def result(year, data, info):
    climate = []
    i = 0
    while i <= len(data)-1:
        if year == data[i]['year']: # YEAR IN DATA IS YEAR IN LIST
            month = data[i]['month'] 
            climate.append([data[i][info], month])      
        i += 1
    return climate

# THIS FUNCTION CALCULATES VALUES TO FIND AVERAGES  
def calcA(year, data, avgMonth):
    monthly = result(year, data, 'MNTM')
    sumUp = [] # NEW LIST TO APPEND AVERAGE TEMPERATURE VALUES
    
    if avgMonth == 0: # OVERALL AVERAGE
        for month in monthly:
            if month[0] != -9999: # CHECK IF VALUE IS NOT VALID
                sumUp.append(month[0])
        print('Overall: {:.1f}'.format(sum(sumUp)/len(sumUp)))
        
        
    if avgMonth == 1: # AVERAGE FIRST 6 MOTNHS
        if year == 1956: # 1956 IS SPECIAL YEAR (<12 MONTHS)
            print('First 6 months: Not enough data')
            
        else:          
            num = 0 
            while num >= 0 and num < 6:
                if monthly[num][0] != -9999:
                    sumUp.append(monthly[num][0])            
                num += 1
            print('First 6 months: {:.1f}'.format(sum(sumUp)/len(sumUp)))
        
        
    if avgMonth == 2: # AVERAGE LAST 6 MOTNHS
        if year == 2015: # 2015 IS SPECIAL YEAR (<12 MONTHS)
            print('Last 6 months: Not enough data')
            
        else:         
            num = 6 # USE ONLY 1 WHILE LOOP RATHER THAN REPEAT    
            numStart = 6
            if year == 1956:
                num = 0 
                numStart = 0
            while num >= numStart and num <= numStart + 5: #CHECKS 6 MONTHS
                if monthly[num][0] != -9999:
                    sumUp.append(monthly[num][0])
                num += 1
            print('Last 6 months: {:.1f}'.format(sum(sumUp)/len(sumUp)))


# FUNCTION TO SORT VALUES AND PRINT INFORMATION
def printF(year, data, info, extreme):
    clim = result(year, data, info)

    if extreme == 'highest':
        clim.sort(reverse = True) # PRINTS HIGHEST TO LOWEST
    else:
        clim.sort()

    i = 0
    count = 4 # INITIALIZE COUNT TO 4 VALUES TO CHECK IF LESS THAN 4 (INVALID)
    countZ = []
    while i < count and i < len(clim):
        
        if clim[i][0] == -9999:
            count += 1 # INCREASES COUNT => CHECK NEXT VALUE
            i += 1
            continue # INVALID VALUES DO NOT GET ADDED TO LIST COUNTZ
        countZ.append((clim[i][1], clim[i][0]))
        i += 1 
        
        
    if len(countZ) <= 3: # CHECK IF MORE THAN 3 VALID DATA VALUES
        print('Not enough data', end = '')
        
    else:
        for value in range(len(countZ)-2):
            print('{}: {:.1f}, '.format(countZ[value][0], countZ[value][1]), end='') # PRINTS FIRST TWO VALUES WITH CORRECT FORMATTING
        print('{}: {:.1f}'.format(countZ[-2][0], countZ[-2][1]), end = '')
     
        
# FUNCTION TO DRAW HISTOGRAM STARS    
def histogram(year, data, avgMonth):
    monthly = result(year, data, 'MNTM')
    sumUp = []
    
    if avgMonth == 0: # FIRST 3 MONTHS
        num = 0 # SET TO 0 FIRST TIME TO USE 1 LOOP STATEMENT AT END
        numStart = 0
        print('01-03: ', end= '')
    elif avgMonth == 1: # MONTHS 4-6
        num = 3 
        numStart = 3
        print('04-06: ', end = '')
    elif avgMonth == 2: # MONTHS 7-9
        if year == 1956: # 1956 SPECIAL YEAR (ONLY HAS LAST 6 VALUES/MONTHS)
            num = 0  
            numStart = 0
        else:
            num = 6
            numStart = 6
        print('07-09: ', end = '')
    elif avgMonth == 3: # MONTHS 10-12
        if year == 1956:
            num = 3
            numStart = 3
        else:
            num = 9
            numStart = 9
        print('10-12: ', end = '')
    
    
    if (avgMonth == 0 or avgMonth == 1) and (year == 1956): # SPECIAL YEAR
        print('Not enough data')
    
    elif (avgMonth == 2 or avgMonth == 3) and (year == 2015): # SPECIAL YEAR
        print('Not enough data')
        
    else:    
        while num >= numStart and num < numStart + 3:
            if monthly[num][0] != -9999: # CHECKS INVALID CONDITION
                sumUp.append(monthly[num][0])
            num += 1

        print('{}'.format('*' * (int(sum(sumUp)/len(sumUp)))))
    
    
#  MAIN PROGRAM  :) :P :) :P
if __name__ == '__main__':
    data = json.loads(open("tempdata.json").read()) # READ INPUT FILE
    
    year = int(input('Enter a year (1956-2015) => '))
    print(year)
    
    # CHECKS ALL REQUIRED INFO PARAMETERS
    
    # TEMPERATURES
    print('Temperatures')
    print('-'*70)
    info = 'EMXT'
    print('Highest max value => ', end = '')
    printF(year, data, info, "highest")
   
    info = 'EMNT'
    print('\nLowest min value => ', end = '')
    printF(year, data, info, "lowest")
   
    info = 'DT90'
    print('\nHighest days with max >= 90 => ', end = '')
    printF(year, data, info, "highest")
    
    info = 'DX32'
    print('\nHighest days with max <= 32 => ', end = '')
    printF(year, data, info, "highest")
    print()
    
    # PRECIPITATION
    print('\nPrecipitation')
    print('-'*70)
    info = 'TPCP'
    print('Highest total => ', end = '')
    printF(year, data, info, "highest")
    
    info = 'TPCP'
    print('\nLowest total => ', end = '')
    printF(year, data, info, "lowest")
   
    info = "TSNW"
    print('\nHighest snow depth => ', end = '')
    printF(year, data, info, "highest")
    
    info = "TSNW"
    print('\nLowest snow depth => ', end = '')
    printF(year, data, info, "lowest")
    print()   
    
    # AVERAGE TEMPERATURES
    print('\nAverage temperatures')
    print('-'*70)
    
    # AVERAGE VALUE CALL FUNCTION X3
    calcA(year, data, 0)
    calcA(year, data, 1)
    calcA(year, data, 2)
    
    # TEMPERATURE HISTOGRAMS
    print('\nTemperature histograms')
    print('-'*70)
    
    # HISTOGRAM CALL FUNCTION X4
    histogram(year, data, 0)
    histogram(year, data, 1)
    histogram(year, data, 2)
    histogram(year, data, 3)