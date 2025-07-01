import random
import string

def generate_password(length, use_digits=True, use_symbols=True, use_uppercase=True, use_lowercase=True):
    characters = ''
    
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase

    if not characters:
        return "Error: No character types selected for password generation."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")
    
    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_digits, use_symbols, use_uppercase, use_lowercase)

    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()