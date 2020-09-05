#!/usr/bin/env pypy3

def ans(S, T, K):

	for _ in range(K):
		for i in range(len(S)):
			
			# cover gaps

			if T[0] == T[1] and 1 <= i <= len(S)-1 and T[0] == S[i-1] and T[0] == S[i+1] and T[0] != S[i]:
				S[i] = T[0]
				break

			# greedily do one-sided


	S = list(S)
	return S,T,K

_, K = input().split()
S = input()
T = input()

print(ans(S, T, K))
