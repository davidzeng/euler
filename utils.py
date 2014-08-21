def is_prime(x, primes):
    for p in primes:
        if x % p == 0:
            return False
        if p * p > x:
            return True
    return True