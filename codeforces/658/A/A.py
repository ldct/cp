#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def ans(A, B):
	intersect = set(A) & set(B)

	if len(intersect) == 0:
		print("NO")
		return

	i = list(intersect)[0]

	print("YES")
	print(1, i)

T = int(input())

for _ in range(T):
	input()
	A = input().split(' ')
	A = list(map(int, A))
	B = input().split(' ')
	B = list(map(int, B))
	ans(A, B)