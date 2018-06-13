def reverse5(value):
    tenThousand = value // 10000
    thousand    = value // 1000 % 10
    hundred     = value // 100 % 10
    tens        = value // 10 % 10
    ones        = value % 10
    reverse     = (ones * 10000 + tens * 1000 + 
                   hundred * 100 + thousand * 10 + tenThousand)
    return reverse

def reverse3(value):
    hundred = value // 100
    tens    = value // 10 % 10
    ones    = value % 10
    reverse = (ones * 100 + tens * 10 + hundred)
    return reverse
     
    
print('Enter a 5 digit number whose first and third digits must differ by at least 2.')
print('The answer will be 1089, if your number is valid')

value = int(input('Enter a value ==> ' ))
print (value)
print()
print('Here is the computation:')
print(value, 'reversed is', reverse5(value))

last3 = reverse3(reverse5(value)%1000)
answer = last3- reverse5(value)%1000

print(last3, '-', reverse5(value)%1000, '=', answer)
print(answer, '+', reverse3(answer), '=', answer+reverse3(answer))
print('You see, I told you.')