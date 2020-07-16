#!/usr/bin/env pypy3

from itertools import chain, combinations

def subsets(iterable, low=0, high=None):
    "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if high is None:
        high = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(low, high+1))

def overflow(A, BB, K):
	if sum(A) > sum(BB): return float("inf")
	old_BB = BB[:]
	BB = list(BB)
	for _ in range(len(A)):
		k = K
		BB = sorted(BB)[::-1]
		for i in range(len(BB)):
			if k > 0 and BB[i] > 0:
				BB[i] -= 1
				k -= 1
		if k > 0: return float("inf")
	return sum(old_BB) - sum(A)

def ss(target, B):
	import array
	possible = array.array('b', [1] + [0]*target)

	for b in B:
		next_possible = array.array('b', possible)
		for i in range(target):
			if possible[i] == 1 and i + b <= target:
				next_possible[i+b] = 1
		possible = next_possible

	for ret in range(target,-1,-1):
		if possible[ret]:
			return ret


def ans(A, B, K):
	if K == 1:
		if sum(B) < sum(A): return "Impossible"
		# print("ss", sum(B) - sum(A), ss(sum(B) - sum(A), B))
		return sum(B) - sum(A) - ss(sum(B) - sum(A), B)

	for a in A:
		if a < K:
			return "Impossible"
	ret = float("inf")
	for BB in subsets(B):
		ret = min(ret, overflow(A, BB, K))
	if ret == float("inf"):
		return "Impossible"
	return ret

N, M, K = input().split(' ')
N = int(N)
M = int(M)
K = int(K)

A = input().split(' ')
A = list(map(int, A))

B = input().split(' ')
B = list(map(int, B))

# print(overflow(A,B,K))
print(ans(A, B, K))