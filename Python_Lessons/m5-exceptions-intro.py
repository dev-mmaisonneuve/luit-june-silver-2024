value = int(input('Enter an interger :'))
print('The inverse of', value, 'is', 1/value)


try:
    value = int(input('Enter an interger :'))
    print('The inverse of', value, 'is', 1/value)
except:
    print('You did not provide a number, so i will not calculate the inverse')



try:
    value = int(input('Enter an interger :'))
    print('The inverse of', value, 'is', 1/value)
except ValueError:
    print('You did not provide a number, so i will not calculate the inverse')
except ZeroDivisionError:
    print('You provided 0 an division by 0 is not possible, sorry')



try:
    value = int(input('Enter an interger :'))
    print('The inverse of', value, 'is', 1/value)
except ValueError:
    print('You did not provide a number, so i will not calculate the inverse')
except ZeroDivisionError:
    print('You provided 0 an division by 0 is not possible, sorry')
except:
    print('Something strange happened here, sorry')