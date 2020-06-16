#!/usr/bin/env python3
	
from collections import Counter

ALPHA = "abcdefghijklmnopqrstuvwxyz"
REV_ALPHA = "abcdefghijklmnopqrstuvwxyz"[::-1]

def ans(M, S):
	letters = [None]*len(M)
	counter = 0

	while sum([m for m in M if m is not None]) > 0:
		next_M = M[:]
		for _ in range(M.count(0)):
			i = M.index(0)
			letters[i] = REV_ALPHA[counter]
			
			for j in range(len(M)):
				if next_M[j] is not None and next_M[j] > 0:
					next_M[j] -= abs(i - j)

			M[i] = None
			next_M[i] = None

		counter += 1
		M = next_M

	for i in range(len(M)):
		if letters[i] is None:
			letters[i] = REV_ALPHA[counter]

	freqs = Counter(letters)

	target = []
	for a in ALPHA:
		if freqs[a] > 0:
			target += [freqs[a]]

	freqs = Counter(S)

	source = []
	sourcemap = []
	for a in ALPHA:
		if freqs[a] > 0:
			source += [freqs[a]]
			sourcemap += [a]

	indexes = []
	i = 0
	for j in target:
		while source[i] < j: i += 1
		indexes += [i]
		i += 1

	matchedsource = []
	for i in indexes:
		matchedsource += sourcemap[i]

	matchedletters = sorted(list(set(letters)))

	assert(len(matchedletters) == len(matchedsource))

	translate = dict()

	for l, s in zip(matchedletters, matchedsource):
		translate[l] = s

	return ''.join(translate[l] for l in letters)

T = int(input())
for t in range(T):
	S = input()
	input()
	M = input().split(' ')
	M = [int(x) for x in M]

	print(ans(M, S))