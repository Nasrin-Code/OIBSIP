import string
import secrets

while True:
    try:
        length = int(input("Enter Password Length: "))
        if length>0:
            break
        else:
            print("Password Length must be greater than 0.")
    except ValueError:
        print("Enter a valid input.")


include_upper = input("Include Uppercase Letters? (y/n): ")
include_lower = input("Include Lowercase Letters? (y/n): ")
include_digits = input("Include Digits? (y/n): ")
include_punctuation = input("Include Punctuation? (y/n): ")

characters = ""
if include_upper == "y":
    characters += string.ascii_uppercase
if include_lower == "y":
    characters += string.ascii_lowercase
if include_digits == "y":
    characters += string.digits
if include_punctuation == "y":
    characters += string.punctuation
if characters == "":
    print("You must select atleast one character type.")
else:
    password = ""
    for i in range(length):
        password += secrets.choice(characters)
    print("Generated Password:", password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digits = any(char.isdigit() for char in password)
    has_punctuation = any(char in string.punctuation for char in password)

    if length>=12 and has_upper and has_lower and has_digits and has_punctuation:
        print("Strength: Strong")
    elif length>=8:
        print("Strength: Medium")
    else:
        print("Strength: Low")