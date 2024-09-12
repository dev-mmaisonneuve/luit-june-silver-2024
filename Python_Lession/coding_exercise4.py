hours_worked = float(input('How many hours did you work last month? '))
hourly_rate = float(input('What is your hourly rate? '))

salary = hours_worked * hourly_rate

print('Last month, you earned', salary, 'dollars')

# another way of writing it

hours = float(input('How many hours did you work last month? '))
rate = float(input('What is your hourly rate? '))
 
print('Last month, you earned', hours * rate ,'dollars')
