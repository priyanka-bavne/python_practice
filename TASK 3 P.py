import random
import string

def generate_password(length, use_special_chars=True, use_numbers=True, use_uppercase=True):
    characters = string.ascii_lowercase  # Start with lowercase letters

    if use_uppercase:
        characters += string.ascii_uppercase  # Add uppercase letters if specified

    if use_numbers:
        characters += string.digits  # Add digits if specified

    if use_special_chars:
        characters += string.punctuation  # Add special characters if specified

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'

        password = generate_password(length, use_special_chars, use_numbers, use_uppercase)
        print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()