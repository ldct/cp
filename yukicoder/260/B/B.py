#!/usr/bin/env pypy3

N=int(input())

s, t = input().split()
s = int(s)
t = int(t)
s -= 1
t -= 1

A = list(map(int, input().split()))
assert(len(A) == N)


q1 = []

i = (s+1) % N
while i != t:
	q1 += [A[i]]
	i += 1
	i %= N

q2 = []

i = (s-1) % N
while i != t:
	q2 += [A[i]]
	i -= 1
	i %= N

from functools import lru_cache

@lru_cache(None)
def ans(q1, q2):

	if len(q1) == 0 and len(q2) == 0: return 0
	if len(q1) % 2 == 0 and len(q2) % 2 == 0:
		m1 = len(q1) // 2
		m2 = len(q2) // 2
		return sum(q1[:m1]) - sum(q1[m1:]) + sum(q2[:m2]) - sum(q2[m2:])
	if len(q1) % 2 == 1 and len(q2) % 2 == 1:
		m1 = len(q1) // 2
		m2 = len(q2) // 2

		return max(
			sum(q1[:m1+1]) - sum(q1[m1+1:]) + sum(q2[:m2]) - sum(q2[m2:]),
			sum(q1[:m1]) - sum(q1[m1:]) + sum(q2[:m2+1]) - sum(q2[m2+1:])
		)

	if len(q1) == 0:
		qh, *qt = q2
		return qh - ans(q1[::-1], tuple(qt)[::-1])
	if len(q2) == 0:
		qh, *qt = q1
		return qh - ans(tuple(qt)[::-1], q2[::-1])
	

	q1h, *q1t = q1
	q2h, *q2t = q2

	return max(
		q2h - ans(q1[::-1], tuple(q2t)[::-1]),
		q1h - ans(tuple(q1t)[::-1], q2[::-1])
	)


# print(ans((100, 100, 100, 3, 2, 1), (1, 2, 100, 100)))
print(A[s] - A[t] + ans(tuple(q1), tuple(q2)))
