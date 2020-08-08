#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

from collections import defaultdict, Counter

N = int(input())
A = list(map(int, input().split()))

smallish = defaultdict(set)
large = Counter()

def add(a):
	for i in range(1, 7):
		if a in smallish[i]:
			smallish[i].remove(a)
			smallish[i+1].add(a)
			return
	
	if a in smallish[7]:
		smallish[7].remove(a)
		large[a] = 8
		return

	if a in large:
		large[a] += 1
		return

	smallish[1].add(a)

def remove(a):
	for i in range(2, 8):
		if a in smallish[i]:
			smallish[i].remove(a)
			smallish[i-1].add(a)
			return

	if a in smallish[1]:
		smallish[1].remove(a)
		return

	if a in large:
		large[a] -= 1
		if large[a] == 7:
			del large[a]
			smallish[7].add(a)
		return

	assert(False)


for a in A:
	add(a)

def ans():
	if len(large):
		return "YES"
	if len(smallish[6]) + len(smallish[7]) >= 2:
		return "YES"
	if len(smallish[6]) + len(smallish[7]) >= 1:
		if sum(len(smallish[i]) for i in range(2, 6)) >= 1:
			return "YES"
		return "NO"
	if len(smallish[4]) + len(smallish[5]) >= 2:
		return "YES"
	if len(smallish[4]) + len(smallish[5]) >= 1:
		if sum(len(smallish[i]) for i in range(2, 4)) >= 2:
			return "YES"
		return "NO"

	return "NO"


for _ in range(int(input())):
	op, e = input().split()
	e = int(e)
	if op == '+':
		add(e)
	elif op == '-':
		remove(e)
	else:
		assert(False)

	print(ans())