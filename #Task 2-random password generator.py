import random 
import string

def generate_password(length,use_letters=True,use_numbers=True,use_symbols=True):
    characters=""

    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character set (letters,numbers,symbols) must be selected.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the password generator------")

    length=int(input("Enter the desired password lenth: "))
    use_letters=input("Include letters?(yes/no): ").lower()=='y'
    use_numbers=input("Include numbers?(yes/no): ").lower()=='y'
    use_symbols=input("Include symbols?(yes/no): ").lower()=='y'

    password=generate_password(length,use_letters,use_numbers,use_symbols)

    if password:
        print("Generated password is: ",password)

if __name__ == "__main__":
    main()
    
        
