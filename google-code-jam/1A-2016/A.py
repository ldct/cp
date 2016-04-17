#!/usr/bin/env python3

T = int(input())

def ans(S):
	ret = S[0]
	for s in S[1:]:
		if s >= ret[0]:
			ret = s + ret
		else:
			ret = ret + s
	return ret

for t in range(T):
	S = input()
	print("Case #{0}: {1}".format(t+1, ans(S)))