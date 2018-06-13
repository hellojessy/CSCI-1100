'''
Write a program that reads in a word entered by the user and checks whether:
- the word has at least 8 characters
- starts with a vowel
- has alternating vowels and consonants, and
- the consonants are in increasing alphabetical order

Program should work for upper case or lower case and take use of a
single function (including a loop)
'''

def is_alternating(word): # Create initial function to check alternating condition
    x = 'aeiou'
    i = 0
    alternate = 1 # If alternate is 1, phrase is alternating, otherwise 0
    
    if len(word) >= 8 and word[0] in x: # Initial check conditions
        while i < (len(word)-1) and (alternate == 1):
            '''
            Check if i is vowel
            Next should be alternate
            otherwise alternate is set to 0
            '''
            if word[i] in x:
                if word[i+1] not in x:
                    alternate = 1
                else:
                    alternate = 0
                    '''
                    Check if i + 1 is a vowel
                    If it is, next consanent should be greater than first
                    If true, alternate set to 1
                    '''
            else:
                if word[i+1] in x:
                    if i+2 < len(word):
                        if word[i] < word[i+2]:
                            alternate = 1
                        else:
                            alternate = 0
                    else:
                        alternate = 1
                else:
                    alternate = 0  
            i += 1                                 
    else:            
        alternate = 0
         
    return alternate   
            
altWord = input('Enter a word => ') # Prompt user for input
print(altWord)
altWord2 = altWord.lower()
if is_alternating(altWord2) == 0: 
    print("The word" , "'" + altWord + "'", "is not alternating")
else:
    print("The word" , "'" + altWord + "'", "is alternating")