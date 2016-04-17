#!/usr/bin/env python3

T = int(input())

def ans(numKids, kids):

	bffOf = [int(k) for k in kids.split(' ')]

	reprOf = {}

	for k in range(1, numKids+1):

		currentStudent = k
		while True:

			if k in reprOf.keys(): break

			reprOf[currentStudent] = k
			currentStudent = bffOf[currentStudent-1]


	return reprOf

for t in range(T):
	numKids = int(input())
	kids = input()
	print("Case #{0}: {1}".format(t+1, ans(numKids, kids)))