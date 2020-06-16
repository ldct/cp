#!/usr/bin/env python3

def ans(p):
	ret = []
	for i in range(len(p)):
		if i == 0: ret += [p[i]]
		elif i == len(p)-1: ret += [p[i]]
		elif p[i-1] <= p[i] <= p[i+1]: continue
		elif p[i-1] >= p[i] >= p[i+1]: continue
		else: ret += [p[i]]
	return ret

T = int(input())
for t in range(T):
	input()
	p = input().split(' ')
	p = [int(x) for x in p]
	a = ans(p)
	print(len(a))
	print(' '.join(str(x) for x in a))
