'''
Write a program that either encrypts or decrypts a string, depending on the 
choice that the user makes. The program should follow the rules:

replace any a after a space with %4%.
replace all occurrences of string he with 7!
replace any remaining e with 9(*9(
replace all occurrences of string y with *%$
replace all occurrences of string u with @@@
replace all occurrences of string an with -?
replace all occurrences of string th with !@+3
replace all occurrences of string o with 7654
replace all occurrences of string 9 with 2

The program should also be able to decrypt the string by following the same 
rules but backwards
'''

def encrypt(word):
    resultE = word.replace(' a', '%4%').replace('he' , '7!').replace('e' , '9(*9(').replace('y' , '*%$').replace('u' , '@@@').replace('an' , '-?').replace('th' , '!@+3').replace('o' , '7654').replace('9' , '2')
    return resultE
    
def decrypt(word):
    resultD = word.replace('2' , '9').replace('7654' , 'o').replace('!@+3' , 'th').replace('-?' , 'an').replace('@@@' , 'u').replace('*%$' , 'y').replace('9(*9(','e').replace('7!' , 'he').replace('%4%', ' a')
    return resultD

enterStatement = input("Enter 'E' for encrypt or 'D' for decrypt ==> ")
print (enterStatement)
if (enterStatement == 'E' or enterStatement == 'e'):
    encryptWord = input('Enter regular text ==> ')
    print (encryptWord)
    print()
    resultE = print('Encrypted as ==>', encrypt(encryptWord))
    print ('Difference in length ==>', len(encrypt(encryptWord))-len(encryptWord))
           
elif (enterStatement == 'D' or enterStatement == 'd'):
    decryptWord = input('Enter cipher text ==> ')
    print (decryptWord)
    print()
    resultD = print('Deciphered as ==>', decrypt(decryptWord))
    print ('Difference in length ==>', len(decryptWord)-len(decrypt(decryptWord)))
else:
    print ("I didn't understand ... exiting")