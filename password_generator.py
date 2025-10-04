# password_generator.py
import random
import string

def generate_password(length, include_uppercase, include_special, include_digits):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")

    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ""
    special = string.punctuation if include_special else ""
    digits = string.digits if include_digits else ""
    all_characters = lower + uppercase + special + digits

    if not (include_uppercase or include_special or include_digits):
        raise ValueError("At least one character set (uppercase, special, digits) must be selected")

    all_characters = lower + uppercase + special + digits

    required_characters = []
    if include_uppercase:
        required_characters.append(random.choice(uppercase))
    if include_special:
        required_characters.append(random.choice(special))
    if include_digits:
        required_characters.append(random.choice(digits))

    remaining_length = length - len(required_characters)
    password = required_characters + [random.choice(all_characters) for _ in range(remaining_length)]
    random.shuffle(password)

    return "".join(password)

# Optional CLI wrapper (you can exclude from tests)
if __name__ == "__main__":
    length = int(input("Enter password length: ").strip())
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
    include_special = input("Include special characters? (yes/no): ").strip().lower() == "yes"
    include_digits = input("Include digits? (yes/no): ").strip().lower() == "yes"

    print(generate_password(length, include_uppercase, include_special, include_digits))
