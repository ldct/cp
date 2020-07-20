#!/usr/bin/env pypy3

def count(S, t):
	ret = 0
	for i in range(len(S)):
		if S[i:i+len(t)] == t:
			ret += 1
	return ret

def match(aa, bb):
	if len(aa) != len(bb): return False
	for a, b in zip(aa, bb):
		if a == '?' or b == '?': continue
		if a != b: return False
	return True

def ok(S, i):
	t = "abacaba"
	if not match(S[i:i+len(t)], t): return False
	S = list(S)
	S[i:i+len(t)] = list(t)
	S = ''.join(S)
	if count(S, t) == 1:
		return S
	return False

def ans(S):
	c = count(S, "abacaba") 
	if c == 1:
		print("Yes")
		print(S.replace('?', 'z'))
		return
	elif c > 1:
		print("No")
		return
	else:
		for i in range(len(S)):
			r = ok(S, i)
			if r:
				print("Yes")
				print(r.replace('?', 'z'))
				return
		print("No")

T = int(input())
for t in range(T):
	input()
	S = input()
	ans(S)