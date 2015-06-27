#!/usr/bin/env python3

N, K = tuple(map(int, input().split(' ')))

chains = []

for i in range(K):
	line = input().split(' ')[1:]
	chains += [list(map(int, line))]

num_small_chains = K

def len_prefix(l):
	if len(l) == 0:
		return 1
	for i in range(len(l)):
		if l[i] != i + 1:
			return i
	return len(l)

cost = 0
total_components = 0

for chain in chains:
	components = len(chain)
	if chain[0] == 1:
		components -= (len_prefix(chain) - 1)
	cuts = components - 1
	cost += cuts
	total_components += components 

cost += (total_components - 1)

print(cost)