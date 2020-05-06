#!/usr/bin/env python3

def mark(N, forwards, backwards, counts, idx):
	new_value = None
	if idx < N:
		new_value = forwards[idx]

	for b in backwards[idx-1]:
		old_value = forwards[b-1]
		forwards[b-1] = new_value

		counts[old_value-1] -= 1
		if new_value is not None:
			counts[new_value-1] += 1
			backwards[new_value-1].add(b)

	backwards[idx-1] = set()


def possible(permutation):
	N = len(permutation)
	forwards = []
	backwards = []
	counts = []
	for i in range(N):
		forwards += [i+1]
		backwards += [set([i+1])]
		counts += [1]

	pairs = list((e, i+1) for i, e in enumerate(permutation))
	indexes = sorted(pairs)
	indexes = list(y for x,y in indexes)

	# print(forwards, backwards, counts)
	for i in indexes:
		# generater chooses i
		presumed_maximum = counts[i-1]
		for c in counts:
			if c > presumed_maximum:
				return False
		mark(N, forwards, backwards, counts, i)	
		# print(forwards, backwards, counts)

	return True
	
T = int(input())
for t in range(T):
	input()
	permutation = input().split(' ')
	permutation = list(int(x) for x in permutation)
	if possible(permutation):
		print("Yes")
	else:
		print("No")