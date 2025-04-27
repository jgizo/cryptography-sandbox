def analyze_frequency(text: str) -> dict:
    char_freq = dict()

    for c in text:
        if c in char_freq.keys():
            char_freq[c] += 1
        else:
            char_freq[c] = 1
    
    return char_freq

print(analyze_frequency("HELLO"))