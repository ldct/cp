#!/usr/bin/env python3
import sys

input()
arr = list(input().split())

def isBeautiful(s):
	if s[0] != '1': return False
	for c in s[1:]:
		if c != '0': return False
	return True

logAns = 0
nonBeautiful = None
isZero = False

for s in arr:
	if s == "0":
		isZero = True
	if isBeautiful(s):
		logAns += (len(s) - 1)
	else:
		nonBeautiful = s

if isZero:
	print(0)
else:
	if nonBeautiful is None:
		nonBeautiful = '1'

	print(nonBeautiful + '0'*logAns)
