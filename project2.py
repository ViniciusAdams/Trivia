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
    lenght = int(input("Enter the disere password lenght:").strip())
    include_uppercase = input("Include uppercase letters? (yes/no)=").strip().lower()
    include_special = input("Include special letters? (yes/no)=").strip().lower()
    include_digits = input("Include uppercase letters? (yes/no)=").strip().lower()

    if lenght < 4:
        print ("Password lenght must be at least 4 characthers")
        return 

    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""
    all_characters = lower + uppercase + special + digits

    required_characters = []
    if include_uppercase == "yes":
        required_characters.append(random.choice(uppercase))
    if include_special == "yes":
        required_characters.append(random.choice(special))
    if include_digits == "yes":
        required_characters.append(random.choice(digits))

    remaining_lenght = lenght - len(required_characters)
    password = required_characters

    for _ in range(remaining_lenght):
        character = random.choice(all_characters)
        password.append(character)

    random.shuffle(password)
    str_password = "".join(password)
    return str_password

password = generate_password()
print(password)

#testing github actions