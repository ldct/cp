#!/usr/bin/env pypy3

def ans(S):
	if len(S) % 2 == 1: return 'NO'
	i = S.index('(')
	j = S.index(')')
	if i < j:
		if S.count('?') % 2 == 1: return 'NO'
		return 'YES'

	if j == 0: return 'NO'
	if i == len(S)-1: return 'NO'
	return 'YES'


def possibilities(S):
	if len(S) == 0:
		return set([S])
	if S[0] == '?':
		ret = set()
		for p in possibilities(S[1:]):
			ret.add('(' + p)
			ret.add(')' + p)

		return ret

	ret = set()
	for p in possibilities(S[1:]):
		ret.add(S[0] + p)

	return ret

def is_rbs(S):
	rs = 0
	for c in S:
		if c == '(': rs += 1
		elif c == ')': rs -= 1
		else: assert(False)
		if rs < 0: return False
	return rs == 0


def ans_slow(S):
	for p in possibilities(S):
		if is_rbs(p):
			return 'YES'
	return 'NO'

# import random
# for _ in range(50000):
# 	testcase = ''.join(random.choice("()?") for _ in range(random.randint(2, 10)))
# 	if not (testcase.count('(') == 1 and testcase.count(')') == 1): continue
# 	if ans(testcase) != ans_slow(testcase):
# 		print(testcase, ans(testcase), ans_slow(testcase))

for _ in range(int(input())):
	S = input()
	print(ans(S))