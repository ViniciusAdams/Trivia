#collect user preferences
# lenght
# should contain uppercase
# should contain special
# should contain digits

# get all available characthers 
# randomly pick characthers up to the lenght 
# ensure we have at least one of each character type
# ensure lenght is valid


import random
import string

def generate_password():
    lenght = int(input("Enter the disere password lenght").strip())
    include_uppercase = input("Include uppercase letters? (yes/no)").strip().lower()
    include_special = input("Include special letters? (yes/no)").strip().lower()
    include_digitals = input("Include uppercase letters? (yes/no)").strip().lower()

    if lenght < 4:
        print ("Password lenght must be at least 4 characthers")
        return 

    lower = string.ascii_lowercase
    print(lower)

generate_password()   