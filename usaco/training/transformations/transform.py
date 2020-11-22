"""
ID: xuanji2
LANG: PYTHON3
TASK: transform
"""

def rot90(grid):
	tmp = zip(*grid)
	return [''.join(l[::-1]) for l in tmp]

def rot180(grid):
	return rot90(rot90(grid))

def rot270(grid):
	return rot90(rot180(grid))

def refl(grid):
	return [''.join(l[::-1]) for l in grid]

def ans(start, end):
	if rot90(start) == end: return 1
	if rot180(start) == end: return 2
	if rot270(start) == end: return 3
	if refl(start) == end: return 4
	for f in [rot90, rot180, rot270]:
		if f(refl(start)) == end: return 5
	if start == end: return 6
	return 7

with open("transform.in") as f:
	with open("transform.out", 'w') as fo:
		lines = f.readlines()
		N = int(lines[0])
		lines = [l[0:-1] for l in lines[1:]]
		start = lines[:N]
		end = lines[N:]
		print(ans(start, end), file=fo)
