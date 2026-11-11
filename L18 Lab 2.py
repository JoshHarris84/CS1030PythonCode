# L18 Lab 2: Problem Solving - Secure Building Access
# Checks a person's access card first, and only checks their PIN if the card is valid.

card_valid = input("Is the access card valid? (y/n): ").strip().lower() == "y"

if not card_valid:
    print("Invalid access card")
else:
    print("Access card accepted")

    pin_correct = input("Is the PIN correct? (y/n): ").strip().lower() == "y"

    if pin_correct:
        print("Access granted")
    else:
        print("Incorrect PIN")

# Why is the PIN condition not evaluated when the access card is invalid?
# The PIN check is nested inside the "else" branch, so it only runs when
# card_valid is True. If the card is invalid, the "if not card_valid" branch
# runs, prints "Invalid access card", and the program skips the whole else
# block, so the PIN is never asked for or checked. This follows the
# requirement that the card must be checked first: there is no reason to check
# a PIN for someone whose card is already rejected, and it means an
# unauthorized person never gets the chance to try guessing PINs.
