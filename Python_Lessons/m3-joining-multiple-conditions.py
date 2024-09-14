user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if user_age < 25 and user_country == 'Germany':
    print('You can apply for a German student exchanfe programme')
else:
    print('Sorry, you do not qualify')


# 2nd statement
user_country = input('What is your country? ')
if user_country == 'Sweden' or user_country == 'Denmark' or user_country == 'Norway':
    print('You can apply for a scandinavian student exchange programme')
else:
    print('Sorry, you do not qualify')


#3rd statement
user_country = input('Where do you come from')
if not user_country == 'Germany':
    print('You are not from Germany!')
else:
    print('You are from Germany')

#4th statement
user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if not user_country == 'Germany' and user_age < 25 or \
    user_country == 'Germany' and user_age < 23:
    print('You qualify!')
else:
    print('You don\'t qualify')