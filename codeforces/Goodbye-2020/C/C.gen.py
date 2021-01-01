#!/usr/bin/env pypy3

import itertools

testcases = []
for N in range(8, 9):
	for s in itertools.product("abc", repeat=N):
		testcases += [''.join(s)]

print(len(testcases))
for t in testcases:
	print(t)
