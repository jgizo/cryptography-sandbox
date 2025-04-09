import math

def is_prime(n: int) -> bool:
    lim = math.floor(math.sqrt(n))

    if n == 1:
        return False
    
    if n > 3:
        for i in range(2, lim+1):
            if n % i == 0:
                return False
    
    return True
    

def generate_prime(bits: int) -> int:
    # TODO: Generate a prime number of the specified bit length
    pass
