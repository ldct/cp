#!/usr/bin/env python3

from math import sqrt; from itertools import count, islice
import random

def isPrime(n):
	return fermatIsPrime(n)

def isJamcoin(s):
	assert(s[0] == '1')
	assert(s[-1] == '1')

	for b in range(2, 11):
		n = int(s, b)
		if isPrime(n): return False
	return True

def randomCoin(l):
	return '1' + ''.join(random.choice('01') for _ in range(l-2)) + '1'

def divisorOf(n):
	for i in range(2, 1000):
		if n % i == 0:
			return i
	raise Exception

def fermatIsPrime(n):
	if n == 2:
		return True
	if not n & 1:
		return False
	return pow(2, n-1, n) == 1

coins = set()

# to generate ./largecoins, uncomment these out

# while len(coins) < 50:
# 	c = randomCoin(32)
# 	if isJamcoin(c):
# 		print(c)


print("Case #1: ")
numcoins = 0
with open('./largecoins') as f:
	for l in f.readlines():
		coin = l[:-1]
		try:
			print(coin, ' '.join(str(divisorOf(int(coin, b))) for b in range(2, 11)))
			numcoins += 1
		except Exception:
			pass

		if (numcoins == 500): break
