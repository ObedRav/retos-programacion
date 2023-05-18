import string
import random

def password_generator(length: int = random.randint(8, 16)) -> str:
    characters = string.ascii_letters + string.digits
    password = random.choices(characters, k=length)
    return "".join(password)

print(password_generator())
