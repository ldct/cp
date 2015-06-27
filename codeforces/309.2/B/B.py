#!/usr/bin/env python3

n = int(input())

rows = []

for i in range(n):
	row = input()
	rows += [row]


def sweepColumn(rows, i):
	def sweep(row):
		return row[0:i] + ('1' if row[i] == '0' else '0') + row[i+1:]
	return [sweep(row) for row in rows]

def sweepColumns(rows, idxs):
	if len(idxs) == 0: return rows
	return sweepColumns(sweepColumn(rows, idxs[0]), idxs[1:])

def numCleanRows(rows):
	return len(list(row for row in rows if '1' not in row))

def dirtyIdxs(row):
	return list(i for i, e in enumerate(row) if e == '1')

print(max(numCleanRows(sweepColumns(rows, dirtyIdxs(row))) for row in rows))