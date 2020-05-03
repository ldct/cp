#!/usr/bin/env python3

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

possibilities = dict()
for a in ALPHABET:
	for i in range(10):
		possibilities[(a,i)] = 0

letters_seen = set()
letters_seen_in_first = set()

def bind(alpha, num, possibilities, letters_seen):
	for i in range(10):
		if i == num: continue
		if (alpha, i) in possibilities:
			del possibilities[(alpha, i)]
	for a in letters_seen:
		if a == alpha: continue
		if (a, num) in possibilities:
			del possibilities[(a,num)]

T = int(input())
for t in range(T):
	U = int(input())

	info = []
	for k in range(10**4):
		m, r = input().split(' ')
		info += [(m,r)]
	
	for m,r in info:
		for a in r:
			letters_seen.add(a)

	for a in ALPHABET:
		for i in range(10):
			if a not in letters_seen:
				if (a,i) in possibilities:
					del possibilities[(a,i)]

	for m,r in info:
		if len(m) != len(r): continue
		left_digit = int(m[0])
		left_alpha = r[0]
		for d in range(left_digit+1, 10):
			if (left_alpha, d) in possibilities:
				del possibilities[(left_alpha, d)]

	for m,r in info:
		if len(m) == len(r): continue
		letters_seen_in_first.add(r[0])


	(zero,) = letters_seen - letters_seen_in_first

	answer = dict()
	for i in range(10):
		answer[i] = set()

	for (a,i) in possibilities:
		answer[i].add(a)

	answer[0] = set([zero])

	for k in range(100):
		for i in range(10):
			if len(answer[i]) == 1:
				(a,) = answer[i]
				for j in range(10):
					if i == j: continue
					if a in answer[j]:
						answer[j].remove(a)


	ans = ""
	for i in range(10):
		(a,) = answer[i]
		ans += a

	print("Case #" + str(t+1) + ": " + ans)
