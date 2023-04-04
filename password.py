import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation
    
    all_characters = lowercase_letters + uppercase_letters + digits + symbols
    
    password = "".join(random.sample(all_characters, length))
    return password
password = generate_password(12)
print(password)