import string
import utils

string_map = dict([(l, i+1) for i, l in enumerate(string.uppercase)])

def prob25():
    last_prev = (89, 2)
    prev = (144, 3)
    counter = 12
    while prev[1] < 1000:
        next = last_prev[0] + prev[0]
        if len(str(next)) > len(str(prev[0])):
            # next digit has been made
            last_prev = (int(str(prev[0])[:10]), prev[1])
            prev = (int(str(next)[:11]), prev[1] + 1)
        else:
            last_prev = prev
            prev = (next, prev[1])
        counter += 1
    return counter

print prob25()

def is_reversed(lst):
	for i in xrange(len(lst) - 1):
		if lst[i] < lst[i+1]:
			return False
	return True

def next_largest(src, nums):
	largest = None
	for x in nums:
		if x > src and (not largest or x < largest):
			largest = x
	return largest

def get_next(nums):
	if is_reversed(nums):
		return sorted(nums) # start over
	return next_perm1(nums)
	
def next_perm1(nums):
        if len(nums) == 1:
		return None
	if len(nums) == 2:
		if nums[0] < nums[1]:
			return [nums[1], nums[0]]
		return None # last element
	first = nums[0]
	rest = next_perm1(nums[1:])
	if rest:
		return [first] + rest
	# rest fully reversed
	next_num = next_largest(first, nums[1:])
	if not next_num: # everything fully reversed
		return None
	rest = set(nums[1:])
	rest.remove(next_num)
	rest.add(first)
	return [next_num] + sorted(list(rest))
	
def prob24():
	nums = range(10)
	print nums
	for i in xrange(1, 1000000):
		nums = get_next(nums)
	return nums
	
# print prob24()

def is_abundant(n):
	return n < sum(set(utils.find_factors(n)))

def prob23():
	start = 12
	end = 28123
	abundant_nums = [i for i in xrange(start, end-start+1) if is_abundant(i)]
	all_nums = set(range(28124))
	for i in abundant_nums:
		for j in abundant_nums:
			if i + j > end:
				break
			if (i + j) in all_nums:
				all_nums.remove(i+j)
	return sum(all_nums)
	
# print prob23()

def prob22():
	names = open('prob22names.txt', 'r').read().split(',')
	names = [n.replace('"', '') for n in names if n]
	names = sorted(names)
	ret = 0
	for i, name in enumerate(names):
		num_lst = [string_map[l] for l in name]
		name_sum = sum(num_lst)
		ret += (name_sum * (i + 1))
	return ret
	
# print prob22()

def prob21():
    amicable = set()
    for i in xrange(1, 10000):
        a = sum(utils.find_factors(i))
        b = sum(utils.find_factors(a))
        if b == i and a != 1 and a != i:
            amicable.add(i)
            amicable.add(a)
    return sum(amicable)

# print prob21()

