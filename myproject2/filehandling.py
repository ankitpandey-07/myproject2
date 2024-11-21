import os

# File to store user data
DATA_FILE = "users.txt"

# Ensure the file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        pass  # Create the file if it doesn't exist

# Register a new user
def register():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    # Check if username already exists
    with open(DATA_FILE, "r") as file:
        for line in file:
            stored_username, _ = line.strip().split(",")
            if username == stored_username:
                print("Username already exists! Try a different one.")
                return

    # Save the new user's data
    with open(DATA_FILE, "a") as file:
        file.write(f"{username},{password}\n")
    print("Registration successful!")

# Login a user
def login():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    # Check if username and password match
    with open(DATA_FILE, "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(",")
            if username == stored_username and password == stored_password:
                print("Login successful!")
                return True
    print("Invalid username or password.")
    return False

# Fetch all registered users
def fetch_users():
    print("\nRegistered Users:")
    with open(DATA_FILE, "r") as file:
        for line in file:
            username, _ = line.strip().split(",")
            print(f"- {username}")

# Main menu
def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Fetch All Users")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            fetch_users()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
