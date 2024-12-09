#!/usr/bin/env python3

import string
import secrets

print("""   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   @                                                  @
   @       $$$$$$  $$     $  $$$$$$  $$$$$$  $$     $ @
   @      $$   $  $$     $  $$      $$      $$$    $  @
   @     $$   $  $$     $  $$      $$      $$ $   $   @
   @    $$$$$$  $$  $  $  $$ $$$  $$$$    $$  $  $    @
   @   $$      $$ $ $ $  $$   $  $$      $$   $ $     @
   @  $$      $$$   $$  $$   $  $$      $$    $$      @
   @ $$      $$     $  $$$$$$  $$$$$$  $$     $       @
   @                                                  @
   @             $$$$$$  $$$$$$  $$$$$$  $$$$$$       @
   @            $$      $$   $  $$   $  $$   $        @
   @           $$      $$   $  $$   $  $$   $         @
   @          $$$$    $$   $  $$   $  $$   $          @
   @            $$$  $$   $  $$   $  $$   $           @
   @            $$  $$   $  $$   $  $$   $            @
   @       $$$$$$  $$$$$$  $$$$$$  $$$$$$             @
   @                                                  @
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   """)

'''                                                   **TODO**
   -utilize upper case characters, lower case characters, integers, and special characters (only certain ones may work)
    -accept input for desired password length, anywhere from 4-30 characters
    -include a means of cipher by selection a random character and changing it based on a specific criteria
    -all digits must be randomized
    -check python library as there may be a secure random generator
    -possibly provide a hash for the password as a means of evaluating it against a publicly available hash list to ensure originality
    -be able to have the use select the option of using any combination of upper/lower case characters, integers, or special characters
    -contain an interactive menu
    -provide export functionality
    '''

# function used to have the user determine how many characters they'd like their password to be and then to confirm their request
def passlen():
    while True:
        try:
            print("""Time to choose how many characters you'd like to have in your password!
The recommended number of characters is 20, however you may choose between 8 and 50 characters.

                         Enter 99 to exit at any time
""")
            passlen_select = int(input("Password length: "))

            if passlen_select == 99:
                print("\nExiting password length selector\n")
                return None

            if passlen_select >= 8 and passlen_select <= 50:
                while True:
                    try:
                        doubt_check = input("Are you sure? (Y/N) ").lower() # used to make y/n choice case insensitive
                        if doubt_check == "y":
                            print(f"\nYou have chosen to make your password ({passlen_select}) characters")
                            return passlen_select
                        elif doubt_check == "n":
                            print("\nOkay let's try again")
                            break
                        else: # stops user from putting in anything but y or n
                            print("Invalid choice, please choose (Y/N)")
                    except ValueError: # catch for non-valid input (special characters, whitespace, etc)
                        print("Invalid choice, please choose (Y/N)")

            else:
                print(f"\n({passlen_select}) is an invalid amount of characters!\nPlease enter a number between 8 and 50\n")

        # catches exception for improper input (not an integer)
        except ValueError:
            print("\nInvalid input. Please enter a number between 8 and 50\n")

# function used to build a 4, 5, or 6 digit pin. User can select how long they'd like for their pin to be made to
def num_pass_len():
    while True:
        try:
            print("""Welcome to the pin selector!
Please select what length to make your pin.

                         Enter 99 to exit at any time
""")
            num_passlen_select = int(input("Pin length: "))

            if num_passlen_select == 99:
                print("\nExiting pin length selector\n")
                return None

            if num_passlen_select >= 4 and num_passlen_select <= 6:
                while True:
                    try:
                        doubt_check = input("Are you sure? (Y/N) ").lower()
                        if doubt_check == "y":
                            print(f"\nYou have chosen to make your pin ({num_passlen_select}) digits")
                            return num_passlen_select
                        elif doubt_check == "n":
                            print("\nOkay let's try again")
                            break
                        else:
                            print("Invalid choice, please choose (Y/N)")
                    except ValueError:
                        print("Invalid choice, please choose (Y/N)")

            else:
                print(f"\n({num_passlen_select}) is an invalid amount of digits!\nPlease enter a number between 4 and 6\n")

        # catches exception for improper input (not an integer)
        except ValueError:
            print("\nInvalid input. Please enter a number between 4 and 6\n")

''' function used to create a fully random password with a minimum of (2) uppercase, (2) lowercase, (2) digits, & (2) special characters
    function also gives the user the ability to pick another ranodm selection'''
