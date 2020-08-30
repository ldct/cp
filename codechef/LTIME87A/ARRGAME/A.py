#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def ans(A):
	A += [1]
	runs = []
	last_run = 0
	for a in A:
		if a == 1:
			if last_run > 0:
				runs += [last_run]
			last_run = 0
		else:
			assert(a == 0)
			last_run += 1

	if len(runs) == 0:
		return 'No'

	if len(runs) == 1:
		[run] = runs
		if run % 2 == 0:
			return 'No'
		return 'Yes'

	odd_runs = []
	even_runs = []

	for run in runs:
		if run % 2 == 0:
			even_runs += [run]
		else:
			odd_runs += [run]

	if len(odd_runs) == 0:
		return 'No'

	odd_runs = sorted(odd_runs)[::-1]

	# player 1 picks the longest odd

	p1_life = (odd_runs[0] + 1) // 2

	# player 2 

	runs = odd_runs[1:] + even_runs

	p2_life = max(runs)

	if p1_life > p2_life:
		return 'Yes'

	return 'No'

	return '?'

	return runs

T = int(input())
for t in range(T):
	input()
	A = list(map(int, input().split()))
	print(ans(A))