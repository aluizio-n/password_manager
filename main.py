from crypto_manager import generate_key, encrypt_password, decrypt_password
from database_manager import create_db, save_password, get_passwords
from utils import generate_password

import getpass

def menu():
    print("\nPassword manager - CLI")
    print("1. Add password")
    print("2. List passwords")
    print("3. Exit")

def main():
    master_password = getpass.getpass("Type your master password: ")
    key = generate_key(master_password)
    create_db()

    while True:
        menu()
        option = input("Choose an option: ")

        if option == "1":
            site = input("Site: ")
            user = input("User: ")
            password = input("Type a password or just hit enter to generate a random password: ")

            if not password:
                password = generate_password()
                print(f"Generated password: {password}")

            encrypt_pass = encrypt_password(password, key)
            save_password(site, user, encrypt_pass)
            print("Password saved!")

        elif option == "2":
            data = get_passwords()
            if not data:
                print("There is no password saved.")
                return
            print("\nPasswords stored:")
            for _, site, user, encrypt_pass in data:
                try:
                    real_password = decrypt_password(encrypt_pass, key)
                except:
                    real_password = "[ERROR IN DECRYPT]"

                print(f"🔹 \nSite: {site} \nUser: {user} \nPassword: {real_password}")

        elif option == "3":
            print("Bye bye...")
            break

        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()