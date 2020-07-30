#!/usr/bin/env pypy3
	
from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def r_of(x):
	k = ["{0:b}".format(int(c)) for c in str(x)]
	k = ''.join(k)
	r = k[0:len(k)-len(str(x))]
	if len(r) == 0: return 0
	return int(r,2)


def ans_slow(n):
	n -= 1
	max_r = max(r_of(x) for x in range(10**n, 10**(n+1)-1))
	min_x = min(x for x in range(10**n, 10**(n+1)-1) if r_of(x) == max_r)
	return min_x

def ans(n):
	s = [1,0,0,1]*n
	for i in range(n):
		s[i] = 0
	s = s[::-1]
	s = list(chunks(s, 4))

	ret = []
	for c in s:
		if c[0] == 0:
			c = [1,0,0,0]
		ss = ''.join(map(str, c))
		ret += [int(ss, 2)]

	return ''.join(map(str, ret))

# for n in range(1, 10):
# 	print(n)
# 	assert(ans(n) == str(ans_slow(n)))


T = int(input())

for _ in range(T):
	n = int(input())
	print(ans(n))
