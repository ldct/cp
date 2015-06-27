#!/usr/bin/env python3

l = input()

def insert_before(s, c, i):
	if i == len(s):
		return s + c
	else:
		return s[0:i] + c + s[i:]

books = set()

for i in range(len(l) + 1):
	for c in 'abcdefghijklmnopqrstuvwxyz':
		s = insert_before(l, c, i)
		books.add(s)

print(len(books))