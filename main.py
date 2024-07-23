import os

# Specify the directory where you want to create the folders
directory = r'C:'

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Create 100 empty folders
for i in range(1, 101):
    folder_name = f'folder{i}'
    folder_path = os.path.join(directory, folder_name)

    # Create the folder
    os.makedirs(folder_path)

print("Empty folders created successfully.")
