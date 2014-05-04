#!/usr/bin/env python



def bit_size(n):
	if n == 0:
		return 0
	else:
		return len("{0:b}".format(n))

def kill_left(n):
	if n == 1 or n == 0:
		return 0
	else:
		return n & 1 << (bit_size(n) - 2)

def shift(n):
	try:
		return 1 << (bit_size(n) - 2)
	except:
		return 0

memo = {}
def f(a, b, k): #less than or equal to
	s_a = bit_size(a)
	s_b = bit_size(b)
	s_k = bit_size(k)

	if (a == b and b == k and k == 0):
		return 1

	if s_k > max(s_a, s_b):
		return (a+1)*(b+1)

	if s_k == max(s_a, s_b):
		if (s_a > s_b):
			return 2 * f(shift(a), b, k)
		if (s_b > s_a):
			return 2 * f(a, shift(b), k)
		else:
			return 3 * f(shift(a), shift(b), k) + f(kill_left(a), kill_left(b), kill_left(k))

	else: #s_k < s_ab
		if (s_a > s_b):
			return 2 * f(shift(a), b, k)
		if (s_a < s_b):
			return 2 * f(a, shift(b), k)
		else:
			print shift(a), shift(b), k
			return f(shift(a), b, k) + f(shift(a), shift(b), k)


T = int(raw_input(''))
for t in range(T):
	(A, B, K) = tuple(raw_input('').split(" "))
	print f(int(A) - 1, int(B) - 1, int(K) - 1)

print f(2, 3, 1)