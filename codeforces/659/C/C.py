#!/usr/bin/env pypy3

def ans(A, B):
	s = set()
	for a, b in zip(A, B):
		if a == b: continue
		if a > b: return -1
		s.add((ord(a)-97, ord(b)-97))
	s = sorted(list(s))

	ret = 0

	while len(s):
		ret += 1
		(a0, b0) = s[0]
		next_s = []
		for a, b in s:
			if a0 == a:
				assert b0 <= b
				a = b0
			next_s += [(a, b)]
		s = next_s
		next_s = []
		for a, b in s:
			if a == b: continue
			next_s += [(a, b)]
		s = sorted(list(set(next_s)))

	return ret
				

	return s

T = int(input())

for _ in range(T):
	input()
	A = input()
	B = input()
	print(ans(A, B))
