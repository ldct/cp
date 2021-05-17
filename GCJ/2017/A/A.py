#!/usr/bin/env python3

N = int(input())

def num_flips(S, K):
	SL = list(S)

	ans = 0

	for i in range(len(S)):
		if i + K > len(S):
			break

		if SL[i] == "-":
			ans += 1
			for j in range(i, i+K):
				if SL[j] == "-":
					SL[j] = "+"
				else:
					SL[j] = "-"

	if "-" in SL: return "IMPOSSIBLE"
	return ans

for i in range(N):
	S, K = input().split(' ')
	K = int(K)
	print("Case #" + str(i+1) + ": " + str(num_flips(S, K)))
