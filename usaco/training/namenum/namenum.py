"""
ID: xuanji2
LANG: PYTHON3
TASK: namenum
"""

import itertools

def p1(c):
	if c == '2': return "ABC"
	if c == '3': return "DEF"
	if c == '4': return "GHI"
	if c == '5': return "JKL"
	if c == '6': return "MNO"
	if c == '7': return "PRS"
	if c == '8': return "TUV"
	if c == '9': return "WXY"

	assert(False)

def possibilities(name):
	return (''.join(x) for x in itertools.product(*map(p1, name)))

def ans(name):
	with open("dict.txt") as f:
		acceptable = set([l[:-1] for l in f.readlines()])

	with open("namenum.out", 'w') as fo:
		ret = acceptable & set(possibilities(name))

		if len(ret) == 0:
			print("NONE", file=fo)
		else:
			ret = sorted(ret)
			for n in ret:
				print(n, file=fo)

with open("namenum.in") as f:
	lines = f.readlines()
	ans(lines[0][0:-1])
