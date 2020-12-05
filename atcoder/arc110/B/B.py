#!/usr/bin/env pypy3

NUM_COPIES = 10**10

def starta(S):
	ret = 0
	i = 0
	while S[i:i+3] == "110":
		ret += 1
		i += 3
	return (ret, S[i:])

def ans1(S):
	reps, rest = starta(S)
	if len(rest) == 0:
		return NUM_COPIES - reps + 1
	elif "110".startswith(rest):
		return NUM_COPIES - reps
	else:
		return 0

def ans(S):
	if S == "1": return NUM_COPIES*2
	if S == "0": return NUM_COPIES
	return max(ans1(S), ans1("1" + S), ans1("11" + S))

input()
print(ans(input()))