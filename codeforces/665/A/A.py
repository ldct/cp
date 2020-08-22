#!/usr/bin/env pypy3

def ans1(a, k):
	if (k + a) % 2 == 1: return 1
	return 0



def ans(a, k):
	if k > a: return k-a
	if k == a: return 0
	return ans1(a, k)


T = int(input())
for t in range(T):
	n, k = input().split()
	n = int(n)
	k = int(k)
	print(ans(n, k))
