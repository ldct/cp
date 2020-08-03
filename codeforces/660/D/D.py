#!/usr/bin/env pypy3
	
from collections import defaultdict, deque

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

input()
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

N = len(A)

next = dict()
prevs = defaultdict(set)

for i, b in enumerate(B):
	next[i+1] = b
	prevs[b].add(i+1)

queue = deque([])

for i in range(1, N+1):
	if len(prevs[i]) == 0:
		queue.append(i)

score = 0
positives = []
negatives = []

while len(queue):
	p = queue.popleft()
	q = next[p]

	prevs[q].remove(p)

	if q != -1 and len(prevs[q]) == 0:
		queue.append(q)

	a = A[p-1]
	b = B[p-1]

	if a >= 0:
		score += a
		if b != -1: A[b-1] += a
		positives += [p]
	else:
		negatives += [p]

for p in negatives:
	a = A[p-1]
	assert(a < 0)
	score += a

order = positives + negatives[::-1]

print(score)
print(*order)