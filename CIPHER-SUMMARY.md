# Full Cipher Techniques Summary

| Cipher / Technique          | Cipher Type                   | Key Input                         | Core Mechanism |
|------------------------------|--------------------------------|-----------------------------------|----------------|
| **Caesar Cipher**             | Substitution Cipher           | Integer shift (e.g., 3)            | Shift each letter forward by a fixed amount. |
| **Vigenère Cipher**           | Substitution Cipher (Polyalphabetic) | Word/phrase (e.g., "LEMON")        | Repeating key determines different shift per character. |
| **Monoalphabetic Substitution** | Substitution Cipher           | 26-letter key (e.g., scrambled alphabet) | Fixed one-to-one letter mapping based on a shuffled alphabet. |
| **Atbash Cipher**             | Substitution Cipher           | None                              | Reflect each letter across the alphabet (A↔Z, B↔Y, etc.). |
| **Affine Cipher**             | Substitution Cipher           | Two integers (a, b) where a is coprime with 26 | Mathematical function combining multiplication and addition mod 26. |
| **Rail Fence Cipher**         | Transposition Cipher          | Integer (number of rails)          | Write letters in zigzag across rails, then read row by row. |
| **Columnar Transposition Cipher** | Transposition Cipher       | Word (e.g., "ZEBRA")               | Write letters in grid columns under a keyword; read columns in order of the keyword. |
| **Scytale Cipher** (Spartan)  | Transposition Cipher          | Integer (number of columns/cylinder circumference) | Write letters row by row, read vertically. |
| **ROT13**                     | Substitution Cipher           | None (fixed shift of 13)            | Caesar cipher with a shift of 13; encrypting twice returns the original. |
| **Playfair Cipher**           | Digraph Substitution Cipher   | Word/Phrase to build 5x5 grid       | Encrypt letter pairs based on their positions in a 5x5 matrix. |
| **Bacon's Cipher**            | Binary Encoding Cipher        | Optional (cover text if using steganography) | Encode letters into 5-character binary sequences (A=AAAAA, B=AAAAB, etc.). |
| **AES (Advanced Encryption Standard)** | Symmetric Cipher (Block Cipher) | Shared secret key (128/192/256 bits) | Block-based encryption with repeated substitution and permutation rounds. |
| **Diffie-Hellman Key Exchange** | Key Exchange Protocol (not encryption itself) | Private key, public prime (p) and generator (g) | Securely agree on a shared secret over an insecure channel using modular exponentiation. |
| **RSA (Rivest–Shamir–Adleman)** | Asymmetric Cipher (Public-Key Encryption) | Public key (n, e), Private key (d) | Modular exponentiation; based on difficulty of factoring large primes. |

---

# Quick Categories Breakdown

| Cipher Category | Examples |
|-----------------|----------|
| **Substitution** | Caesar, Vigenère, Atbash, Monoalphabetic, Affine, ROT13 |
| **Transposition** | Rail Fence, Columnar Transposition, Scytale |
| **Binary/Encoding** | Bacon’s Cipher |
| **Block Cipher (Symmetric)** | AES |
| **Key Exchange (Protocol)** | Diffie-Hellman |
| **Public Key (Asymmetric)** | RSA |

---

# Quick Way to Think About Them

| Symmetric | Asymmetric | Key Exchange |
|:----------|:-----------|:-------------|
| AES | RSA | Diffie-Hellman |

- **Symmetric**: Same key for encrypt and decrypt.
- **Asymmetric**: Public/private key pair.
- **Key Exchange**: Securely share secret keys for symmetric use.

