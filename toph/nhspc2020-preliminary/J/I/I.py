#!/usr/bin/env pypy3

from collections import deque

input()
S = input()

C = deque([])
O = deque([])
D = deque([])
E = deque([])

for i, c in enumerate(S):
	if c == "c": C.append(i)
	if c == "o": O.append(i)
	if c == "d": D.append(i)
	if c == "e": E.append(i)

ret = 0
while len(C) and len(O) and len(D) and len(E):
	if C[0] < O[0] < D[0] < E[0]:
		ret += 1
		C.popleft()
		O.popleft()
		D.popleft()
		E.popleft()
	elif C[0] > O[0]:
		O.popleft()
	elif O[0] > D[0]:
		D.popleft()
	elif D[0] > E[0]:
		E.popleft()
	else:
		break

print(ret)
