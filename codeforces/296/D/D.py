n = int(raw_input())

intervals = []
rev_intervals = []

idx_left = {}

for i in range(n):
	c, w = raw_input().split(' ')
	c, w = int(c), int(w)
	a = c - w
	b = c + w
	intervals += [(int(a), int(b))]
	rev_intervals += [(int(b), int(a))]

left_endpoints = []
right_endpoints = []

for (a, b) in sorted(intervals):
	left_endpoints += [a]

for (b, a) in sorted(rev_intervals):
	right_endpoints += [b]

# print(left_endpoints)
# print(right_endpoints)

def ss(arr, key):
	if len(arr) == 0:
		return 0
	if arr[0] > key:
		return 0
	else:
		return 1 + ss(arr[1:], key)

def bs_left(key, lo, hi):
	if hi - lo < 2:
		return ss(left_endpoints, key)
	if lo + 1 >= hi:
		return lo
	mid = int((lo + hi) / 2)
	if left_endpoints[mid] < key:
		return bs_left(key, mid, hi)
	else:
		return bs_left(key, lo, mid)

def bs_right(key, lo, hi):
	if hi - lo < 2:
		return ss(right_endpoints, key)
	if lo + 1 >= hi:
		return lo
	mid = int((lo + hi) / 2)
	if right_endpoints[mid] < key:
		return bs_right(key, mid, hi)
	else:
		return bs_right(key, lo, mid)

def num_intervals(x):
	num_left_left_inclusive = bs_left(x + 0.1, 0, len(left_endpoints) - 1)
	num_left_right_exclusive = bs_right(x - 0.1, 0, len(right_endpoints) - 1)

	ans = num_left_left_inclusive - num_left_right_exclusive
	print(x, ans)
	return ans

if len(left_endpoints):
	print max(num_intervals(l) for l in left_endpoints)
else:
	print 0