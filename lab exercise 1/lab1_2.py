import re

def validate_username(username):
    # Username must contain only alphabetical characters
    return username.isalpha()

def validate_password(password):
    # Password must be at least 7 characters long
    if len(password) < 7:
        return False
    
    # Password must contain at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False
    
    # Password must contain at least one digit
    if not any(char.isdigit() for char in password):
        return False
    
    # Password must contain at least one special character
    special_characters = r"@_!#$%^&*()<>??/\|}{~:"
    if not re.search(rf"[{re.escape(special_characters)}]", password):
        return False
    
    return True

def main():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if not validate_username(username):
        print("Username must contain only alphabetical characters.")
    elif not validate_password(password):
        print("Password must be at least 7 characters long, contain at least one uppercase letter, one digit, and one special character.")
    else:
        print("Username and password are valid.")

if __name__ == "__main__":
    main()
