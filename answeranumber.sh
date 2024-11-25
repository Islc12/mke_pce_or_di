#!/bin/bash

# these numbers can change, simply set it to where you want the script to start & end at
minnum=8433000
maxnum=8434000

# Start the loop to test numbers
while [ $minnum -le $maxnum ];
do
   echo "Testing number: $minnum"

    # feed the current number as input to the pickanumber program and stores as a variable
    output=$(echo "$minnum" | ./pickanumber)

    # redirects and appends the variable into a file that we can reference later if needed
    echo "$output">>flag.txt

    # if statement that will go through and find the flag sentence as well as catch
    # the number that was used when that flag expression was found
    if echo "$output" | grep "flag";
    then
       echo "" # blank line just added to make output easier to read
       echo "The number is: $minnum"
       break # ends the program as it is no longer neccessary to run
    else
    # increment the number through each loop
    ((minnum++))
    fi
done

