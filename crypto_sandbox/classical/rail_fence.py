import math

# rail_fence.py
def encrypt(plaintext: str, key: int) -> str:
    #key = "rails"
    plaintext = ''.join([i for i in plaintext if i.isalpha()])
    rails = [[] for _ in range(key)]

    for i, c in enumerate(plaintext):
        if i % 2 == 1:
            rails[1].append(c)
        elif math.cos(math.radians(i*90)) == 1:
            rails[0].append(c)
        elif math.cos(math.radians(i*90)) == -1:
            rails[2].append(c)
    
    return " ".join("".join(rail) for rail in rails)


def decrypt(ciphertext: str, key: int) -> str:
    # TODO: Implement rail fence decryption
    pass

print(encrypt("WE ARE DISCOVERED. RUN AT ONCE.", 3))