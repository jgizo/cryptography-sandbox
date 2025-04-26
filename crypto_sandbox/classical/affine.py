import math
ALPHA = 26

def _validate_key(a: int) -> None:
    if math.gcd(a, ALPHA) != 1:
        raise ValueError(f"'a' must be coprime with {ALPHA} (got {a}).")

def modular_inverse(a: int, m: int) -> int:
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
        
    raise ValueError(f"No modular inverse for a = {a} under modulo {m}")

def _affine(text: str, a: int, b: int, decrypt: bool = False) -> str:
    _validate_key(a)
    if decrypt:
        mul = modular_inverse(a, 26)
        add = -b
    else:
        mul = a
        add = b

    out = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            off  = ord(ch) - base
            # correct formulas:
            val = (mul * off + add) % ALPHA if not decrypt \
                  else (mul * (off + add)) % ALPHA   # add is negative here
            out.append(chr(base + val))
        else:
            out.append(ch)
    return "".join(out)

def encrypt(plaintext: str, a: int, b: int) -> str:
    """Affine-cipher encryption."""
    return _affine(plaintext, a, b, decrypt=False)

def decrypt(ciphertext: str, a: int, b: int) -> str:
    """Affine-cipher decryption."""
    return _affine(ciphertext, a, b, decrypt=True)

print(encrypt("AFFINE", 5, 8))
print(decrypt("IHHWVC", 5, 8))