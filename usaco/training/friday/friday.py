"""
ID: xuanji2
LANG: PYTHON3
TASK: friday
"""

def is_leap_year(year):
	if year % 400 == 0: return True
	if year % 100 == 0: return False
	return year % 4 == 0

def next(year, month, day):
	DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	if is_leap_year(year):
		DAYS_IN_MONTH[1] += 1

	day += 1
	if day == DAYS_IN_MONTH[month]:
		day = 0
		month += 1

	if month == 12:
		month = 0
		year += 1

	return (year, month, day)


def ans(N):
	ret = [0,0,0,0,0,0,0]

	day = 0
	month = 0
	year = 1900
	dow = 2

	while (year, month, day) != (1900+N, 0, 0):
		if day == 12:
			ret[dow] += 1

		year, month, day = next(year, month, day)
		dow += 1
		dow %= 7

	return ret


with open("friday.in") as f:
	with open("friday.out", 'w') as fo:
		[N] = f.readlines()
		N = int(N)
		print(*ans(N), file=fo)
