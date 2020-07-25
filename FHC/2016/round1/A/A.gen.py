#!/usr/bin/python3

from random import randint

N=402

def increasingRandom():
	i = 0;
	while True:
		yield i;
		i += randint(1, 10)

def r(max):
	for (i, x) in enumerate(steady()):
		if (i == max): break
		yield (x % 100) + 1

def steady():
	while True:
		yield 0
		yield 1
		yield 2
		yield 3

print(1)
print(N)
print(' '.join(str(x) for x in r(N)))