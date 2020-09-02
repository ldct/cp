#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

import functools

@functools.lru_cache(None)
def p1_wins(A, banned):
	if len(A) == 0:
		return False
	
	for i in range(len(A)):
		next_A = A[0:i] + A[i+1:]
		if banned is not None:
			next_A += (banned,)
		next_banned = A[i]-1
		if next_banned == 0:
			next_banned = None

		if not p1_wins(tuple(sorted(next_A)), next_banned):
			return True
	
	return False

def ans_slow(A):
	if p1_wins(tuple(A), None):
		return 'T'
	return 'HL'

def ans(A):

	P1_turn = True
	last_chosen = None

	while sum(A) > 0:
		# print(A)
		eligible = []
		for i, e in enumerate(A):
			if i != last_chosen and e > 0:
				eligible += [(e, i)]
		
		if len(eligible) == 0:
			# print("P1" if P1_turn else "P2", "nothing to choose")
			if P1_turn:
				return 'HL'
			else:
				return 'T'

		_, last_chosen = max(eligible)
		# print("P1" if P1_turn else "P2", "choose", last_chosen)

		A[last_chosen] -= 1

		P1_turn = not P1_turn

	# print("all chosen")
	if P1_turn:
		return 'HL'
	else:
		return 'T'


# import random
# for _ in range(100):
# 	a = random.randint(1,100)
# 	b = random.randint(1,20)
# 	c = random.randint(1,20)
# 	d = random.randint(1,20)

# 	if ans([a,b,c,d]) != ans_slow([a,b,c,d]):
# 		print(a,b,c,d)

for _ in range(int(input())):
	input()
	A = list(map(int, input().split()))
	print(ans(A))
	print(ans_slow(A))