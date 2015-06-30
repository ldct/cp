#!/usr/bin/env python3

import math

N = int(input())
L = list(map(int, input().split(' ')))
D = list(map(int, input().split(' ')))

max_cost = 200

lc = list(zip(L, D))
lc.sort()
cost_l = [_lc[1] for _lc in lc]
length_l = [_lc[0] for _lc in lc]

cost_l_prefix = [0]
for i in range(N):
	cost_l_prefix += [cost_l_prefix[-1] + cost_l[i]]

def sum_cost_l(a, b):
	#[a, b)
	return cost_l_prefix[b] - cost_l_prefix[a]

# length_l_d[d] = lengths of legs of cost d, sorted by length
length_l_d = {}

len_lld = {}

for cc in range(1, max_cost + 1):
	length_l_d[cc] = [_lc[0] for _lc in lc if _lc[1] == cc]
	len_lld[cc] = len(length_l_d[cc])


def cost_rkp(k, p):
	# cheapest cost to remove k legs of length less than p
	cc = 1
	cost = 0
	while (k > 0):
		num_removable = min(num_kp(cc, p), k)
		k -= num_removable
		cost += num_removable * cc
		cc += 1
	return cost

def num_kp(c, p):
	# number of cost c legs of length strictly less than p
	ls = length_l_d[c] # all lengths
	i = 0
	j = len_lld[c] - 1

	if (j <= 1):
		return len([_ls for _ls in ls if _ls < p])

	if (ls[i] >= p):
		return 0

	if (ls[j] < p):
		return len_lld[c]

	while (j - i > 1):
		#ls[i] < p, ls[j] >= p
		mid = math.ceil((i + j) / 2)
		if ls[mid] < p:
			i = mid
		else:
			j = mid

	return j - i + 1


	# todo: binary search



s = set()

# go through length_l
i = 0

while (i < N):
	length = length_l[i]
	j = i
	while ((j + 1 < N) and length_l[j + 1] == length):
		j += 1


	ctc_l = sum_cost_l(j + 1, N)
	total_after_cutting = j + 1 #l
	total_maximal = j - i + 1

	ntc_s = total_after_cutting - 2 * total_maximal + 1
	ntc_s = max(0, ntc_s)

	ctc_s = cost_rkp(ntc_s, length)


	s.add(ctc_s + ctc_l)

	# print('considering length', length, 'from', i, j, ctc_l, ctc_s)
	i = j + 1

print(min(s))