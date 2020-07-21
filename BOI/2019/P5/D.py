#!/usr/bin/env pypy3

from collections import Counter

def ok(a, b):
	if Counter(a) != Counter(b): return False
	for _ in range(len(a) + 2):
		if a == b or a[::-1] == b: return True
		a = a[1:] + a[0]
	return False

S1 = input()
S2 = input()

longest = float("-inf")
ans = None

for i in range(len(S1)):
	for j in range(i, min(i + 10000, len(S1))):
		for k in range(len(S2)):
			ss_length = j - i
			if ss_length <= longest: continue
			if not (k + ss_length <= len(S2)): continue
			if ok(S1[i:j], S2[k:k+ss_length]):
				longest = ss_length
				ans = (i, k)
print(longest)
print(*ans)