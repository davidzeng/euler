def prob21():
    amicable = set()
    for i in xrange(1, 10000):
        a = sum(find_factors(i))
        b = sum(find_factors(a))
        if b == i and a != 1 and a != i:
            amicable.add(i)
            amicable.add(a)
    print amicable
    return sum(amicable)

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

print prob21()

