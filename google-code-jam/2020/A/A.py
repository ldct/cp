#!/usr/bin/env python3

T = int(input())

def trace(mat):
	ret = 0
	for i in range(len(mat)):
		ret += mat[i][i]
	return ret

def has_duplicates(arr):
	return len(arr) > len(set(arr))

def num_duplicate_rows(mat):
	return len([row for row in mat if has_duplicates(row)])

mats = []

for i in range(T):
	N = int(input())
	mat = []
	for i in range(N):
		row = input().split(' ')
		row = [int(x) for x in row]
		mat.append(row)
	mats.append(mat)

for i in range(T):
	m = mats[i]
	print(''.join([
		"Case #",
		str(i+1),
		": ",
		str(trace(m)),
		" ",
		str(num_duplicate_rows(m)),
		" ",
		str(num_duplicate_rows(zip(*m)))
	]))
