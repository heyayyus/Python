# write a python programe to print the contents of directory using the os module, search online for the function which does that
# so we can use the os module to print the contents of the directory


import os


# Define the directory path (use '.' for the current directory)
directory_path = "/"

# Use os.listdir() to get the contents of the directory
contents = os.listdir(directory_path)

    # Print the contents of the directory
print("Contents of the directory:")
for item in contents:
    print(item)