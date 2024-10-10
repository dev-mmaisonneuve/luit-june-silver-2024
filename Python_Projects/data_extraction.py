import os

# Get the current working directory
current_directory = os.getcwd()

# Initialize an empty list to hold the file information
files_info = []

# Loop through all items in the current directory
for item in os.listdir(current_directory):
    item_path = os.path.join(current_directory, item)

    # Check if the item is a file (not a directory)
    if os.path.isfile(item_path):
        # Get file information: name and size
        file_info = {
            'name': item,
            'size': os.path.getsize(item_path)
        }
        # Add the file information to the list
        files_info.append(file_info)

# Print the list of dictionaries containing file information
print(files_info)