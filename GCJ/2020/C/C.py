#!/usr/bin/env python3

T = int(input())

def ans(sched, N):
	ppl = []
	for i in range(N):
		ppl.append('?')

	is_free_at = {}
	is_free_at['J'] = -1
	is_free_at['C'] = -1

	for s, e, j in sched:		

		# print("is_free_at=", is_free_at)
		if is_free_at['C'] < s:
			# print("assigning", j, "to C with end", e)
			ppl[j] = 'C'
			is_free_at['C'] = e
		elif is_free_at['J'] < s:
			# print("assigning", j, "to J with end", e)
			ppl[j] = 'J'
			is_free_at['J'] = e

		else:
			return "IMPOSSIBLE"

	return ''.join(ppl)

for i in range(T):
	N = int(input())
	sched = []
	for j in range(N):
		s, e = input().split(' ')
		s = int(s)
		e = int(e)
		sched += [(s + 0.1, e, j)]

	sched = sorted(sched)
	
	print("Case #" + str(i+1) + ": " + ans(sched, N))
