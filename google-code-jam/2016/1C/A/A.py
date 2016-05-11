#!/usr/bin/env python

T = int(raw_input())

def argmax(arr):
	ret = 0
	for i, e in enumerate(arr):
		if e > arr[ret]:  ret = i
	return ret

def ans(S):
	members = [int(x) for x in S.split(' ')]
	leave = []
	total_members = sum(members)
	tm = total_members

	while total_members > 0:
		am = argmax(members)
		leave += ['ABCDEFGHIJKLMNOPQRSTUVWXYZ'[am]]
		members[am] -= 1
		total_members -= 1

	ret = []

	if tm % 2 == 0:
		for i in range(0, tm, 2):
			ret += [leave[i] + leave[i+1]]
	else:
		for i in range(0, tm-3, 2):
			ret += [leave[i] + leave[i+1]]
		ret += [leave[-3]]
		ret += [leave[-2] + leave[-1]]
	return ' '.join(ret)

for t in range(T):
	raw_input()
	S = raw_input()
	print("Case #{0}: {1}".format(t+1, ans(S)))