#!/usr/bin/env pypy3
	
from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

input()
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

N = len(A)

next = dict()
prev = dict()

for i, b in enumerate(B):
	next[i+1] = b
	prev[b] = i+1

lengths_of = dict()

def cl(i):
	ret = 0
	p = i
	while p != -1:
		ret += 1
		p = next[p]
	return ret

for i in range(1, N+1):
	if i not in prev:
		lengths_of[i] = cl(i)

head_of_longest = max(lengths_of, key=lengths_of.get)

# dump all positive numbers to head

score = 0

for i in len(N):
	
for i, a in enumerate(A):
	if a >= 0:


print(head_of_longest)