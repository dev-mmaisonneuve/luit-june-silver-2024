import uuid

def create_unique_name(department):
    unique_id = str(uuid.uuid4())[:7]
    return department + '-' + unique_id

total_instances = int(input('How many EC2 instances do you want names for? '))

name_of_department = input('Enter the name of your department: ')

print('\nHere are your EC2 instance names:')
for i in range(total_instances):
    print(create_unique_name(name_of_department))

