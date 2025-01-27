import string
from math import gcd

def modular_inverse(a, m):
    """Find the modular multiplicative inverse of a under modulo m."""
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return None

def affine_encrypt(text, a, b):
    """Encrypts the text using the Affine Cipher."""
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")

    text = text.lower()
    encrypted_text = ""
    alphabet = string.ascii_lowercase

    for char in text:
        if char.isalpha():
            x = alphabet.index(char)
            encrypted_char = (a * x + b) % 26
            encrypted_text += alphabet[encrypted_char]
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged

    return encrypted_text

def affine_decrypt(ciphertext, a, b):
    """Decrypts the ciphertext using the Affine Cipher."""
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")

    a_inv = modular_inverse(a, 26)
    if a_inv is None:
        raise ValueError("Modular inverse of 'a' does not exist.")

    ciphertext = ciphertext.lower()
    decrypted_text = ""
    alphabet = string.ascii_lowercase

    for char in ciphertext:
        if char.isalpha():
            y = alphabet.index(char)
            decrypted_char = (a_inv * (y - b)) % 26
            decrypted_text += alphabet[decrypted_char]
        else:
            decrypted_text += char  # Non-alphabetic characters remain unchanged

    return decrypted_text

# Example usage
if __name__ == "__main__":
    plaintext = "hello world"
    a = 5
    b = 8

    print("Original text:", plaintext)

    encrypted = affine_encrypt(plaintext, a, b)
    print("Encrypted text:", encrypted)

    decrypted = affine_decrypt(encrypted, a, b)
    print("Decrypted text:", decrypted)
