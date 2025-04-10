import math

# rail_fence.py
def encrypt(plaintext: str, key: int, keep_nonalpha: bool) -> str:
    #key = "rails"

    if keep_nonalpha:
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
    length = len(ciphertext)
    rail_pattern = [['' for _ in range(length)] for _ in range(key)]

    rail_index = 0
    direction = 1

    #Trace rail pattern
    for i in range(length):
        rail_pattern[rail_index][i] = '*'

        if rail_index == 0:
            direction = 1
        elif rail_index == key - 1:
            direction = -1

        rail_index += direction

    rail_index = 0
    for i in range(key):
        for j in range(length):
            if rail_pattern[i][j] == '*' and rail_index < length:
                rail_pattern[i][j] = ciphertext[rail_index]
                rail_index += 1

    plaintext = []
    rail_index = 0
    direction = 1

    for i in range(length):
        plaintext.append(rail_pattern[rail_index][i])

        if rail_index == 0:
            direction = 1
        elif rail_index == key - 1:
            direction = -1

        rail_index += direction

    return ''.join(plaintext)