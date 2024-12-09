#!/usr/bin/env python3

input_string = input("Enter a string here: ")
reversed_string = ''

for char in input_string:
    reversed_string = char + reversed_string

print(f"Reversed string: {reversed_string}")
