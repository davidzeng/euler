def is_prime(x, primes):
    for p in primes:
        if x % p == 0:
            return False
        if p * p > x:
            return True
    return True
	
def find_factors(n):
    max_num = n
    divisor = 2
    factors = [1]
    while divisor < max_num:
        if n % divisor == 0:
            factors.append(divisor)
            factors.append(n/divisor)
            max_num = n / divisor
        divisor += 1
    return factors