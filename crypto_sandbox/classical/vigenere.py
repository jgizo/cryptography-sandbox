def encrypt(plaintext: str, key: str) -> str:
    encryption = list()
    key_lower = key.lower()

    for i in range(0, len(plaintext)):
        key_i = i % len(key) #keep the index rotating in key to adjust for when index returns to 0
        base = 'A' if plaintext[i].isupper() else 'a'

        p_i = ord(plaintext[i]) - ord(base)
        k_i = ord(key_lower[key_i]) - ord('a')
        c_i = ((p_i + k_i) % 26) + ord(base)

        encryption.append(chr(c_i))

    return ''.join(encryption)

def decrypt(ciphertext: str, key: str) -> str:
    decryption = list()
    key_lower = key.lower()

    for i in range(0, len(ciphertext)):
        key_i = i % len(key)
        base = 'A' if ciphertext[i].isupper() else 'a'

        c_i = ord(ciphertext[i]) - ord(base)
        k_i = ord(key_lower[key_i]) - ord('a')
        p_i = ((c_i - k_i) % 26) + ord(base)

        decryption.append(chr(p_i))

    return ''.join(decryption)