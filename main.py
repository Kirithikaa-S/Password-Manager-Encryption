import json
from cryptography.fernet import Fernet

# Load Encryption Key
with open("key.key", "rb") as file:
    key = file.read()

fernet = Fernet(key)


# Encrypt Password
def encrypt_password(password):
    return fernet.encrypt(password.encode()).decode()


# Decrypt Password
def decrypt_password(password):
    return fernet.decrypt(password.encode()).decode()


# Add Password
def add_password():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    encrypted_password = encrypt_password(password)

    with open("passwords.json", "r") as file:
        data = json.load(file)

    data.append({
        "website": website,
        "username": username,
        "password": encrypted_password
    })

    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)

    print("✅ Password Saved Successfully!")


# View Passwords
def view_passwords():
    with open("passwords.json", "r") as file:
        data = json.load(file)

    if len(data) == 0:
        print("No passwords stored.")
        return

    for item in data:
        print("\n-------------------")
        print("Website :", item["website"])
        print("Username:", item["username"])
        print("Password:", decrypt_password(item["password"]))
        print("-------------------")


# Search Password
def search_password():
    website = input("Enter Website Name: ")

    with open("passwords.json", "r") as file:
        data = json.load(file)

    found = False

    for item in data:
        if item["website"].lower() == website.lower():
            print("\nWebsite :", item["website"])
            print("Username:", item["username"])
            print("Password:", decrypt_password(item["password"]))
            found = True
            break

    if not found:
        print("Password not found.")


# Delete Password
def delete_password():
    website = input("Enter Website Name to Delete: ")

    with open("passwords.json", "r") as file:
        data = json.load(file)

    new_data = []

    for item in data:
        if item["website"].lower() != website.lower():
            new_data.append(item)

    with open("passwords.json", "w") as file:
        json.dump(new_data, file, indent=4)

    print("✅ Password Deleted Successfully!")


# Main Menu
while True:

    print("\n========== PASSWORD MANAGER ==========")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Search Password")
    print("4. Delete Password")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_password()

    elif choice == "2":
        view_passwords()

    elif choice == "3":
        search_password()

    elif choice == "4":
        delete_password()

    elif choice == "5":
        print("Thank You For Using Password Manager!")
        break

    else:
        print("Invalid Choice! Try Again.")