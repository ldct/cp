#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def s_of(w):
	ret = []

	for i in range(len(w)):
		anchors = []
		for j in [i-x, i+x]:
			if 0 <= j < len(w):
				anchors += [w[j]]
		if 1 in anchors:
			ret += [1]
		else:
			ret += [0]

	return ret

def ans(S, x):
	ret = [1] * len(S)

	for i, s in enumerate(S):
		if s == '0':

			for j in [i-x, i+x]:
				if 0 <= j < len(ret): ret[j] = 0
	
	if ''.join(map(str, s_of(ret))) == S:
		return ''.join(map(str, ret))
	else:
		return '-1'

T = int(input())
for t in range(T):
	S = input()
	x = int(input())

	print(ans(S, x))