
def one_divide(n):
    numerator = 1
    ret = []
    remainders = []
    while len(ret) < 1000 and numerator:
        while numerator < n:
            numerator *= 10
        multiple = numerator / n
        numerator = numerator % n
        if numerator in remainders:
            return ret[remainders.index(numerator):]
        remainders.append(numerator)
        ret.append(multiple)
    return []

def prob26():
    max_len = 6
    max_num = 7
    for i in xrange(11, 1000):
        repeats = one_divide(i)
        if len(repeats) > max_len:
            max_num = i
            max_len = len(repeats)
            print i, repeats, len(repeats)
    return max_num

print prob26()

