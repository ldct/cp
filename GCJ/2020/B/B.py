#!/usr/bin/env python3

T = int(input())

def is_done(l):
	for x in l:
		if x > 0: return False
	return True

def combine(l, b):
	ret = ''
	ret += b[0]
	for i in range(len(l)):
		ret += str(l[i])
		ret += b[i+1]
	return ret

def first_nonzero(l):
	ret = 0
	while l[ret] == 0:
		ret += 1
	return ret

def first_zero(l, s):
	N = len(l)
	ret = s
	while ret < N and l[ret] > 0:
		ret += 1
	return ret
	
def ans(l):	
	old_l = l[:]

	brackets = []
	for i in range(len(l)+1):
		brackets.append('')

	while True:
		if is_done(l):
			return combine(old_l, brackets)

		s = first_nonzero(l)
		e = first_zero(l, s)
		brackets[s] = brackets[s] + '('
		brackets[e] = ')' + brackets[e]

		for i in range(s, e):
			l[i] -= 1

for i in range(T):
	l = list(input())
	l = [int(x) for x in l]
	print("Case #" + str(i+1) + ": " + ans(l))
