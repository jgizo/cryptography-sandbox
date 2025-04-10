import math

# rail_fence.py
def encrypt(plaintext: str, key: int) -> str:
    #key = "rails"
    plaintext = ''.join([i for i in plaintext if i.isalpha()])
    rails = [[] for _ in range(key)]

    rail_index = 0
    direction = 1


    for i, c in enumerate(plaintext):
        rails[rail_index].append(c)

        if rail_index == 0:
            direction = 1
        elif rail_index == key - 1:
            direction = -1
        
        rail_index += direction
    
    return " ".join("".join(rail) for rail in rails)


def decrypt(ciphertext: str, key: int) -> str:
    # TODO: Implement rail fence decryption
    pass

print(encrypt("WE ARE DISCOVERED. RUN AT ONCE.", 4))