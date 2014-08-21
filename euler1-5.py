import itertools
import math

def prob5():
	nums = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
	for x in itertools.count(20, 10):
		if all([x % n == 0 for n in nums]):
			return x
			
print prob5()

def is_palindrome(x):
	str_x = str(x)
	for i in xrange(0, len(str_x)/2 + 1):
		if str_x[i] != str_x[-i -1]:
			return False
	return True

def prob4():
	max = 0
	for x in reversed(xrange(999)):
		for y in reversed(xrange(999)):
			if is_palindrome(x * y) and x * y > max:
				max = x * y
	return max
	
# print prob4()

def prob3():
	n = 600851475143
	i = 2
	while i * i < n:
		while n % i == 0:
			n = n / i
		i = i + 1
	return n
	
# print prob3()

def prob2():
	sum = 2
	i, j = 1, 2
	while True:
		next = i + j
		if next > 4000000:
			break;
		if next % 2 == 0:
			sum += next
		i = j
		j = next
	return sum
	
# print prob2()
def prob1():
    sum = 0
    for i in xrange(1000):
	    if i % 3 == 0 or i % 5 == 0:
	        sum += i
    return sum

# print prob1()

