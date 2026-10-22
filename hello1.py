# Assigning variables
# A variable is a name that stores a value so we can use it later.

# input() shows a prompt, waits for the user to type something, and
# returns what they typed as a string (text).
name = input("What is your name? ")

# input() always returns a string, so int() converts the text into a
# whole number. We need a number to do math with it later.
birthYear = int(input("What year were you born? "))

# These variables are set directly in the code instead of asked for.
hobby = "playing Tennis, hanging out with friends, and being with family"
currentYear = 2026


# Printing text using an f-string to format it
# Putting an f before the quotes lets us place variables inside {} and
# Python replaces each {variable} with its value when it prints.
print(f"Hello my name is {name}, my hobbies are {hobby}")

# Age calculation
# Subtracting the birth year from the current year gives the age.
# (This can be off by one if your birthday hasn't happened yet this year.)
age = currentYear - birthYear

print(f"{name}, you are {age} years old")
