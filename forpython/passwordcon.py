import hashlib
import os

def hash_password(password: str):
    salt = os.urandom(16)
    salted_password = salt + password.encode('utf-8')
    password_hash = hashlib.sha256(salted_password).hexdigest()
    return salt,password_hash

def verify_password(stored_salt: bytes,stored_hash: str,input_password: str):
    salted_password = stored_salt + input_password.encode('utf-8')
    input_hash = hashlib.sha256(salted_password).hexdigest()
    return input_hash == stored_hash

if __name__ == "__main__":
    password = input("Enter a password to hash:")
    salt, hashed_password = hash_password(password)
    print("password hashed sucessfully..")
    print(f"Salt:{salt.hex()}")
    print(f"Hashed password: {hash_password}")

    input_password = input("Enter the password to verify")

    if verify_password(salt, hashed_password, input_password):
        print("password verified sucessfully!")
    else:
        print("password verified failed!")


