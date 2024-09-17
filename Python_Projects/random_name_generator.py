import uuid

# Function to create a unique EC2 name
def create_unique_name(department):
    unique_id = str(uuid.uuid4())[:7]
    return department + '-' + unique_id

# Get number of instances
total_instances = int(input('How many EC2 instances do you want names for? '))

# Get department name
name_of_department = input('Enter the name of your department: ')

# Generate and display the EC2 instance names
print('\nHere are your EC2 instance names:')
for i in range(total_instances):
    print(create_unique_name(name_of_department))

