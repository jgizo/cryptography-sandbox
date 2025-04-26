ALPHA = 26

def _vigenere(text: str, key: str, decrypt: bool = False) -> str:
    key = key.lower()
    key_len = len(key)
    if key_len == 0:
        raise ValueError("Key must not be empty.")

    out   = []
    k_pos = 0

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            offset = ord(ch) - base
            k = ord(key[k_pos % key_len]) - ord('a')

            if decrypt:
                val = (offset - k) % ALPHA
            else:
                val = (offset + k) % ALPHA

            out.append(chr(base + val))
            k_pos += 1
        else:
            out.append(ch)

    return "".join(out)

def encrypt(plaintext: str, key: str) -> str:
    return _vigenere(plaintext, key, decrypt=False)

def decrypt(ciphertext: str, key: str) -> str:
    return _vigenere(ciphertext, key, decrypt=True)


