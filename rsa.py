from math import gcd
from sympy import mod_inverse

def generate_rsa_keys(p, q):
    """Generates RSA keys given two prime numbers p and q."""
    n = p * q
    phi = (p - 1) * (q - 1)

    # Find e such that 1 < e < phi and gcd(e, phi) == 1
    e = next(i for i in range(2, phi) if gcd(i, phi) == 1)

    # Find modular multiplicative inverse of e modulo phi
    d = mod_inverse(e, phi)

    return (e, n), (d, n)

def rsa_encrypt(plaintext, public_key):
    """Encrypts plaintext using the RSA public key."""
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]

def rsa_decrypt(ciphertext, private_key):
    """Decrypts ciphertext using the RSA private key."""
    d, n = private_key
    return ''.join(chr(pow(char, d, n)) for char in ciphertext)

# Example usage
if __name__ == "__main__":
    p = 17
    q = 23

    public_key, private_key = generate_rsa_keys(p, q)
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    plaintext = "hello"
    print("Original text:", plaintext)

    ciphertext = rsa_encrypt(plaintext, public_key)
    print("Ciphertext:", ciphertext)

    decrypted_text = rsa_decrypt(ciphertext, private_key)
    print("Decrypted text:", decrypted_text)
