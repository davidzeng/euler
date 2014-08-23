import math

def prob20():
    return sum([int(l) for l in str(math.factorial(100))])

print prob20()

def count_month(start_day, month_num, year):
    days = 31
    if month_num in (4, 6, 9, 11):
        days = 30
    elif month_num == 2:
        days = 29 if leap_year(year) else 28
    ct = 1 if start_day == 0 else 0
    start_day = (start_day + days) % 7
    return ct, start_day

def count_year(start_day, year):
    ct = 0
    start = start_day
    for i in xrange(1, 13):
        month_ct, next_start = count_month(start, i, year)
        ct += month_ct
        start = next_start
    return ct, start

def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

def prob19():
    ct = 0
    start = 0
    for i in xrange(1901, 2001):
        yr_ct, next_start = count_year(start, i)
        ct += yr_ct
        start = next_start
    return ct

#print prob19()

def prob18():
    nums = parse_nums()
    nums.reverse()
    ret_arr = [[0] * len(nums) for _ in xrange(len(nums))]
    ret_arr[0] = nums[0]
    for i in xrange(1, len(nums)):
        counter = len(nums) - i
        for j in xrange(counter):
            ret_arr[i][j] = nums[i][j] + max(ret_arr[i-1][j], ret_arr[i-1][j+1])
    print ret_arr
    return ret_arr[14][0]

def parse_nums():
    num_arr = open('prob18nums.txt', 'r').read().split('\n')[:-1]
    ret_arr = [map(int, i.split(' ')) for i in num_arr]
    return ret_arr

# print prob18()

def prob17():
    ltr_ct = 0
    for i in xrange(1, 1000):
        ltr_ct += parse_wrd(i)
    ltr_ct += len('onethousand')
    return ltr_ct

ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def parse_wrd(i):
    ct = 0
    if i / 100  != 0:
        ct += len(ones[i/100]) + len('hundred')
        if i % 100 != 0:
            ct += len('and')
    i = i % 100  # grab remainder
    if i >= 11 and i < 20:
        ct += len(teens[i % 10])
    else:
        # not in the teens
        ct += len(tens[i / 10])
        ct += len(ones[i % 10])
    return ct

# print prob17()

def prob16():
    return sum([int(l) for l in str(2**1000)])

# print prob16()
