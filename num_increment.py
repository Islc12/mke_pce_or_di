#!/usr/bin/env python3

import subprocess
import os
import glob

# Set the range for the numbers
minnum = int(input("Enter the starting number: "))
maxnum = int(input("Enter the ending number: "))

# Get the absolute path of the file to use
file_input = input("Type the path of the file you wish to use: ")
file_path = os.path.expanduser(file_input)  # Expands `~` to the home directory

# Handle wildcard (`*`) if present
files = glob.glob(file_path)
if len(files) == 1:
    file = files[0]
elif len(files) > 1:
    print("Multiple files matched:", files)
    file = files[0]  # Choose the first match (or let user decide)
else:
    print("No files matched the provided path.")
    exit(1)

# Start the loop to test numbers
while minnum <= maxnum:
    print(f"Testing number: {minnum}")
    
    # Feed the current number as input to the specified program and capture the output
    try:
        process = subprocess.run([file], input=str(minnum), text=True, capture_output=True)
        output = process.stdout.strip()
    except FileNotFoundError:
        print(f"Error: The file {file} was not found or is not executable.")
        break

    # Append the output to a file
    with open("flag.txt", "a") as flag_file:
        flag_file.write(output + "\n")
    
    # Check for the flag in the output
    if "flag" in output:
        print("\nThe flag is the number")
        print("The number is:", minnum)
        break
    else:
        # Increment the number
        minnum += 1
