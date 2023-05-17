import string
import random

def password_generator(length: int) -> str:
    lower_case_letters = string.ascii_lowercase
    upper_case_letters = string.ascii_uppercase
    digits = string.digits
    
    password = random.choices(lower_case_letters + upper_case_letters + digits, k=random.randint(8, 16))

    return "".join(password)

print(password_generator(10))
    
    
    
    