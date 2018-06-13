'''
1. Asks user for a year in the range 1880 to 2014 and print error if it is not
2. Ask user for female name and find index 
3. Use the index of the nameplus/minus 5 and 10 years within the range, ignore
any dates outside of the 1880- 2014 range
4. If the name was found in the year, output the statistics of the name
including year tested, the rank, the count, the percemtage of the count 
relative to the count of the top ranked name, and the percentage of the name
relative to the sum of all the name counts in the top 250. If index is between
0 and 249, print nothing
5. Repeat process with male name
'''
import read_names
import sys

#Read in all the names. The result is stored in the module
read_names.read_from_file("top_names_1880_to_2014.txt")

#Check is year is valid
yearCheck = int(input('Enter the year to check => '))

#Check for female name in - 10 years
if (yearCheck >= 1880 and yearCheck <= 2014):
    print (yearCheck)
    name = input('Enter a female name => ')
    print (name)
    print ('Data about female names')
    print(name + ':')
    if (yearCheck - 10 >= 1880 and yearCheck - 10 <= 2014):
        (female_names,female_counts) = read_names.top_in_year(yearCheck-10, 'f')
        if (name in female_names):
            i = female_names.index(name)
            percent = female_counts[i] / female_counts[0] * 100
            percentC = female_counts[i] / sum(female_counts) * 100
            print ('   {:d}: {:3d} {:5d} {:7.3f} {:7.3f}'.format(yearCheck - 10, i+1, female_counts[i], percent, percentC))
                   
        else:
            print ('   {:d}: Not in the top 250'.format(yearCheck - 10))
            
#Check for female name in - 5 years
    if (yearCheck - 5 >= 1880 and yearCheck - 5 <= 2014):
        (female_names,female_counts) = read_names.top_in_year(yearCheck - 5, 'f')
        if (name in female_names):
            i = female_names.index(name)
            percent = female_counts[i] / female_counts[0] * 100
            percentC = female_counts[i] / sum(female_counts) * 100
            print ('   {:d}: {:3d} {:5d} {:7.3f} {:7.3f}'.format(yearCheck - 5, i+1, female_counts[i], percent, percentC))
        else:
            print ('   {:d}: Not in the top 250'.format(yearCheck - 5)) 
            
#Check for female name in given year           
    if (yearCheck >= 1880 and yearCheck <= 2014):
        (female_names,female_counts) = read_names.top_in_year(yearCheck, 'f')
        if (name in female_names):
            i = female_names.index(name)
            percent = female_counts[i] / female_counts[0] * 100
            percentC = female_counts[i] / sum(female_counts) * 100
            print ('   {:d}: {:3d} {:5d} {:7.3f} {:7.3f}'.format(yearCheck, i+1, female_counts[i], percent, percentC))
        else:
            print ('   {:d}: Not in the top 250'.format(yearCheck))   
#Check for female name in + 5 years            
    if (yearCheck + 5 >= 1880 and yearCheck + 5 <= 2014):
        (female_names,female_counts) = read_names.top_in_year(yearCheck + 5, 'f')
        if (name in female_names):
            i = female_names.index(name)
            percent = female_counts[i] / female_counts[0] * 100
            percentC = female_counts[i] / sum(female_counts) * 100
            print ('   {:d}: {:3d} {:5d} {:7.3f} {:7.3f}'.format(yearCheck + 5, i+1, female_counts[i], percent, percentC))
        else:
            print ('   {:d}: Not in the top 250'.format(yearCheck + 5))

#Check for female name in + 10 years
    if (yearCheck + 10 >= 1880 and yearCheck + 10 <= 2014):
        (female_names,female_counts) = read_names.top_in_year(yearCheck + 10, 'f')
        if (name in female_names):
            i = female_names.index(name)
            percent = female_counts[i] / female_counts[0] * 100
            percentC = female_counts[i] / sum(female_counts) * 100
            print ('   {:d}: {:3d} {:5d} {:7.3f} {:7.3f}'.format(yearCheck + 10, i+1, female_counts[i], percent, percentC))
        else:
            print ('   {:d}: Not in the top 250'.format(yearCheck + 10))
            
    print()
    
    name = input('Enter a male name => ')
    print (name)
    print ('Data about male names')
    print(name + ':') 
    
#Check for male name in - 10 years    
    if (yearCheck - 10 >= 1880 and yearCheck - 10 <= 2014):
        (male_names,male_counts) = read_names.top_in_year(yearCheck-10, 'M')
        if (name in male_names):
            i = male_names.index(name)
            percent = male_counts[i] / male_counts[0] * 100
            percentC = male_counts[i] / sum(male_counts) * 100
            print ('   {:d}: {:3d} {:5d} {:7.3f} {:7.3f}'.format(yearCheck - 10, i+1, male_counts[i], percent, percentC))
                   
        else:
            print ('   {:d}: Not in the top 250'.format(yearCheck - 10))
            
#Check for male name in - 5 years
    if (yearCheck - 5 >= 1880 and yearCheck - 5 <= 2014):
        (male_names,male_counts) = read_names.top_in_year(yearCheck-5, 'M')
        if (name in male_names):
            i = male_names.index(name)
            percent = male_counts[i] / male_counts[0] * 100
            percentC = male_counts[i] / sum(male_counts) * 100
            print ('   {:d}: {:3d} {:5d} {:7.3f} {:7.3f}'.format(yearCheck - 5, i+1, male_counts[i], percent, percentC))
                   
        else:
            print ('   {:d}: Not in the top 250'.format(yearCheck - 5))
            
#Check for male name in given years            
    if (yearCheck >= 1880 and yearCheck <= 2014):
        (male_names,male_counts) = read_names.top_in_year(yearCheck, 'M')
        if (name in male_names):
            i = male_names.index(name)
            percent = male_counts[i] / male_counts[0] * 100
            percentC = male_counts[i] / sum(male_counts) * 100
            print ('   {:d}: {:3d} {:5d} {:7.3f} {:7.3f}'.format(yearCheck, i+1, male_counts[i], percent, percentC))
                   
        else:
            print ('   {:d}: Not in the top 250'.format(yearCheck)) 

#Check for male name in + 5 years            
    if (yearCheck + 5 >= 1880 and yearCheck + 5 <= 2014):
        (male_names,male_counts) = read_names.top_in_year(yearCheck + 5, 'M')
        if (name in male_names):
            i = male_names.index(name)
            percent = male_counts[i] / male_counts[0] * 100
            percentC = male_counts[i] / sum(male_counts) * 100
            print ('   {:d}: {:3d} {:5d} {:7.3f} {:7.3f}'.format(yearCheck + 5, i+1, male_counts[i], percent, percentC))
                   
        else:
            print ('   {:d}: Not in the top 250'.format(yearCheck + 5))
            
#Check for male name in + 10 years            
    if (yearCheck + 10 >= 1880 and yearCheck + 10 <= 2014):
        (male_names,male_counts) = read_names.top_in_year(yearCheck+10, 'M')
        if (name in male_names):
            i = male_names.index(name)
            percent = male_counts[i] / male_counts[0] * 100
            percentC = male_counts[i] / sum(male_counts) * 100
            print ('   {:d}: {:3d} {:5d} {:7.3f} {:7.3f}'.format(yearCheck +  10, i+1, male_counts[i], percent, percentC))
                   
        else:
            print ('   {:d}: Not in the top 250'.format(yearCheck + 10))       
            
else:
    print('Year must be at least 1880 and at most 2014')