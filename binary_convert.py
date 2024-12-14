#!/usr/bin/env python3

print("""
    11111111111111111111111111111111111
    1                                 1
    1        0000      0000    00000  1
    1       00  0    00   00  00   00 1
    1      00   0        00  00   00  1
    1     00    0      00   000000    1
    1    00    0     00    00    00   1
    1   00   00    00     00    00    1
    1  00  00    00      00    00     1
    1 00000    0000000  00000000      1
    1                                 1
    11111111111111111111111111111111111
""")

print("\nType (exit) to leave the program at any time\n")

while True:
    try:
        decimal_input = input("Enter a decimal number from 0 to 255 to be converted into binary: ").lower()

        if decimal_input == "exit":
            print("\nExiting!")
            break

        # sets a parameter that if the input isn't a digit or if the digit is greater than 255 or less than 0 it is invalid
        elif not decimal_input.isdigit() or int(decimal_input) > 255 or int(decimal_input) < 0:
            print("\nInvalid input")
            continue

        # gives the program something to output if the input is (0)
        elif int(decimal_input) == 0:
            print("\nBinary conversion: 00000000")

            # after previous checks this becomes the 'meat and potatoes' of the program
        else:
            # the first thing that happens is we take the valid input for decimal_input and convert it into an integer
            decimal_input = int(decimal_input)

            # initializes the variable binary with an empty string
            binary = ''

            ''' this portion does the math of our program, taking the modulo of input and running it against (2) which
                will force the result to be either a (0) or (1), the functioning numbers of binary. After running modulo
                the program uses floor division to divide the number by (2) forcing a remaninder that we will run modulo (2)
                against again. Finally after the program runs until the final result is (0) it will print the binary output
                of the decimal number input
            '''
            while int(decimal_input) > 0:
                binary = str(decimal_input % 2) + binary
                decimal_input //= 2

            # reassigns variable binary to equal binary with right justification (rjust) with 8 total positions and padding whitespace with (0)
            binary = binary.rjust(8, '0')

            print(f"\nBinary conversion: {binary}")

    except ValueError:
        print("\nInvalid input")
