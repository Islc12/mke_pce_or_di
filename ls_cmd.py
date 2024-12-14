#!/usr/bin/env python3

import subprocess
import os
import glob

while True:
    # standard input for searching for a file by name
    file_input = input("\nType the directory whose contents you wish to view or enter \'exit\' to quit: ")

    # allows the user to use OS specific searching criteria such as ~ or / in *nix
    file_path = os.path.expanduser(file_input)

    # *nix specific feature that allows for globbing such as the use of * or ?
    files = glob.glob(file_path)

    if file_input.lower() == "exit":
        print("Exiting")
        break
    if not files:
        print(f"No directories exist called [{file_input}] on the system")

    else:
        print(f"\nThe contents of {files} is:")

        # simple for loop that will run through the input and output the result
        for file in files:
            # process is the variable used to run a command, in this case the ls command with the -l and -Q arguments
            # -Q is used to provide quotes around file names, while not always neccessary this is useful for files that have spaces in their names
            #    even if its unnecessary to that specific file it also doesn't hurt to use quotes
            process = subprocess.run(["ls", "-l", "-a", "-Q", file], text=True, capture_output=True)
            # this part uses the .stdout to ensure the output of the file is printed to standard output (the screen)
            # strip() is added so that unncessary whitespace is removed from the output such as leading or trailing new lines
            print(process.stdout.strip())
