"""
ID: xuanji2
LANG: PYTHON3
TASK: ride
"""

def val(s):
	ret = 1
	for c in s:
		ret *= (ord(c) - ord('A') + 1)
		ret %= 47
	return ret

with open("ride.in") as f:
	with open("ride.out", 'w') as fo:
		[a, b] = f.readlines()
		a = a[:-1]
		b = b[:-1]
		if val(a) == val(b):
			print("GO", file=fo)
		else:
			print("STAY", file=fo)
