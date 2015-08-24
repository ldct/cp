#!/usr/bin/env python3

SIZE = 300000

print("%d %d" % (SIZE, SIZE))
s = []
for i in range(SIZE // 2):
	s += ".x"
print(''.join(s))
for i in range(SIZE):
	print("1 .")