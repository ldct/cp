#!/usr/bin/env pypy3

def ans(A):

	A = sorted(A)[::-1]

	adv = 0
	alice_turn = True

	for a in A:
		if alice_turn:
			if a % 2 == 0:
				adv += a
		else:
			if a % 2 == 1:
				adv -= a

		alice_turn = not alice_turn

	if adv == 0: return "Tie"
	if adv > 0: return "Alice"
	return "Bob"

for _ in range(int(input())):
	input()
	A = list(map(int, input().split()))
	print(ans(A))