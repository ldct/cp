"""
ID: xuanji2
LANG: PYTHON3
TASK: milk2
"""

def ans(lines):
	events = []

	starts = []
	ends = []

	for (start, end) in lines:
		events += [(start, -1)]
		events += [(end, +1)]
		starts += [start]
		ends += [end]

	events = sorted(events)

	nomilks = []

	last = None
	count = 0
	for time, delta in events:
		count -= delta
		if delta == -1 and count == 1 and last is not None:
			nomilks += [(last, time)]
		last = time

	if len(nomilks) == 0:
		return f"{max(ends) - min(starts)} 0"

	start = min(starts)
	milks = []

	for [a, b] in nomilks:
		milks += [(start, a)]
		start = b

	milks += [(b, max(ends))]

	return f"{max(b - a for [a, b] in milks)} {max(b - a for [a, b] in nomilks)}"

with open("milk2.in") as f:
	with open("milk2.out", 'w') as fo:
		lines = f.readlines()
		lines = lines[1:]
		lines = [l.split() for l in lines]
		lines = [tuple(map(int, l)) for l in lines]

		print(ans(lines), file=fo)
