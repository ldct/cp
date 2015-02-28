#!/usr/bin/env python3

a = input()
b = input()

def str_to_int(s):
	if len(s) == 0:
		return 0
	else:
		return str_to_int(s[:-1]) * 26 + (ord(s[-1]) - ord('a'))

def int_to_str(n):
	if n < 26:
		return chr(ord('a') + n)
	else:
		last_char = n % 26
		return int_to_str(n // 26) + chr(ord('a') + last_char)

i_a = str_to_int(a)
i_b = str_to_int(b)

if len(a) == len(b) and i_a + 1 < i_b:
	ret = int_to_str(i_a + 1)
	prefix_length = len(a) - len(ret)
	print('a'*prefix_length + ret)
else:
	print('No such string')