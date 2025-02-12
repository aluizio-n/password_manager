from cryptography.fernet import Fernet
import hashlib
import base64

def generate_key(master_password:str):
    """ generate a key based on user's master password """
    hash_password = hashlib.sha256(master_password.encode()).digest()
    return base64.urlsafe_b64encode(hash_password[:32])

def encrypt_password(password:str, key:bytes):
    """ encrypt the password with the given key """
    cipher = Fernet(key)
    return cipher.encrypt(password.encode())

def decrypt_password(encrypt_password:str, key:bytes):
    """ decrypt the stored password """
    cipher = Fernet(key)
    return cipher.decrypt(encrypt_password).decode()





