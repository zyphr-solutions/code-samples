"""
Create example database.
"""

import os
import json

from app import bcrypt


def encrypt_users(users):
    """
    Encrypt the password for every user in the given users dictionary of users.
    Check the contents of the dictionary before and after encryption via print statements.
    """
    print("\nShould be unencrypted:")
    for username in users:
        print(users[username])

    for username in users.keys():
        users[username]["password"] = bcrypt.generate_password_hash(
            users[username]["password"]
        ).decode("utf-8")

    print("\nShould be encrypted:")
    for username in users:
        print(users[username])
    print("\n")

    return users


def init_data():
    """
    Get unencrypted dictionary of users from users_unencrypted.py and encrypt dictionary.
    Adds or refreshes any existing users.py to contain a newly encrypted dictionary of users.
    """
    input_path = os.path.join("data", "users_unencrypted.py")
    output_path = os.path.join("data", "users.py")

    if os.path.exists(input_path):
        input_path = "".join(input_path.split(".")[:-1])
        input_module = __import__(input_path.replace("/", "."), fromlist=[None])
        users = encrypt_users(input_module.USERS)
        with open(output_path, "w") as file:
            file.write("USERS = ")
            json.dump(users, file)
    else:
        raise Exception(f"File \"{input_path}\" is undefined.")


if __name__ == "__main__":
    init_data()
