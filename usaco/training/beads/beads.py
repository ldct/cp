"""
ID: xuanji2
LANG: PYTHON3
TASK: beads
"""

def mp(s):
	s += '?'
	for i in range(len(s)):
		if s[i] != s[0]:
			break
	return i

# maximum prefix
def mpw(s):
	return max(mp(s.replace('w', 'r')), mp(s.replace('w', 'b')))

def ans(s):
	cap = len(s)

	s += s

	s = ''.join(s)

	ret = -1
	for i in range(1,len(s)):
		a, b = s[0:i], s[i:]
		x = mpw(a[::-1])
		y = mpw(b)
		candidate = min(cap, x + y)
		# print(a, b, x, y, candidate)
		ret = max(ret, candidate)
	return ret

with open("beads.in") as f:
	with open("beads.out", 'w') as fo:
		[a, b] = f.readlines()
		b = b[:-1]
		print(ans(b), file=fo)