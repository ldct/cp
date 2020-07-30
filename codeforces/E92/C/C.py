#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

T = int(input())

def ans1(S):
	return max(S.count(i) for i in "0123456789")

def ans2(S):
	ret = float("-inf")
	for i in "0123456789":
		for j in "0123456789":
			ret = max(ret, ans3(S, i, j))
	return ret

def ans3(S, a, b):
	# longest substring match of (ab)* in S

	na = 0
	nb = 0

	for c in S:
		if na == nb and c == a:
			na += 1
		elif na == nb + 1 and c == b:
			nb += 1

	return 2*nb


def ans(S):
	return len(S) - max(ans1(S), ans2(S))

for _ in range(T):
	S = input()
	print(ans(S))