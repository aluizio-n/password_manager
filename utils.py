import random
import string

def generate_password(size=16):
    """" generates a random password """
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(characters) for _ in range(size))
