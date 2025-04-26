def encrypt(plaintext: str, shift: int) -> str:
    result = list()

    for c in plaintext:
        if c.isalpha():
            base = 'A' if c.isupper() else 'a'
            offset = ord(c) - ord(base)
            shifted = (offset + shift) % 26
            new_char = chr(shifted + ord(base))
            result.append(new_char)
        else:
            result.append(c)
    
    return ''.join(result)

def decrypt(ciphertext: str, shift: int) -> str:
    return encrypt(ciphertext, shift*-1)

def ROT13(plaintext: str, shift: int) -> str:
    return encrypt(plaintext, 13)