def fullpw_funct():
    print("""
  You have selected option 1
  """)
    passlength = passlen()
    mass_combo = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(mass_combo) for i in range(passlength))
        if (sum(c.islower() for c in password) >= 2 and 
            sum(c.isupper() for c in password) >= 2 and 
            sum(c.isdigit() for c in password) >= 2 and 
            sum(c in string.punctuation for c in password) >= 2):
            print(f"Your randomly generated password is: {password}\n")
            confirmation = input("Do you like this password? (Y/N) ").lower()
            if confirmation == "y":
                print(f"\nCongrats your now password is: {password}\n")
                break
            elif confirmation == "n":
                continue
            elif confirmation == "99":
                print("Exiting!")
                break
            else:
                print("\nInvalid choice, please choose (Y/N)")

''' function used to create a letter ONLY password, this password will no matter what have at least (3) upper or (3) lower case ascii characters'''
def letterpw_funct():
    print("""
  You have selected option 2
  """)
    passlength = passlen()
    alphabet = string.ascii_letters
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(passlength))
        if (sum(c.islower() for c in password) >= 3 and sum(c.isupper() for c in password) >= 3):
            print(f"Your randomly generated password is: {password}\n")
            confirmation = input("Do you like this password? (Y/N) ").lower()
            if confirmation == "y":
                print(f"\nCongrats your now password is: {password}\n")
                break
            elif confirmation == "n":
                continue
            elif confirmation == "99":
                break
                print("Exiting!")
            else:
                print("\nInvalid choice, please choose (Y/N)")

''' pin function, gives the user a choice between a 4 to 6 digit pin. As with previous functions this one allows the user to reroll a random password'''
def numpw_funct():
    print("""
  You have selected option 3
  """)
    pin_length = num_pass_len()
    digits = string.digits
    while True:
        password = ''.join(secrets.choice(digits) for i in range(pin_length))
        print(f"Your randomly generated password is {password}\n")
        confirmation = input("Do you like this new pin? (Y/N) ").lower()
        if confirmation == "y":
            print(f"\nCongrats your new pin is: {password}\n")
            break
        elif confirmation == "n":
            continue
        elif confirmation == "99":
            print("Exiting!")
            break
        else:
            print("\nInvalid choice, please choose (Y/N)\n")

''' function that allows the user to only use letters and numbers for their password. Password criteria is a minimum of (2) uppcase, (2) lowercase, and (2) digits
    even though in theory this function only requires (6) digits the program is set for a minimum password length of (8)'''
def combopw_funct():
    print("""
  You have selected option 4
  """)
    passlength = passlen()
    combo_abc = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(combo_abc) for i in range(passlength))
        if (sum(c.islower() for c in password) >= 2 and sum(c.isupper() for c in password) >=2
            and sum(c.isdigit() for c in password) >= 2):
            print(f"Your randomly generated password is: {password}\n")
            confirmation = input("Do you like this new pin? (Y/N) ").lower()
            if confirmation == "y":
                print(f"\nCongrats your new pin is: {password}\n")
                break
            elif confirmation == "n":
                continue
            elif confirmation == "99":
                print("Exiting!")
                break
            else:
                print("\nInvalid choice, please choose (Y/N)")

''' main function of the program, includes a welcome message, printed menu selection, and a switch statement offering the user full control of the program.
    The exit is set to the user typing "99" which is vastly different to the criteria for other options in the menu which should keep any "accidental" exits
    from ever occuring. 

    In the future this will be updated to include a feature allowing a user to link a username/login e-mail with a specific random password generated into a 
    password manager suite. Eventually I'll figure out a way to auto-copy the generated password into the user's clipboard so they can manually paste it into 
    a new login screen.'''
while True:
    try:
        print("""          Welcome to the password generator 5000

  Please select from one of the options below

   1. Create a standard password using letters (upper & lower case), numbers, and special characters
   2. Create a password using only letters
   3. Create a password using only numbers
   4. Create a password using only letters and numbers

                  ****99. to Exit****
""")

        selection = int(input("Which option would you like to perform: "))

        if selection == 1:
            fullpw_funct()
        elif selection == 2:
            letterpw_funct()
        elif selection == 3:
            numpw_funct()
        elif selection == 4:
            combopw_funct()
        elif selection == 99:
            print("""
                     Exiting!!!""")
            break
        else:
            print("""
Invalid selection
""")
    except Exception:
        print("\nInvalid selection, please choose an option\n")

# This program was written by Richard Smith (December 2024) as a hands on python project for further skill enhancement
# Understand that while this is a publicly available program I also wrote this while at community college having only had
#   a single python class. The security of this program is likely very minimal and if the 'secrets' module from the python
#   built in library ever becomes compromised then this program isn't even useful as a paper weight
# I mostly hope anyone who would use this is doing so just to help get a better understanding of how to do basic functions
#   from within python. I purposefully (<-- pretty sure I messed that spelling up!) wrote the program to be much more complex
#   than it needed to be. 
# This program could have probably been 30 lines max, but adding all the other stuff and testing has definitely helped me in
#   my journey and I hope it does others as well.

# Make Peace or Die
# 1st Bn 5th Mar
# Cherokee Co
# 2nd Plt
