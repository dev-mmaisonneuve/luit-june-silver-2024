correct_answer = 1994

user_input = int(input('When was Python 1.0 released? '))
while user_input != correct_answer:
    if user_input > correct_answer:
        print('It was earlier than that!')
    else:
        print('It was later than that!')
    user_input = int(input('When was Python 1.0 released? '))
print('Correct!')


# 2nd solution
year_guess = int(input('When was Python 1.0 released? '))

while year_guess != 1994:
    if year_guess > 1994:
        print('It was earlier than that!')
    else:
        print('It was later than that!')
    
    year_guess = int(input('When was Python 1.0 released? '))

print('Correct!')


# 3rd
while True:
    answer = int(input('When was Python 1.0 released? '))
    if answer > 1994:
        print('It was earlier than that!')
    elif answer < 1994:
        print('It was later than that!')
    else:
        print('Correct!')
        break