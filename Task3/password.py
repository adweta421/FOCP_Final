import getpass

# File path for storing user information
file_path = "passwd.txt"

# Simple substitution cipher for password encryption

def encrypt_password(password):
    """
    Encrypts a password using a basic substitution cipher.

    Args:
        password (str): The password to be encrypted.

    Returns:
        str: The encrypted password.
    """
    return ''.join(chr((ord(char) + 3) % 128) for char in password)

# User class to represent each user
    
class User:
    """
    Represents a user with username, real name, and encrypted password.

    Attributes:
        username (str): The username of the user.
        real_name (str): The real name of the user.
        password (str): The encrypted password of the user.
    """
    def __init__(self, username, real_name, password):
        self.username = username
        self.real_name = real_name
        self.password = password

# Function to read user information from a file and return a list of User objects
def read_passwd_file(file_path):
    """
    Reads user information from a file and returns a list of User objects.

    Args:
        file_path (str): The file path to read user information from.

    Returns:
        list: A list of User objects.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            users = [User(*line.strip().split(':')) for line in lines]
        return users
    except FileNotFoundError:
        return []

# Function to write user information to a file
def write_passwd_file(file_path, users):
    """
    Writes user information to a file.

    Args:
        file_path (str): The file path to write user information to.
        users (list): A list of User objects.
    """
    with open(file_path, 'w') as file:
        for user in users:
            file.write(f"{user.username}:{user.real_name}:{user.password}\n")

# Function to check if a user exists in the user list
def user_exists(username, users):
    """
    Checks if a user with the given username exists in the user list.

    Args:
        username (str): The username to check for existence.
        users (list): A list of User objects.

    Returns:
        bool: True if the user exists, False otherwise.
    """
    return any(user.username == username for user in users)

# Function to validate a password for a given user
def validate_password(username, password, users):
    """
    Validates a password for a given user.

    Args:
        username (str): The username of the user.
        password (str): The password to validate.
        users (list): A list of User objects.

    Returns:
        bool: True if the password is valid for the user, False otherwise.
    """
    user = next((user for user in users if user.username == username), None)
    return user and encrypt_password(password) == encrypt_password(user.password)

# Function to add a new user to the system
def add_user(users):
    """
    Adds a new user to the system.

    Args:
        users (list): A list of User objects.
    """
    username = input("Enter new username: ")
    real_name = input("Enter real name: ")
    password = getpass.getpass("Enter password: ")

    if user_exists(username, users):
        
        print("Cannot add as username already exists.")
    else:
        users.append(User(username, real_name, password))
        write_passwd_file(file_path, users)
        print("User Created.")

# Function to delete a user from the system
def delete_user(users):
    """Delets the user from the system
    Args:
        users (list): A list of User objects.
    """
    username = input("Enter username: ")

    if user_exists(username, users):
        users[:] = [user for user in users if user.username != username]
        write_passwd_file(file_path, users)
        print("User Deleted")
    else:
        print("User not found")

# Function to change the password for a user
def change_password(users):
    """
    Changes the password for a user.

    Args:
        users (list): A list of User objects.
    """
    username = input("User: ")

    user = next((user for user in users if user.username == username), None)
    if user:
        current_password = getpass.getpass("Current Password: ")
        if validate_password(username, current_password, users):
            new_password = getpass.getpass("New Password: ")
            confirm_password = getpass.getpass("Confirm: ")

            if new_password == confirm_password:
                user.password = new_password
                write_passwd_file(file_path, users)
                print("Password changed")
            else:
                print("Passwords do not match")
        else:
            print("Invalid current password")
    else:
        print("User not found")

# Function for user login
def login(users):
    """
    Performs user login.

    Args:
        users (list): A list of User objects.
    """
    username = input("User: ")
    password = getpass.getpass("Password: ")

    if validate_password(username, password, users):
        print("Access granted")
    else:
        print("Access denied")

# Main program
users = read_passwd_file(file_path)

while True:
    print("\n1. Add User\n2. Delete User\n3. Change Password\n4. Login\n5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_user(users)
    elif choice == "2":
        delete_user(users)
    elif choice == "3":
        change_password(users)
    elif choice == "4":
        login(users)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
