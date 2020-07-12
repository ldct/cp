#!/usr/bin/env python3
	
def ans_slow(p):
	for i in range(len(p)):
		for j in range(i+1, len(p)):
			for k in range(j+1, len(p)):
				if p[j] > p[i] and p[j] > p[k]: return (i+1, j+1, k+1)
	return None

def ans(p):
	for i in range(len(p)-2):
		j = i+1
		k = j+1

		if p[j] > p[i] and p[j] > p[k]: return (i+1, j+1, k+1)

	return None

T = int(input())
for t in range(T):
	input()
	p = input().split(' ')
	p = list(map(int, p))
	r = ans(p)
	if r is None:
		print("NO")
	else:
		print("YES")
		print(*r)
