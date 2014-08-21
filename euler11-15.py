import itertools

def prob15():
	grid = [[0] * 21 for i in xrange(21)]
	grid[0][0] = 1
	for i in xrange(20):
		grid[i][0] = 1
		grid[0][i] = 1
	for i in xrange(21):
		for j in xrange(21):
			if not grid[i][j]:
				grid[i][j] += grid[i-1][j]
				grid[i][j] += grid[i][j-1]
	return grid[20][20]

# print prob15()

def prob14():
	count_dict = {}
	max_num = 1
	max_ct = 1
	for i in xrange(1, 1000000):
		ct = collatz_count(i, count_dict)
		count_dict[i] = ct
		if ct > max_ct:
			max_ct = ct
			max_num = i
	return max_num

def collatz_count(i, d):
	counter = 1
	while i != 1:
		if i in d:
			return d[i] + counter
		i = (i/2) if i % 2 == 0 else (3 * i + 1)
		counter += 1
	return counter	
	
# print prob14()

def prob13():
	num_txt = open('prob13nums.txt', 'r').read()
	nums = [int(i) for i in num_txt.split()]
	ret_num = sum(nums)
	return str(ret_num)[:10]
	
# print prob13()

def prob12():
	sum = 0
	count = 1
	while True:
		divisor_count = find_divisors(sum)
		if divisor_count > 500:
			return sum
		sum += count
		count += 1
	
def find_divisors(i):
	divisors = 2
	cur_divisor = 2
	max_i = i
	while cur_divisor < max_i:
		if i % cur_divisor == 0:
			divisors += 2
			max_i = i / cur_divisor
		cur_divisor += 1
	return divisors

# print prob12()

def prob11():
	grid = read_grid()
	max_prod = 1
	# find max in horizontal
	for i in xrange(20):
		for j in xrange(20-3):
			prod = grid[i][j]
			for k in xrange(1, 4):
				prod *= grid[i][j+k]
			if prod > max_prod:
				max_prod = prod
	# find max in vertical
	for i in xrange(20-3):
		for j in xrange(20):
			prod = grid[i][j]
			for k in xrange(1, 4):
				prod *= grid[i+k][j]
			if prod > max_prod:
				max_prod = prod
	# find max in diagonal to right
	for i in xrange(20-3):
		for j in xrange(20-3):
			prod = grid[i][j]
			for k in xrange(1, 4):
				prod *= grid[i+k][j+k]
			if prod > max_prod:
				max_prod = prod
	# find max in diagonal to the left
	for i in xrange(20-3):
		for j in xrange(3, 20):
			prod = grid[i][j]
			for k in xrange(1, 4):
				prod *= grid[i+k][j-k]
			if prod > max_prod:
				max_prod = prod
	return max_prod
	
def read_grid():
	grid_txt = open('prob11nums.txt', 'r').read()
	grid_nums = grid_txt.split('\n')
	grid_nums = [g.split(' ') for g in grid_nums]
	for i in xrange(len(grid_nums)):
		for j in xrange(len(grid_nums[i])):
			grid_nums[i][j] = int(grid_nums[i][j])
	return grid_nums

#print prob11()