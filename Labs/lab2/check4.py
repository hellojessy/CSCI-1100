first_name = input('Please enter your first name: ')
last_name  = input('Please enter your last name: ')
greeting = ('Hello,')

out = max(len(first_name),len(last_name),len(greeting))
print('*' * (7+(out)))
print('**', greeting, ' ' * (out-len(greeting)) +' **')
print('**', first_name, ' ' * (out-len(first_name)) +' **')
print('**', last_name+'!', ' ' * (out-len(last_name)) + '**')
print('*' * (7+(out)))