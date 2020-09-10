#!/usr/bin/env pypy3

def fprint(*args):
	print(*args, flush=True)

N = int(input())

value_of = dict()
unknown = list(range(1, N+1))

while len(unknown) >= 2:
	a = unknown.pop()
	b = unknown.pop()
	fprint(f"? {a} {b}")
	r1 = int(input())
	fprint(f"? {b} {a}")
	r2 = int(input())

	if r1 > r2:
		# pa % pb > pb % pa
		# pb > pa
		# pa % pb == pa
		value_of[a] = r1
		unknown += [b]
	elif r2 > r1:
		value_of[b] = r2
		unknown += [a]

assert(len(unknown) == 1)
[idx] = unknown

known = set(value_of.values())


for i in range(1, N+1):
	if i not in known:
		value_of[idx] = i

ret = []
for i in range(1, N+1):
	ret += [value_of[i]]

fprint(' '.join(["!"] + list(map(str, ret))))

