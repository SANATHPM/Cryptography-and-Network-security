import random

# Function to compute modular exponentiation
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:  # If exp is odd
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result

# Key generation
def generate_keys(p):
    e1 = random.randint(2, p - 2)  # Primitive root modulo p
    d = random.randint(2, p - 2)  # Private key
    e2 = mod_exp(e1, d, p)        # Public key part
    return (e1, e2, d)

# Encryption
def encrypt(p, e1, e2, r, m):
    c1 = mod_exp(e1, r, p)
    c2 = (m * mod_exp(e2, r, p)) % p
    return (c1, c2)

# Decryption
def decrypt(p, c1, c2, d):
    s = mod_exp(c1, d, p)  # Compute shared secret
    s_inv = mod_exp(s, p - 2, p)  # Compute modular inverse of s
    m = (c2 * s_inv) % p
    return m

# Example usage
if __name__ == "__main__":
    # Prime number
    p = 467  # Choose a large prime
    message = 123  # Plaintext message
    r = random.randint(2, p - 2)  # Random value for encryption

    # Key generation
    e1, e2, d = generate_keys(p)
    print(f"Public key: (e1={e1}, e2={e2}, p={p})")
    print(f"Private key: d={d}")

    # Encryption
    c1, c2 = encrypt(p, e1, e2, r, message)
    print(f"Ciphertext: (c1={c1}, c2={c2})")

    # Decryption
    decrypted_message = decrypt(p, c1, c2, d)
    print(f"Decrypted message: {decrypted_message}")
