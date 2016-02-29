#!/usr/bin/env python3

def lastTwo(n):
	# 5 ** n % 100
	if n == 0: return 1
	if n == 1: return 5
	return 25

n = str(input())
print(lastTwo(n))
