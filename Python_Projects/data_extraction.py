import os

# Function to gather information about files in the current directory
def get_files_info():
    # Create an empty list to store file information
    files_info = []

    # Get a list of all files and folders in the current directory
    for file_name in os.listdir():
        # Check if the item is a file (ignore folders)
        if os.path.isfile(file_name):
            # Get the file size (in bytes)
            file_size = os.path.getsize(file_name)

            # Get the file type (extension), e.g., '.txt', '.py'
            file_type = os.path.splitext(file_name)[1]

            # Create a dictionary to store details about the file
            file_info = {
                'file_name': file_name,
                'file_size': file_size,
                'file_type': file_type
            }

            # Add the file information to the list
            files_info.append(file_info)

    # Return the list of file information
    return files_info

# Call the function and store the result in a variable
files_info_list = get_files_info()

# Print the list of file information
print(files_info_list)
