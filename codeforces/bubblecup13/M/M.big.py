#!/usr/bin/env pypy3

N = 1
K = 10**5

alphabet = "abcdefghijklmnopqrstuvwxyz"

import random

def random_word():
	return ''.join(random.choice(alphabet) for _ in range(99))

words = [random_word() for _ in range(K)]
words = sorted(words)


print(N, K)
print(0)
for w in words:
	print(w)
