import random
import string

def generate_password(length):
    """Generate a random password with letters, digits, and symbols."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Simple Password Generator ===")
    try:
        length = int(input("Enter desired password length: "))
        if length < 4:
            print("⚠️ Password length should be at least 4 characters.")
            return

        password = generate_password(length)
        print(f"\nYour generated password is: {password}")

    except ValueError:
        print("⚠️ Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
