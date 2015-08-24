#!/usr/bin/env python3

N = int(input())

room = set()

max_occupancy = 0

for _ in range(N):
	command, uid = input().split()
	uid = int(uid)

	if command == '+': room.add(uid)
	if command == '-':
		if uid not in room:
			room.add(uid)
			max_occupancy += 1
		room.remove(uid)

	max_occupancy = max(max_occupancy, len(room))

print(max_occupancy)