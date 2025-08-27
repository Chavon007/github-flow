import random
import string

def generate_password(length=12, use_digits=True, use_special=True):
    """
    Generate a random password.
    
    Args:
        length (int): Length of the password (default: 12).
        use_digits (bool): Include digits (0–9).
        use_special (bool): Include special characters.
    
    Returns:
        str: Generated password.
    """
    # Base characters (letters)
    chars = string.ascii_letters  
    
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    # Ensure at least 1 character from each chosen category
    password = []
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase))

    # Fill the rest randomly
    password += random.choices(chars, k=length - len(password))

    # Shuffle to remove predictability
    random.shuffle(password)

    return ''.join(password)


# Example usage:
print(generate_password(16))
print(generate_password(20, use_special=False))
